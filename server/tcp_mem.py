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

        mem=psutil.virtual_memory()
        mem_percent = mem.percent
        
	connections = os.popen('./connections.sh '+sip).read()

        values = {}
        values['time'] = now

        values['TCP'] = int(connections)
        r.lpush('TCP', values)
	
	values['MEMORY'] = mem_percent
        r.lpush('MEMORY', values)
	
	time.sleep(space)
#	print num
