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
#num = 0
while(True):
#	num = num + 1
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        before = psutil.net_io_counters(True)[settings.eth]
        
	time.sleep(space)
	after = psutil.net_io_counters(True)[settings.eth]
	income = after[1] - before[1]
        out = after[0] - before[0]
        income = income/1024.0/1024.0
        out = out/1024.0/1024.0
        in_out = income + out
        width = in_out


        values = {}
        values['time'] = now

        values['WIDTH'] = width
        r.lpush('WIDTH', values)
#	r.set('num', num)
