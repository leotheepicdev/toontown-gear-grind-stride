import json, os, sys
import cookielib
import urllib
import urllib2


req_version = (2,7,9)
cur_version = sys.version_info
if cur_version < req_version:
    print 'Your version of python is too old. Please upgrade to 2.7.9.'
    sys.exit()

username = os.environ['ttUsername']
password = os.environ['ttPassword']
distribution = 'qa'

accountServerEndpoint = 'https://toontownstride.com/api/'

data = urllib.urlencode({'username': username, 'password': password, 'distribution': distribution, 'version': 'dev'})
cookie_jar = cookielib.LWPCookieJar()
cookie = urllib2.HTTPCookieProcessor(cookie_jar)
opener = urllib2.build_opener(cookie)
req = urllib2.Request(accountServerEndpoint + 'login', data,
                      headers={"Content-Type" : "application/x-www-form-urlencoded"})
req.get_method = lambda: "POST"
_response = opener.open(req).read()

try:
    response = json.loads(_response)
except ValueError:
    print "Couldn't verify account credentials."
else:
    if response['status'] != 7:
        print response['message']
    else:
        os.environ['TT_PLAYCOOKIE'] = response['token']
        os.environ['TT_GAMESERVER'] = response['gameserver']

        # Start the game:
        import toontown.toonbase.ClientStart