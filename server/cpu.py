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
num = 0
while(True):
	num = num + 1
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	cpu_percent = psutil.cpu_percent(space)

        values = {}
        values['time'] = now

        values['CPU'] = cpu_percent

        r.lpush('CPU', values)
	r.set('num', num)
