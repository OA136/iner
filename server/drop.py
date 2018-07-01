import psutil
import datetime
import time
import os
import string
import init
import sys
import settings

r = init.r
sip = init.get_ip(settings.eth) + ':6699'
if len(sys.argv) >= 2:
	space = float(sys.argv[1])
else:
	space = 1
while(True):
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        before_drop = os.popen('./drop.sh').read().split('\n')
	time.sleep(space)
        after_drop = os.popen('./drop.sh').read().split('\n')


        rx = int(after_drop[0]) - int(before_drop[0])
        drop = int(after_drop[1]) - int(before_drop[1])

        if rx != 0:
                drop = drop/(rx*1.0)
        else:
                drop = 0
        values = {}
        values['time'] = now

        values['DROP_RATE'] = drop

        r.lpush('DROP_RATE', values)
