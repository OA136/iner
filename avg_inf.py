import MySQLdb
import settings
import redis
import socket
import fcntl
import struct
import datetime


db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
cursor = db.cursor()

thread_num = int(sys.argv[1])
attack_num = int(sys.argv[2])
data_size = int(sys.argv[3])
frecurent = float(sys.argv[4])


def init_database():
	cursor.execute("DROP TABLE IF EXISTS %s" % 'result')
	sql = """CREATE TABLE %s (
		NOW_TIME DATETIME,
		TCP INT,
		WIDTH FLOAT,
		DROP_RATE FLOAT,
		MEMORY FLOAT,
		CPU FLOAT,
		SERVICE INT,
		THREAD_NUM INT,
        ATTACK_NUM INT,
        DATA_SIZE INT,
        FRECURENT FLOAT)""" % 'result'
	cursor.execute(sql)
	db.close()
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
	sql = "INSERT INTO result (NOW_TIME, TCP, WIDTH, DROP_RATE, MEMORY, CPU, SERVICE, THREAD_NUM, ATTACK_NUM, DATA_SIZE, FRECURENT) VALUES('%s', '%f', '%f', '%f', '%f', '%f', '%f', '%d', '%d', '%d', '%f')" % (now, results[0], results[3], max_drop_rate, results[2], results[1], results[4], thread_num, attack_num, data_size, frecurent)
	cursor.execute(sql)
	db.commit()
	db.close()
if __name__ == '__main__':
	init_database()
	insert_result()




