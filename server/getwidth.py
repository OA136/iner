import psutil
import time
import os
import string
#import insert
import datetime
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
	before = psutil.net_io_counters(True)[settings.eth]

	
	before_drop = os.popen('./drop.sh').read().split('\n')
	

	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	time.sleep(space)
	after = psutil.net_io_counters(True)[settings.eth]

	income = after[1] - before[1]
	out = after[0] - before[0]


	income = income/1024.0/1024.0
	out = out/1024.0/1024.0
	in_out = income + out
	width = in_out
	#width = in_out/125.0

	#print "income: %fMB out: %fMB wtdth_rate: %f%%" % (income, out, width*100)

	connections = os.popen('./connections.sh '+sip).read()
#print connections


	after_drop = os.popen('./drop.sh').read().split('\n')
	rx = int(after_drop[0]) - int(before_drop[0])
	drop = int(after_drop[1]) - int(before_drop[1])

	if rx != 0:
		drop = drop/(rx*1.0)
	else:
		drop = 0

        values = {}
        values['time'] = now
        values['rate'] = int(connections)
        r.lpush('TCP', values)

        values['rate'] = width
        r.lpush('WIDTH', values)

	values['rate'] = drop
	r.lpush('DROP_RATE', values)
'''

insert.insert_data('TCP', now, int(connections))
insert.insert_data('WIDTH', now, width)
#insert.insert_data('DROP_PACKET', now, drop)
'''
