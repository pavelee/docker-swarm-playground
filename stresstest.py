import urllib.request, time, sys

address = sys.argv[1]
try:
    interval = float(sys.argv[2])
except IndexError:
    interval = 0.1

# print(interval)
# exit()

while 1:
    try:
        start = time.time()
        fp = urllib.request.urlopen(address)
        fp.close()
        end = time.time()
        print(end - start)
        time.sleep(interval)
    except KeyboardInterrupt:
        sys.exit()
    except:
        print('Connection problem!')