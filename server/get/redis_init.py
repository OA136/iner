import redis
import settings
import socket
import fcntl
import struct


def get_ip(name):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', name[:15]))[20:24])

pool = redis.ConnectionPool(host=get_ip(settings.eth), port=6379, password='123')
r = redis.Redis(connection_pool=pool)

'''
key = 'key'
value = {"time":'8:00', "rate": 0.12}
r.lpush(key, value)
element = r.rpop(key)
element = eval(element)
print element.get('time'), element.get('rate'),
'''