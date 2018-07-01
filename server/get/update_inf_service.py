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
#			print row[1].strftime("%Y-%m-%d %H:%M:%S"), (row[1]-datetime.timedelta(seconds=1)).strftime("%Y-%m-%d %H:%M:%S")
			try:
				cursor.execute(sql)
			except:
				print "update error"
		db.commit()
	except:
		print "Error: unable to fetch data"
	#db.close()
def next_second(now_time, space):
	return now_time + datetime.timedelta(seconds=space)

def last_second(now_time, space):
	return now_time - datetime.timedelta(seconds=space)

def update_service_isnull():
	sql = "SELECT NOW_TIME FROM inf WHERE SERVICE is NULL"
	cursor.execute(sql)
	results = cursor.fetchall()
	for now_time in results:
		now_time = now_time[0]
#		print "now:",now_time.strftime("%Y-%m-%d %H:%M:%S")
		space = 1
		flags = 0
		while (space < 10 and flags == 0):
			next_seconds = next_second(now_time, space)
#			print "next:",next_seconds.strftime("%Y-%m-%d %H:%M:%S")
			sql = "SELECT SERVICE FROM inf WHERE NOW_TIME='%s'" % (next_seconds)
			try:
				cursor.execute(sql)
				next_service_time = cursor.fetchone()[0]
#				print "next_service_time:", next_service_time
				sql = "UPDATE inf SET SERVICE=%d WHERE NOW_TIME='%s'" % (next_service_time, now_time)
				try:
					cursor.execute(sql)
					flags = 1
				except:
					print "update now_service use next_second_service failed"
			except:
				print "the next_second record is not exsit"
				last_seconds = last_second(now_time, space)
#				print "last:", last_seconds.strftime("%Y-%m-%d %H:%M:%S")
				sql = "SELECT SERVICE FROM inf WHERE NOW_TIME='%s'" % (last_seconds)
				try:
					cursor.execute(sql)
	                        	last_service_time = cursor.fetchone()[0]
#					print "last_service_time:",last_service_time
        	                	sql = "UPDATE inf SET SERVICE=%d WHERE NOW_TIME='%s'" % (last_service_time, now_time)
                	        	try:
                        		        cursor.execute(sql)
						flags = 1
                       			except:
                                		print "update now_service use last_second_service failed"
				except:
					print "the last_second record is not exsit"
			db.commit()
			space = space + 1
def delete_service_isnull():
	sql = "DELETE FROM inf WHERE SERVICE is NULL"
        try:
		cursor.execute(sql)
		db.commit()
	except:
		print "delete service null is error"

if __name__ == '__main__':
	update_service()
#	delete_service_isnull()
#	update_service_isnull()
#	db.commit()
	db.close()
