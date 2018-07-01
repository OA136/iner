import MySQLdb
import settings
import init
import result
import sys

r = init.r
db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)

def deal_data(start):
#	db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
	try:
		db.ping()
	except:
		db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
	sql = "SELECT NOW_TIME FROM inf limit %d,%d" % (start, 1)
	try:
		print start
		cursor = db.cursor()
		cursor.execute(sql)
		result = cursor.fetchone()[0]
		#return result
	except Exception as msg:
		print "deal_data"
		print str(msg)
#	print result
	return result

def delete_inf(start_time, end_time):
	sql = "DELETE FROM inf WHERE NOW_TIME < '%s' or NOW_TIME > '%s'" % (start_time, end_time)
	try:
		cursor = db.cursor()
		cursor.execute(sql)
		db.commit()
        except Exception as msg:
                print msg
                print str(msg)
def update_inf_attack_num(start_time, end_time):
	sql = "update inf set THREAD_NUM=%d, ATTACK_NUM=%d,DATA_SIZE=%d where NOW_TIME < '%s' or NOW_TIME > '%s'" % (0, 0, 0, start_time, end_time)
	try:
		cursor = db.cursor()
		cursor.execute(sql)
		db.commit()
	except Exception as msg:
		print msg
		print str(msg)
def get_count_of_inf():
	db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
	cursor = db.cursor()
	sql = "select count(*) from inf"
	result = 0
	try:
			cursor.execute(sql)
			result = cursor.fetchone()[0]
	except:
			print "count inf error"
	return result


def delete_service_isnull():
	sql = "DELETE FROM inf WHERE SERVICE is NULL"
        try:
		cursor = db.cursor()
		cursor.execute(sql)
		db.commit()
	except Exception as msg:
                print msg
                print str(msg)

def cp_inf_into_original(table):
        try:
                db.ping()
        except:
                db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)

        sql = "insert into %s select * from inf" % (table)
	try:
                cursor = db.cursor()
                cursor.execute(sql)
                db.commit()
		print "cp inf to %s successful" % (table)
        except Exception as msg:
                print msg
                print str(msg)

if __name__ == '__main__':
	if (len(sys.argv) == 3):
		start = int(sys.argv[1])
		end = get_count_of_inf() - 11
		start_time = deal_data(start)
		end_time = deal_data(end)
		#delete other data
		delete_inf(start_time, end_time)
		#update_inf_attack_num(start_time, end_time)
		delete_service_isnull()
		cp_inf_into_original('original')
		db.close()
	if (len(sys.argv) == 1):
		cp_inf_into_result()
