import MySQLdb
import settings
import init
#import result
import sys
#import dealwith_inf

r = init.r
table = settings.table

db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
thread_num = int(sys.argv[3])
attack_num = int(sys.argv[4])
data_size = int(sys.argv[5])
frecurent = float(sys.argv[6])

def insert_data(sql):
	try:
		db.ping()
	except:
		db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
	try:
		cursor = db.cursor()
		cursor.execute(sql)
		db.commit()
	except:
		print "rollback"
		db.rollback()


if __name__ == '__main__':
	queues = ["MEMORY", "CPU", "WIDTH", "TCP", "DROP_RATE"]
	while (r.llen("DROP_RATE") > 0 and r.llen("MEMORY") > 0 and r.llen("CPU") > 0 and r.llen("WIDTH") > 0 and r.llen("TCP") > 0 ):
		element = {}
		for queue in queues:
			value = r.rpop(queue)
			value = eval(value)
			element[queue] = value.get(queue)
			element['time'] = value.get('time')
		sql = "INSERT INTO %s(THREAD_NUM, ATTACK_NUM, NOW_TIME, TCP, WIDTH, DROP_RATE, MEMORY, CPU, DATA_SIZE, FRECURENT) VALUES('%d', '%d','%s', '%d', '%f', '%f', '%f', '%f', '%d', '%f')" % (table, thread_num, attack_num, element.get('time'), element.get('TCP'), element.get('WIDTH'), element.get('DROP_RATE'), element.get('MEMORY'), element.get('CPU'), data_size, frecurent)
		insert_data(sql)
	for queue in queues:
		r.delete(queue)
