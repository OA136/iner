import MySQLdb
import settings
import redis
import socket
import fcntl
import struct


def get_ip(name):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', name[:15]))[20:24])

db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
cursor = db.cursor()

pool = redis.ConnectionPool(host=get_ip(settings.eth), port=6379, password='123')
r = redis.Redis(connection_pool=pool)
def init_database(sql, table):
	cursor.execute("DROP TABLE IF EXISTS %s" % table)
	cursor.execute(sql)

if __name__ == '__main__':
	table = 'SERVICE'
	sql = """CREATE TABLE %s (
                 RATE FLOAT,
                 NOW_TIME DATETIME)""" % table
	init_database(sql, table)
	#'inf'
	table = settings.table
        sql = """CREATE TABLE %s (
                NOW_TIME DATETIME,
                TCP FLOAT,
                WIDTH FLOAT,
                DROP_RATE FLOAT,
                MEMORY FLOAT,
                CPU FLOAT,
                SERVICE INT,
                THREAD_NUM INT,
                ATTACK_NUM INT,
                DATA_SIZE INT,
                FRECURENT FLOAT)""" % table
	init_database(sql, table)
	db.close()

	queues = ["MEMORY", "CPU", "WIDTH", "TCP", "DROP_RATE"]
	for queue in queues:
		r.delete(queue)




