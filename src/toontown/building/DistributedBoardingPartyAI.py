from otp.ai.AIBase import *
from toontown.base import ToontownGlobals
from direct.distributed.ClockDelta import *
from ElevatorConstants import *
from direct.distributed import DistributedObjectAI
from direct.fsm import ClassicFSM, State
from direct.task import Task
from direct.directnotify import DirectNotifyGlobal
from toontown.building import BoardingPartyBase
GROUPMEMBER = 0
GROUPINVITE = 1

class DistributedBoardingPartyAI(DistributedObjectAI.DistributedObjectAI, BoardingPartyBase.BoardingPartyBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardingPartyAI')

    def __init__(self, air, elevatorList, maxSize = 4):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        BoardingPartyBase.BoardingPartyBase.__init__(self)
        self.setGroupSize(maxSize)
        self.elevatorIdList = elevatorList
        self.visibleZones = []

    def delete(self):
        self.cleanup()
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)
        for elevatorId in self.elevatorIdList:
            elevator = simbase.air.doId2do.get(elevatorId)
            elevator.setBoardingParty(self)

        '''
        store = simbase.air.dnaStoreMap.get(self.zoneId)
        if store:
            numVisGroups = store.getNumDNAVisGroupsAI()
            myVisGroup = None
            for index in xrange(numVisGroups):
                if store.getDNAVisGroupAI(index).getName() == str(self.zoneId):
                    myVisGroup = store.getDNAVisGroupAI(index)

            if myVisGroup:
                numVisibles = myVisGroup.getNumVisibles()
                for index in xrange(numVisibles):
                    newVisible = myVisGroup.getVisibleName(index)
                    self.visibleZones.append(int(newVisible))

            else:
                self.visibleZones = [self.zoneId]
        else:
            self.visibleZones = [self.zoneId]
        '''
        return

    def cleanup(self):
        BoardingPartyBase.BoardingPartyBase.cleanup(self)
        del self.elevatorIdList
        del self.visibleZones

    def getElevatorIdList(self):
        return self.elevatorIdList

    def setElevatorIdList(self, elevatorIdList):
        self.elevatorIdList = elevatorIdList

    def addWacthAvStatus(self, avId):
        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.handleAvatarDisco, extraArgs=[avId])
        self.accept(self.staticGetLogicalZoneChangeEvent(avId), self.handleAvatarZoneChange, extraArgs=[avId])
        messageToonAdded = 'Battle adding toon %s' % avId
        self.accept(messageToonAdded, self.handleToonJoinedBattle)
        messageToonReleased = 'Battle releasing toon %s' % avId
        self.accept(messageToonReleased, self.handleToonLeftBattle)

    def handleToonJoinedBattle(self, avId):
        self.notify.debug('handleToonJoinedBattle %s' % avId)

    def handleToonLeftBattle(self, avId):
        self.notify.debug('handleToonLeftBattle %s' % avId)

    def removeWacthAvStatus(self, avId):
        self.ignore(self.air.getAvatarExitEvent(avId))
        self.ignore(self.staticGetLogicalZoneChangeEvent(avId))

    # BoardingParty data model
    #
    # groupList[0] - people in the group
    # groupList[1] - people invited to the group
    # groupList[2] - people kicked from the group
    #
    # avIdDict - lookup from player to the leader of the group they are in
    #     if you are in a group or have been invited to a group, you
    #     are in this dictionary with a pointer to the leader of the
    #     group.   The only exception to this is if you were invited
    #     to merge groups.
    # mergeDict - This is a link that points back to the original
    #     invitee before we mapped it to the leader of the other group.

    def requestInvite(self, inviteeId):
        self.notify.debug('requestInvite %s' % inviteeId)
        inviterId = self.air.getAvatarIdFromSender()
        invitee = simbase.air.doId2do.get(inviteeId)
        originalInviteeId = inviteeId
        merger = False
        if invitee and invitee.battleId != 0:
            reason = BoardingPartyBase.BOARDCODE_BATTLE
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        if self.hasPendingInvite(inviteeId):
            reason = BoardingPartyBase.BOARDCODE_PENDING_INVITE
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        if self.__isInElevator(inviteeId):
            reason = BoardingPartyBase.BOARDCODE_IN_ELEVATOR
            self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason])
            self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
            return
        if self.hasActiveGroup(inviteeId):
            # We could make the assumption both are in the avIdDict but I'd prefer not to blow up the district
            if self.hasActiveGroup(inviterId):
                inviteeLeaderId = self.avIdDict[inviteeId]
                leaderId = self.avIdDict[inviterId]

                # group merge already requested?
                if self.hasPendingInvite(inviteeLeaderId):
                    reason = BoardingPartyBase.BOARDCODE_PENDING_INVITE
                    self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason])
                    self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
                    return

                if ((len(self.getGroupMemberList(leaderId)) + len(self.getGroupMemberList(inviteeLeaderId))) <= self.maxSize):
                    # Lets send the invitation to the person in authority...
                    invitee = simbase.air.doId2do.get(inviteeLeaderId)
                    inviteeId = inviteeLeaderId
                    merger = True
                else:
                    reason = BoardingPartyBase.BOARDCODE_GROUPS_TOO_LARGE
                    self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason])
                    self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
                    return
            else:
                reason = BoardingPartyBase.BOARDCODE_DIFF_GROUP
                self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason])
                self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
                return
        # Lets see what the invitee is currently doing
        inviteeOkay = self.checkBoard(inviteeId, self.elevatorIdList[0])
        reason = 0
        # I know there is an unexpected issue here when we are merging groups... lets think about this really hard..
        if len(self.elevatorIdList) == 1:
            if inviteeOkay:
                if inviteeOkay == REJECT_PROMOTION:
                    reason = BoardingPartyBase.BOARDCODE_PROMOTION
                self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason])
                return
            else:
                inviterOkay = self.checkBoard(inviterId, self.elevatorIdList[0])
                if inviterOkay:
                    if inviterOkay == REJECT_PROMOTION:
                        reason = BoardingPartyBase.BOARDCODE_PROMOTION
                    self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviterId, reason])
                    return
        # Is the inviter already in the avIdDict?  It follows they either must be in a group or have a pending invite...
        if inviterId in self.avIdDict:
            self.notify.debug('old group')
            # Everything is indexed by the leaders
            leaderId = self.avIdDict[inviterId]
            groupList = self.groupListDict.get(leaderId)
            if groupList:  # One would hope we have a group...
                self.notify.debug('got group list')
                # Only the leader of a group can invite somebody who was kicked out back in
                if inviterId == leaderId:
                    # The invitee was kicked out so lets let them back in again
                    if inviteeId in groupList[2]:
                        groupList[2].remove(inviteeId)
                # Is the group already oversized?
                if len(self.getGroupMemberList(leaderId)) >= self.maxSize:
                    self.sendUpdate('postSizeReject', [leaderId, inviterId, inviteeId])
                elif merger:
                    # We cannot muck with the avIdDict because they are pointing to their original groups.
                    # We shall stash away the info into a different
                    # dictionary.. This way, if something goes wrong,
                    # the original groups  with their original data
                    # structures are untouched.   The mergeDict gives
                    # us a pointer back to where the original invite
                    # went to so that we can issue a notice to close
                    # the appropriate invite dialog
                    self.mergeDict[inviteeId] = originalInviteeId
                    self.sendUpdateToAvatarId(inviteeId, 'postInvite', [leaderId, inviterId, True])
                    # notify everybody in the inviters group of the
                    # invitation..
                    for memberId in groupList[0]:
                        if not memberId == inviterId:
                            self.sendUpdateToAvatarId(memberId, 'postMessageInvited', [inviteeId, inviterId])
                elif inviterId not in groupList[1] and inviterId not in groupList[2]:
                    # If the invitee isn't already in the group, add them..
                    if inviteeId not in groupList[1]:
                        groupList[1].append(inviteeId)
                    self.groupListDict[leaderId] = groupList
                    if inviteeId in self.avIdDict:
                        self.notify.warning('inviter %s tried to invite %s who already exists in the avIdDict.' % (inviterId, inviteeId))
                        self.air.writeServerEvent('suspicious: inviter', inviterId, ' tried to invite %s who already exists in the avIdDict.' % inviteeId)
                    self.avIdDict[inviteeId] = leaderId
                    self.sendUpdateToAvatarId(inviteeId, 'postInvite', [leaderId, inviterId, False])
                    # notify everybody of the invitation..
                    for memberId in groupList[0]:
                        if not memberId == inviterId:
                            self.sendUpdateToAvatarId(memberId, 'postMessageInvited', [inviteeId, inviterId])
                # The inviter was kicked.. so, we cannot let them back in since they are not the leader...
                elif inviterId in groupList[2]:
                    self.sendUpdate('postKickReject', [leaderId, inviterId, inviteeId])
        else:
            if inviteeId in self.avIdDict:
                self.notify.warning('inviter %s tried to invite %s who already exists in avIdDict.' % (inviterId, inviteeId))
                self.air.writeServerEvent('suspicious: inviter', inviterId, ' tried to invite %s who already exists in the avIdDict.' % inviteeId)
            self.notify.debug('new group')
            # The inviter is now the leader of the new group
            leaderId = inviterId
            self.avIdDict[inviterId] = inviterId
            self.avIdDict[inviteeId] = inviterId
            self.groupListDict[leaderId] = [[leaderId], [inviteeId], []]
            self.addWacthAvStatus(leaderId)
            self.sendUpdateToAvatarId(inviteeId, 'postInvite', [leaderId, inviterId, False])

    def requestCancelInvite(self, inviteeId):
        inviterId = self.air.getAvatarIdFromSender()
        if inviteeId in self.mergeDict:
            inviteeId = self.mergeDict.pop(inviteeId)
            self.sendUpdateToAvatarId(inviteeId, 'postInviteCanceled', [])
            return
        if inviterId in self.avIdDict:
            leaderId = self.avIdDict[inviterId]
            groupList = self.groupListDict.get(leaderId)
            if groupList:
                self.removeFromGroup(leaderId, inviteeId)
                self.sendUpdateToAvatarId(inviteeId, 'postInviteCanceled', [])

    def requestAcceptInvite(self, leaderId, inviterId):
        inviteeId = self.air.getAvatarIdFromSender()
        self.notify.debug('requestAcceptInvite leader%s inviter%s invitee%s' % (leaderId, inviterId, inviteeId))
        if inviteeId in self.avIdDict:
            if inviteeId in self.mergeDict:
                # Clean things up in case we back this operation out
                oldId = self.mergeDict.pop(inviteeId)
                # Check the state of things to deal with odd race conditions
                # both should still be in the avIdDict
                if leaderId not in self.avIdDict or inviteeId not in self.avIdDict:
                    self.notify.warning('leaderId not in self.avIdDict or inviteeId not in self.avIdDict');
                    self.sendUpdateToAvatarId(inviteeId, 'postSomethingMissing', [])
                    return
                # Does the leader still have a group?
                if leaderId not in self.groupListDict:
                    self.notify.warning('the leader does not have a group?');
                    self.sendUpdateToAvatarId(inviteeId, 'postSomethingMissing', [])
                    return
                # They should STILL be the leaders.. right?
                if leaderId != self.avIdDict[leaderId]:
                    self.notify.warning('leaderId != self.avIdDict[leaderId]');
                    self.sendUpdateToAvatarId(inviteeId, 'postSomethingMissing', [])
                    return
                # They should STILL be the leaders.. right?
                if inviteeId != self.avIdDict[inviteeId]:
                    self.notify.warning('inviteeId != self.avIdDict[inviteeId]');
                    self.sendUpdateToAvatarId(inviteeId, 'postSomethingMissing', [])
                    return
                # both should still have active groups
                if not self.hasActiveGroup(inviteeId) or not self.hasActiveGroup(leaderId):
                    self.notify.warning('not self.hasActiveGroup(inviteeId) or not self.hasActiveGroup(leaderId)');
                    self.sendUpdateToAvatarId(inviteeId, 'postSomethingMissing', [])
                    return
                # Lets make sure we still CAN merge them in
                if ((len(self.getGroupMemberList(leaderId)) + len(self.getGroupMemberList(inviteeId))) > self.maxSize):
                    reason = BoardingPartyBase.BOARDCODE_GROUPS_TOO_LARGE
                    self.sendUpdateToAvatarId(inviterId, 'postInviteNotQualify', [inviteeId, reason])
                    self.sendUpdateToAvatarId(inviteeId, 'postMessageInvitationFailed', [inviterId])
                    return
                group = self.groupListDict.get(leaderId)
                # Something is wonky
                if group == None or (len(group) < 3):
                    self.notify.warning('the leader has a group but it is null or too short')
                    self.sendUpdateToAvatarId(inviteeId, 'postSomethingMissing', [])
                    return
                # get the memberList of the invitee and add it into the leaders group
                memberList = self.getGroupMemberList(inviteeId)
                for memberId in memberList:
                    self.addToGroup(leaderId, memberId, 0)
                # get rid of the old group (invitee is always the old leader)
                self.groupListDict.pop(inviteeId)
                # notify everybody of their new group info
                self.sendUpdateToAvatarId(inviterId, 'postInviteAccepted', [oldId])
                self.sendUpdate('postGroupInfo', [leaderId, group[0], group[1], group[2]])
                return
            if self.hasActiveGroup(inviteeId):
                self.sendUpdateToAvatarId(inviteeId, 'postAlreadyInGroup', [])
                return
            if leaderId not in self.avIdDict or not self.isInGroup(inviteeId, leaderId):
                self.sendUpdateToAvatarId(inviteeId, 'postSomethingMissing', [])
                return
            memberList = self.getGroupMemberList(leaderId)
            if self.avIdDict[inviteeId]:
                if self.avIdDict[inviteeId] == leaderId:
                    if inviteeId in memberList:
                        self.notify.debug('invitee already in group, aborting requestAcceptInvite')
                        return
                else:
                    self.air.writeServerEvent('suspicious: ', inviteeId, " accepted a second invite from %s, in %s's group, while he was in alredy in %s's group." % (inviterId, leaderId, self.avIdDict[inviteeId]))
                    self.removeFromGroup(self.avIdDict[inviteeId], inviteeId, post=0)
            if len(memberList) >= self.maxSize:
                self.removeFromGroup(leaderId, inviteeId)
                self.sendUpdateToAvatarId(inviterId, 'postMessageAcceptanceFailed', [inviteeId, BoardingPartyBase.INVITE_ACCEPT_FAIL_GROUP_FULL])
                self.sendUpdateToAvatarId(inviteeId, 'postGroupAlreadyFull', [])
                return
            self.sendUpdateToAvatarId(inviterId, 'postInviteAccepted', [inviteeId])
            self.addToGroup(leaderId, inviteeId)
        else:
            self.air.writeServerEvent('suspicious: ', inviteeId, " was invited to %s's group by %s, but the invitee didn't have an entry in the avIdDict." % (leaderId, inviterId))

    def requestRejectInvite(self, leaderId, inviterId):
        inviteeId = self.air.getAvatarIdFromSender()
        if inviteeId in self.mergeDict:
            inviteeId = self.mergeDict.pop(inviteeId)
        else:
            self.removeFromGroup(leaderId, inviteeId)
        self.sendUpdateToAvatarId(inviterId, 'postInviteDelcined', [inviteeId])

    def requestKick(self, kickId):
        leaderId = self.air.getAvatarIdFromSender()
        if kickId in self.avIdDict:
            if self.avIdDict[kickId] == leaderId:
                self.removeFromGroup(leaderId, kickId, kick=1)
                self.sendUpdateToAvatarId(kickId, 'postKick', [leaderId])

    def requestLeave(self, leaderId):
        memberId = self.air.getAvatarIdFromSender()
        if memberId in self.avIdDict:
            if leaderId == self.avIdDict[memberId]:
                self.removeFromGroup(leaderId, memberId)

    def checkBoard(self, avId, elevatorId):
        elevator = simbase.air.doId2do.get(elevatorId)
        avatar = simbase.air.doId2do.get(avId)
        if avatar and elevator:
            return elevator.checkBoard(avatar)
        return REJECT_BOARDINGPARTY

    def testBoard(self, leaderId, elevatorId, needSpace = 0):
        elevator = None
        boardOkay = BoardingPartyBase.BOARDCODE_MISSING
        avatarsFailingRequirements = []
        avatarsInBattle = []
        if elevatorId in self.elevatorIdList:
            elevator = simbase.air.doId2do.get(elevatorId)
        if elevator:
            if leaderId in self.avIdDict:
                if leaderId == self.avIdDict[leaderId]:
                    boardOkay = BoardingPartyBase.BOARDCODE_OKAY
                    for avId in self.getGroupMemberList(leaderId):
                        avatar = simbase.air.doId2do.get(avId)
                        if avatar:
                            if elevator.checkBoard(avatar) != 0:
                                if elevator.checkBoard(avatar) == REJECT_PROMOTION:
                                    boardOkay = BoardingPartyBase.BOARDCODE_PROMOTION
                                avatarsFailingRequirements.append(avId)
                            elif avatar.battleId != 0:
                                boardOkay = BoardingPartyBase.BOARDCODE_BATTLE
                                avatarsInBattle.append(avId)

                    groupSize = len(self.getGroupMemberList(leaderId))
                    if groupSize > self.maxSize:
                        boardOkay = BoardingPartyBase.BOARDCODE_SPACE
                    if needSpace:
                        if groupSize > elevator.countOpenSeats():
                            boardOkay = BoardingPartyBase.BOARDCODE_SPACE
        if boardOkay != BoardingPartyBase.BOARDCODE_OKAY:
            self.notify.debug('Something is wrong with the group board request')
            if boardOkay == BoardingPartyBase.BOARDCODE_PROMOTION:
                self.notify.debug('An avatar did not meet the elevator promotion requirements')
            elif boardOkay == BoardingPartyBase.BOARDCODE_BATTLE:
                self.notify.debug('An avatar is in battle')
        return (boardOkay, avatarsFailingRequirements, avatarsInBattle)

    def requestBoard(self, elevatorId):
        wantDisableGoButton = False
        leaderId = self.air.getAvatarIdFromSender()
        elevator = None
        if elevatorId in self.elevatorIdList:
            elevator = simbase.air.doId2do.get(elevatorId)
        if elevator:
            if leaderId in self.avIdDict:
                if leaderId == self.avIdDict[leaderId]:
                    group = self.groupListDict.get(leaderId)
                    if group:
                        boardOkay, avatarsFailingRequirements, avatarsInBattle = self.testBoard(leaderId, elevatorId, needSpace=1)
                        if boardOkay == BoardingPartyBase.BOARDCODE_OKAY:
                            leader = simbase.air.doId2do.get(leaderId)
                            if leader:
                                elevator.partyAvatarBoard(leader)
                                wantDisableGoButton = True
                            for avId in group[0]:
                                if not avId == leaderId:
                                    avatar = simbase.air.doId2do.get(avId)
                                    if avatar:
                                        elevator.partyAvatarBoard(avatar, wantBoardingShow=1)

                            self.air.writeServerEvent('boarding_elevator', self.zoneId, '%s; Sending avatars %s' % (elevatorId, group[0]))
                        else:
                            self.sendUpdateToAvatarId(leaderId, 'postRejectBoard', [elevatorId,
                             boardOkay,
                             avatarsFailingRequirements,
                             avatarsInBattle])
                            return
        if not wantDisableGoButton:
            self.sendUpdateToAvatarId(leaderId, 'postRejectBoard', [elevatorId,
             BoardingPartyBase.BOARDCODE_MISSING, [], []])
        return

    def testGoButtonRequirements(self, leaderId, elevatorId):
        if leaderId in self.avIdDict:
            if leaderId == self.avIdDict[leaderId]:
                if elevatorId in self.elevatorIdList:
                    elevator = simbase.air.doId2do.get(elevatorId)
                    if elevator:
                        boardOkay, avatarsFailingRequirements, avatarsInBattle = self.testBoard(leaderId, elevatorId, needSpace=0)
                        if boardOkay == BoardingPartyBase.BOARDCODE_OKAY:
                            avList = self.getGroupMemberList(leaderId)
                            if 0 in avList:
                                avList.remove(0)
                            if leaderId not in elevator.seats:
                                return True
                            else:
                                self.notify.warning('avId: %s has hacked his/her client.' % leaderId)
                                self.air.writeServerEvent('suspicious: ', leaderId, ' pressed the GO Button while inside the elevator.')
                        else:
                            self.sendUpdateToAvatarId(leaderId, 'rejectGoToRequest', [elevatorId,
                             boardOkay,
                             avatarsFailingRequirements,
                             avatarsInBattle])
        return False

    def requestGoToFirstTime(self, elevatorId):
        callerId = self.air.getAvatarIdFromSender()
        if self.testGoButtonRequirements(callerId, elevatorId):
            self.sendUpdateToAvatarId(callerId, 'acceptGoToFirstTime', [elevatorId])

    def requestGoToSecondTime(self, elevatorId):
        callerId = self.air.getAvatarIdFromSender()
        avList = self.getGroupMemberList(callerId)
        if self.testGoButtonRequirements(callerId, elevatorId):
            for avId in avList:
                self.sendUpdateToAvatarId(avId, 'acceptGoToSecondTime', [elevatorId])

            THREE_SECONDS = 3.0
            taskMgr.doMethodLater(THREE_SECONDS, self.sendAvatarsToDestinationTask, self.uniqueName('sendAvatarsToDestinationTask'), extraArgs=[elevatorId, avList], appendTask=True)

    def sendAvatarsToDestinationTask(self, elevatorId, avList, task):
        self.notify.debug('entering sendAvatarsToDestinationTask')
        if len(avList):
            if elevatorId in self.elevatorIdList:
                elevator = simbase.air.doId2do.get(elevatorId)
                if elevator:
                    self.notify.warning('Sending avatars %s' % avList)
                    boardOkay, avatarsFailingRequirements, avatarsInBattle = self.testBoard(avList[0], elevatorId, needSpace=0)
                    if not boardOkay == BoardingPartyBase.BOARDCODE_OKAY:
                        for avId in avatarsFailingRequirements:
                            self.air.writeServerEvent('suspicious: ', avId, ' failed requirements after the second go button request.')

                        for avId in avatarsInBattle:
                            self.air.writeServerEvent('suspicious: ', avId, ' joined battle after the second go button request.')

                    self.air.writeServerEvent('boarding_go', self.zoneId, '%s; Sending avatars %s' % (elevatorId, avList))
                    elevator.sendAvatarsToDestination(avList)
        return Task.done

    def handleAvatarDisco(self, avId):
        self.notify.debug('handleAvatarDisco %s' % avId)
        if avId in self.mergeDict:
            self.mergeDict.pop(avId)
        if avId in self.avIdDict:
            leaderId = self.avIdDict[avId]
            self.removeFromGroup(leaderId, avId)

    def handleAvatarZoneChange(self, avId, zoneNew, zoneOld):
        self.notify.debug('handleAvatarZoneChange %s new%s old%s bp%s' % (avId, zoneNew, zoneOld, self.zoneId))
        if zoneNew in self.visibleZones:
            self.toonInZone(avId)
        elif avId in self.avIdDict:
            leaderId = self.avIdDict[avId]
            self.removeFromGroup(leaderId, avId)
        if avId in self.mergeDict:
            self.mergeDict.pop(avId)

    def toonInZone(self, avId):
        if avId in self.avIdDict:
            leaderId = self.avIdDict[avId]
            group = self.groupListDict.get(leaderId)
            if leaderId and group:
                self.notify.debug('Calling postGroupInfo from toonInZone')

    def addToGroup(self, leaderId, inviteeId, post = 1):
        group = self.groupListDict.get(leaderId)
        if group:
            self.avIdDict[inviteeId] = leaderId
            if inviteeId in group[1]:
                group[1].remove(inviteeId)
            if inviteeId not in group[0]:
                group[0].append(inviteeId)
            self.groupListDict[leaderId] = group
            if post:
                self.notify.debug('Calling postGroupInfo from addToGroup')
                self.sendUpdate('postGroupInfo', [leaderId, group[0], group[1], group[2]])
            self.addWacthAvStatus(inviteeId)
        else:
            self.sendUpdate('postGroupDissolve', [leaderId, leaderId, [], 0])

    def removeFromGroup(self, leaderId, memberId, kick = 0, post = 1):
        self.notify.debug('')
        self.notify.debug('removeFromGroup leaderId %s memberId %s' % (leaderId, memberId))
        self.notify.debug('Groups %s' % self.groupListDict)
        self.notify.debug('avDict %s' % self.avIdDict)
        if leaderId not in self.avIdDict:
            self.sendUpdate('postGroupDissolve', [memberId, leaderId, [], kick])
            if memberId in self.avIdDict:
                self.avIdDict.pop(memberId)
            return
        self.removeWacthAvStatus(memberId)
        group = self.groupListDict.get(leaderId)
        if group:
            if memberId in group[0]:
                group[0].remove(memberId)
            if memberId in group[1]:
                group[1].remove(memberId)
            if memberId in group[2]:
                group[2].remove(memberId)
            if kick:
                group[2].append(memberId)
        else:
            return
        if memberId == leaderId or len(group[0]) < 2:
            if leaderId in self.avIdDict:
                self.avIdDict.pop(leaderId)
                for inviteeId in group[1]:
                    if inviteeId in self.avIdDict:
                        self.avIdDict.pop(inviteeId)
                        self.sendUpdateToAvatarId(inviteeId, 'postInviteCanceled', [])

            dgroup = self.groupListDict.pop(leaderId)
            for dMemberId in dgroup[0]:
                if dMemberId in self.avIdDict:
                    self.avIdDict.pop(dMemberId)

            self.notify.debug('postGroupDissolve')
            dgroup[0].insert(0, memberId)
            self.sendUpdate('postGroupDissolve', [memberId, leaderId, dgroup[0], kick])
        else:
            self.groupListDict[leaderId] = group
            if post:
                self.notify.debug('Calling postGroupInfo from removeFromGroup')
                self.sendUpdate('postGroupInfo', [leaderId, group[0], group[1], group[2]])
        if memberId in self.avIdDict:
            self.avIdDict.pop(memberId)
        self.notify.debug('Remove from group END')
        self.notify.debug('Groups %s' % self.groupListDict)
        self.notify.debug('avDict %s' % self.avIdDict)
        self.notify.debug('')

    def informDestinationInfo(self, offset):
        leaderId = self.air.getAvatarIdFromSender()
        if offset > len(self.elevatorIdList):
            self.air.writeServerEvent('suspicious: ', leaderId, 'has requested to go to %s elevator which does not exist' % offset)
            return
        memberList = self.getGroupMemberList(leaderId)
        for avId in memberList:
            if avId != leaderId:
                self.sendUpdateToAvatarId(avId, 'postDestinationInfo', [offset])

    def __isInElevator(self, avId):
        inElevator = False
        for elevatorId in self.elevatorIdList:
            elevator = simbase.air.doId2do.get(elevatorId)
            if elevator:
                if avId in elevator.seats:
                    inElevator = True

        return inElevator
