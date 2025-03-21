# Distribution:
distribution dev

# Art assets:
vfs-mount ../resources/phase_3 /phase_3
vfs-mount ../resources/phase_3.5 /phase_3.5
vfs-mount ../resources/phase_4 /phase_4
vfs-mount ../resources/phase_5 /phase_5
vfs-mount ../resources/phase_5.5 /phase_5.5
vfs-mount ../resources/phase_6 /phase_6
vfs-mount ../resources/phase_7 /phase_7
vfs-mount ../resources/phase_8 /phase_8
vfs-mount ../resources/phase_9 /phase_9
vfs-mount ../resources/phase_10 /phase_10
vfs-mount ../resources/phase_11 /phase_11
vfs-mount ../resources/phase_12 /phase_12
vfs-mount ../resources/phase_13 /phase_13
vfs-mount ../resources/phase_14 /phase_14
vfs-mount ../resources/server /server
model-path /

# Server:
server-version ttgg-dev
min-access-level 700
#accountdb-type live
accountdb-type developer
shard-low-pop 50
shard-mid-pop 100

# DClass file:
dc-file config/toontown.dc

# Core features:
want-pets #t
want-parties #t
want-cogdominiums #t
want-lawbot-cogdo #t
want-cashbot-cogdo #t
want-bossbot-cogdo #t
want-anim-props #t
want-game-tables #t
want-find-four #t
want-chinese-checkers #t
want-checkers #t
want-house-types #t
want-gifting #t

# Chat:
want-whitelist #f
want-sequence-list #f

# Developer options:
show-population #t
want-instant-parties #t
cogdo-pop-factor 1.5
cogdo-ratio 0.5
default-directnotify-level info

# Gameserver (SSL/TLS):
# ssl-mod dev
# ssl-certs-folder ./lib/astron/certs/dev/

# Speedhack
want-speedhack-check #f