import time
import tilt

while True:
    res = tilt.getFirstTilt()
    print res
    time.sleep(2)
