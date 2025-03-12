from direct.directnotify.DirectNotifyGlobal import directNotify

import os, platform, re, json, struct, socket, uuid, time

class ToontownDiscordPresence(object):
    notify = directNotify.newCategory('ToontownDiscordPresence')
    notify.setInfo(True)

    def __init__(self, client_id):
        super(ToontownDiscordPresence, self).__init__()
        self.platform = self._get_platform()
        self.ipc_path = self._get_ipc_path()
        self.client_id = client_id
        self.pid = os.getpid()
        self.connected = False
        self.activity = None
        self.socket = None
        self.haveDiscord = True
        self.connectedSince = int(time.time())
        self.data = {}
        self.activityLevels = []

    def _get_platform(self):
        return 'windows'

    def _get_ipc_path(self, id=0):
        if self.platform == 'windows':
            return ('\\\\?\\pipe\\discord-ipc-{0}').format(id)
        path = os.environ.get('XDG_RUNTIME_DIR') or os.environ.get('TMPDIR') or os.environ.get('TMP') or os.environ.get('TEMP') or '/tmp'
        return re.sub('\\/$', '', path) + ('/discord-ipc-{0}').format(id)

    def _encode(self, opcode, payload):
        payload = json.dumps(payload)
        payload = payload.encode('utf-8')
        return struct.pack('<ii', opcode, len(payload)) + payload

    def _decode(self):
        if not self.haveDiscord:
            return
        if self.platform == 'windows':
            encoded_header = ''
            header_size = 8
            while header_size:
                encoded_header += self.socket.read(header_size)
                header_size -= len(encoded_header)

            decoded_header = struct.unpack('<ii', encoded_header)
            encoded_data = ''
            remaining_packet_size = int(decoded_header[1])
            while remaining_packet_size:
                encoded_data += self.socket.read(remaining_packet_size)
                remaining_packet_size -= len(encoded_data)

        else:
            recived_data = self.socket.recv(1024)
            encoded_header = recived_data[:8]
            decoded_header = struct.unpack('<ii', encoded_header)
            encoded_data = recived_data[8:]
        return json.loads(encoded_data.decode('utf-8'))

    def _send(self, opcode, payload):
        encoded_payload = self._encode(opcode, payload)
        try:
            if self.platform == 'windows':
                self.socket.seek(0, 2)
                self.socket.write(encoded_payload)
                self.socket.flush()
            else:
                self.socket.send(encoded_payload)
        except Exception as e:
            self.notify.warning("Can't send data to Discord via IPC.")
            self.notify.warning(e)
            self.haveDiscord = False

    def open(self):
        if self.connected or not self.haveDiscord:
            pass
        else:
            try:
                if self.platform == 'windows':
                    self.socket = open(self.ipc_path, 'w+b')
                else:
                    self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                    self.socket.connect(self.ipc_path)
            except Exception:
                self.notify.warning("Can't connect to Discord Client.")
                self.haveDiscord = False
                return

            self._send(0, {'v': 1, 
               'client_id': self.client_id})
            self._decode()
            self.connected = True
            self.connectedSince = int(time.time())

    def close(self):
        self._send(2, {})
        try:
            if self.platform != 'windows':
                self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()
        except:
            pass

        self.socket = None
        self.connected = False
        self.activity = None
        return

    def set_activity(self, activity):
        self.haveDiscord = True
        if not self.connected:
            self.open()
        if not self.haveDiscord:
            return
        payload = {'cmd': 'SET_ACTIVITY', 
           'args': {'activity': activity, 
                    'pid': self.pid}, 
           'nonce': str(uuid.uuid4())}
        self._send(1, payload)
        self._decode()

    def send_general(self):
        RPCactivity = {'timestamps': {'start': self.connectedSince}, 
           'assets': {'large_text': 'Toontown Gear Grind', 
                      'large_image': 'logo_square'}}
        self.activityLevels = []
        self.push_activity(RPCactivity, 0)

    def push_activity(self, activity, level):
        self.activityLevels = self.activityLevels[:level]
        self.activityLevels.append(activity)
        self.set_activity(activity)

    def pop_activity(self):
        self.activityLevels.pop()
        if len(self.activityLevels) == 0:
            self.send_general()
        else:
            self.set_activity(self.activityLevels[-1])