import MySQLdb
import settings
import redis_init

r = redis_init.r
tables = settings.tables
queues = settings.queues

db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)


def insert_data(table, date, rate):
	sql = "INSERT INTO %s (NOW_TIME, RATE) VALUES('%s', '%f')" % (table, date, rate)
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

length = len(queues)
for i in range(length):
	while (r.llen(queues[i]) > 0):
		element = r.rpop(queues[i])
		element = eval(element)
		#print element.get('time'), element.get('rate')
		insert_data(tables[i], element.get('time'), element.get('rate'))


