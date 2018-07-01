import MySQLdb
import settings
import redis
import socket
import fcntl
import struct
import datetime


db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
cursor = db.cursor()
def connect_mysql():
	try:    
                db.ping()
        except:         
                db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)

def init_database(table, sql):
	cursor.execute("DROP TABLE IF EXISTS %s" % table)
        cursor.execute(sql)
	print "init %s successful" % table

def insert_data(sql):
        connect_mysql()
	try:
                cursor = db.cursor()
                cursor.execute(sql)
                db.commit()
        except:
                print "execute %s error" % sql
                db.rollback()


def set_tags_from_result():
	sql = "select WIDTH,DROP_RATE,MEMORY,CPU,SERVICE,THREAD_NUM,FRECURENT,R100 from result"
	devide = [125.0, 1, 100.0, 100.0, 1000.0, 20.0, 1, 1]
	result = [1,2,3,4,5,6,7,8]
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for element in results:
			for i in range(len(element)):
				result[i] = element[i]/devide[i]
			sql = "insert into tags (WIDTH,DROP_RATE,MEMORY,CPU,SERVICE,THREAD_NUM,FRECURENT,R100) values('%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f')" % (result[0], result[1], result[2],result[3], result[4], result[5], result[6], result[7])
			insert_data(sql)
	except Exception as msg:
        	print "select from result error"
	        print msg
                print str(msg)
	db.close()
if __name__ == '__main__':
	table = 'tags'
	sql = """CREATE TABLE %s (
                WIDTH FLOAT(3,2),
                DROP_RATE FLOAT,
                MEMORY FLOAT(3,2),
                CPU FLOAT(3,2),
                SERVICE FLOAT(3,2),
                THREAD_NUM FLOAT,
                FRECURENT FLOAT,
                R100 FLOAT(2, 1))""" % table
	init_database(table, sql)
	set_tags_from_result()
	
	
