import MySQLdb
import settings
import redis
import socket
import fcntl
import struct
import datetime
import sys

db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
cursor = db.cursor()

thread_num = int(sys.argv[1])
attack_num = int(sys.argv[2])
data_size = int(sys.argv[3])
frecurent = float(sys.argv[4])

def get_rate(service, table):
	db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
        cursor = db.cursor()
	sql = "select count(*) from %s where SERVICE > '%f'" % (table, service)
	try:
		cursor.execute(sql)
                result = cursor.fetchone()[0]
	except:
		print "service > %f values not exist" % (service)
	return result

def insert_result():
	db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
	cursor = db.cursor()
	names = ['TCP','CPU','MEMORY','WIDTH', 'SERVICE']
	length = len(names)
	results = [0, 0.0, 0.0, 0.0, 0]
	for i in range(length):
		sql = "select avg(%s) from inf" % (names[i])
	
		try:
			cursor.execute(sql)
			results[i] = cursor.fetchone()[0]
#			print type(results[i])			
		except:
			print "Error: unable to fetch data"
	#sql = "SELECT max(rate) from SERVICE"
	#cursor.execute(sql)
	#max_service = cursor.fetchone()[0]
	sql = "SELECT max(DROP_RATE) from inf"
        cursor.execute(sql)
        max_drop_rate = cursor.fetchone()[0]

	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	services = [100, 200, 300, 400, 500]
	rate = [0.0, 0.0, 0.0, 0.0, 0.0]
	length = len(services)
	for i in range(length):
		try:
			small = get_rate(services[i], 'inf')
			big = get_rate(0, 'inf')
			rate[i] = small/(big*1.0)
		except:
			print "compute service rate error", small, big
	
	sql = "INSERT INTO result (NOW_TIME, TCP, WIDTH, DROP_RATE, MEMORY, CPU, SERVICE, THREAD_NUM, ATTACK_NUM, DATA_SIZE, FRECURENT, R100, R200, R300, R400, R500) VALUES('%s', '%f', '%f', '%f', '%f', '%f', '%f', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f', '%f')" % (now, results[0], results[3], max_drop_rate, results[2], results[1], results[4], thread_num, attack_num, data_size, frecurent, rate[0], rate[1], rate[2], rate[3], rate[4])
	cursor.execute(sql)
	db.commit()
	db.close()
if __name__ == '__main__':
	#init_database()
	insert_result()
	print "cp avg inf to result success"




