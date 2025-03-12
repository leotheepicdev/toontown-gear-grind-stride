# otp/ai
AIZoneData is currently needed for Pets. (_handleZoneChange on PetLookerAI)
Panda3D imports AIZoneData so a workaround has to be made.

DistributedObjectUD also imports otp.ai.Barrier
Not decided exactly on what to do, but use of Barrier might have to be wiped out.

# otp/distributed
Going to merge this with ToontownClientRepository. This is going to take a bit. It can't be magic.

# otp/otpbase
OTPGlobals contains Bitmask stuff. There's tons of files that need to be changed in order to wipe OTPGlobals out.
OTPLocalizer will take some time to wipe out.

# otp/otpgui
OTPDialog has to be merged with ToontownDialog