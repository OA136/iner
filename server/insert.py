import MySQLdb
import settings
import init
#import result
import sys
#import dealwith_inf

r = init.r
queue = settings.queue
table = settings.table

db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
thread_num = int(sys.argv[3])
attack_num = int(sys.argv[4])
data_size = int(sys.argv[5])
frecurent = float(sys.argv[6])

def insert_data(table, element):

	sql = "INSERT INTO %s(THREAD_NUM, ATTACK_NUM, NOW_TIME, TCP, WIDTH, DROP_RATE, MEMORY, CPU, DATA_SIZE, FRECURENT) VALUES('%d', '%d','%s', '%d', '%f', '%f', '%f', '%f', '%d', '%f')" % (table, thread_num, attack_num, element.get('time'), element.get('TCP'), element.get('WIDTH'), element.get('DROP_RATE'), element.get('MEMORY'), element.get('CPU'), data_size, frecurent)
	#print table, date, rate
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

	db.close()


while (r.llen(queue) > 0):
	element = r.rpop(queue)
	element = eval(element)
	#print element.get('time'), element.get('rate')
	insert_data(table, element)

#start = int(sys.argv[1])
#length = int(sys.argv[2])
#result.insert_result(start, length)
