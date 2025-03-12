from panda3d.core import HTTPChannel, loadPrcFile, loadPrcFileData, NodePath
import __builtin__


__builtin__.process = 'ai'

import sys, os
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../lib"
        )
    )
)

import argparse
import gc

# Panda3D 1.10.0 is 63.
gc.disable()

parser = argparse.ArgumentParser()
parser.add_argument('--base-channel', help='The base channel that the server may use.')
parser.add_argument('--max-channels', help='The number of channels the server may use.')
parser.add_argument('--stateserver', help="The control channel of this AI's designated State Server.")
parser.add_argument('--district-name', help="What this AI Server's district will be named.")
parser.add_argument('--district-difficulty', help="How hard the AI Server's district will be.")
parser.add_argument('--astron-ip', help="The IP address of the Astron Message Director to connect to.")
parser.add_argument('--eventlogger-ip', help="The IP address of the Astron Event Logger to log to.")
parser.add_argument('config', nargs='*', default=['config/general.prc', 'config/release/dev.prc'], help="PRC file(s) to load.")
args = parser.parse_args()

for prc in args.config:
    loadPrcFile(prc)

if os.path.isfile('config/local.prc'):
    loadPrcFile('config/local.prc')
	
for dtool in ('children', 'parent', 'name'):
    del NodePath.DtoolClassDict[dtool]

localconfig = ''
if args.base_channel: localconfig += 'air-base-channel %s\n' % args.base_channel
if args.max_channels: localconfig += 'air-channel-allocation %s\n' % args.max_channels
if args.stateserver: localconfig += 'air-stateserver %s\n' % args.stateserver
if args.district_name: localconfig += 'district-name %s\n' % args.district_name
if args.district_difficulty: localconfig+= 'district-difficulty %s\n' % args.district_difficulty
if args.astron_ip: localconfig += 'air-connect %s\n' % args.astron_ip
if args.eventlogger_ip: localconfig += 'eventlog-host %s\n' % args.eventlogger_ip
loadPrcFileData('Command-line', localconfig)

from otp.ai.AIBaseGlobal import *

from toontown.ai.ToontownAIRepository import ToontownAIRepository
simbase.air = ToontownAIRepository(config.GetInt('air-base-channel', 401000000),
                                   config.GetInt('air-stateserver', 4002),
                                   config.GetString('district-name', 'Devhaven'),
                                   config.GetInt('district-difficulty', 0))
host = config.GetString('air-connect', '127.0.0.1')
port = 7100
if ':' in host:
    host, port = host.split(':', 1)
    port = int(port)
simbase.air.connect(host, port)

gc.enable()

try:
    run()
except SystemExit:
    raise
except Exception:
    info = describeException()

    simbase.air.writeServerEvent('ai-exception', avId=simbase.air.getAvatarIdFromSender(), accId=simbase.air.getAccountIdFromSender(), exception=info)

    from raven import Client
    from os.path import expanduser

    errorReporter = Client(config.GetString('sentry-dsn', ''))
    errorReporter.user_context({
        'district_name': os.getenv('DISTRICT_NAME', ''),
        'AVID_SENDER': simbase.air.getAvatarIdFromSender(),
        'ACID_SENDER': simbase.air.getAccountIdFromSender(),
        'homedir': expanduser('~'),
        'critical': 'True'})
    errorReporter.captureMessage(info)

    raise
