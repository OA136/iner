import MySQLdb
import settings
import datetime

db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
cursor = db.cursor()

def update_service():
	sql = "SELECT * FROM %s" % "SERVICE"
	try:
		cursor.execute(sql)
       		results = cursor.fetchall()
        	for row in results:
			sql = "UPDATE %s SET SERVICE=%d WHERE NOW_TIME='%s'" % ("inf", row[0], row[1])
			print row[1].strftime("%Y-%m-%d %H:%M:%S"), (row[1]-datetime.timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
			try:
				cursor.execute(sql)
			except:
				print "update error"
		db.commit()
	except:
		print "Error: unable to fetch data"
	#db.close()
def next_second(now_time):
	return (now_time+datetime.timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")

def last_second(now_time):
	return (now_time-datetime.timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")

def update_service_isnull():
	sql = "SELECT NOW_TIME FROM inf WHERE SERVICE is NULL"
	cursor.execute(sql)
	results = cursor.fetchall()
	for now_time in results:
		next_second = next_second(now_time)
		sql = "SELECT SERVICE WHERE NOW_TIME=%s" % (next_second)
		try:
			cursor.execute(sql)
			next_service_time = cursor.fetchone()[0]
			sql = "UPDATE inf SET SERVICE=%d WHERE NOW_TIME=%s" % (next_service_time, now_time)
			try:
				cursor.execute(sql)
			except:
				print "update now_service use next_second_service failed"
		except:
			last_second = next_second(now_time)
			sql = "SELECT SERVICE WHERE NOW_TIME=%s" % (last_second)
			try:
				cursor.execute(sql)
	                        last_service_time = cursor.fetchone()[0]
        	                sql = "UPDATE inf SET SERVICE=%d WHERE NOW_TIME=%s" % (last_service_time, now_time)
                	        try:
                        	        cursor.execute(sql)
                       		except:
                                	print "update now_service use last_second_service failed"

if __name__ == '__main__':
#	update_service()
	update_service_isnull()
	db.commit()
	db.close()
