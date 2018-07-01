
#!/usr/bin/python
# coding: UTF-8
import StringIO
import pycurl
import sys
import os
import datetime
import insert
import requests
import redis_init
import time
import settings

r = redis_init.r
class Test:
        def __init__(self):
                self.contents = ''
        def body_callback(self,buf):
                self.contents = self.contents + buf
 
 
def test_gzip(input_url):
        t = Test()
        #gzip_test = file("gzip_test.txt", 'w')
        c = pycurl.Curl()
        c.setopt(pycurl.WRITEFUNCTION,t.body_callback)
        c.setopt(pycurl.ENCODING, 'gzip')
        c.setopt(pycurl.URL,input_url)
        c.perform()
        http_code = c.getinfo(pycurl.HTTP_CODE)
        #http_conn_time =  c.getinfo(pycurl.CONNECT_TIME)
        #http_pre_tran =  c.getinfo(pycurl.PRETRANSFER_TIME)
        #http_start_tran =  c.getinfo(pycurl.STARTTRANSFER_TIME)
        http_total_time = c.getinfo(pycurl.TOTAL_TIME)
        #http_size = c.getinfo(pycurl.SIZE_DOWNLOAD)
        #print 'http_code http_size conn_time pre_tran start_tran total_time'
        #print "%d %d %f %f %f %f"%(http_code,http_size,http_conn_time,http_pre_tran,http_start_tran,http_total_time)
        


def test_time(url):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        req = requests.get(url)
        rate = req.elapsed.microseconds/1000.0
        value = {}
        value['time'] = now
        value['rate'] = rate
        r.lpush('SERVICE', value)
        #insert.insert_data('SERVICE', now, req.elapsed.microseconds/1000.0)
 
if __name__ == '__main__':
        input_url = sys.argv[1]
        #test_gzip(input_url)
        if len(sys.argv) >= 3:
                space = float(sys.argv[2])
        else:
                space = 1
        while (True):
                test_time(input_url)
                time.sleep(space)
