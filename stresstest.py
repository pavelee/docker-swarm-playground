import base64
from random import random
import time, sys
import urllib.request

def stresser(request):
    name = "process_%s" % random()
    while 1:
        try:
            start = time.time()
            result = urllib.request.urlopen(request)
            end = time.time()
            print("process %s: %s" % (name, end - start))
            time.sleep(interval)
        except KeyboardInterrupt:
            sys.exit()
        except:
            print('Connection problem!')

address = sys.argv[1]
try:
    interval = float(sys.argv[2])
    basicauth = sys.argv[3]
    basicauth_username = sys.argv[4]
    basicauth_password = sys.argv[5]
except IndexError:
    interval = 0.1
    basicauth = 0
    basicauth_username = ""
    basicauth_password = ""

request = urllib.request.Request(address)
if  basicauth:
    data_string = "%s:%s" % (basicauth_username,basicauth_password)
    data_bytes = data_string.encode("ascii")
    b64auth = base64.b64encode(data_bytes)
    request.add_header("Authorization", "Basic %s" % b64auth.decode('ascii'))
    
stresser(request)