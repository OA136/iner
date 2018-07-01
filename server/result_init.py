import MySQLdb
import settings
import redis
import socket
import fcntl
import struct
import datetime


db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
cursor = db.cursor()

def init_database(table, sql):
	cursor.execute("DROP TABLE IF EXISTS %s" % table)
        cursor.execute(sql)
	print "init %s successful" % table

if __name__ == '__main__':
	table = 'result'
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
                FRECURENT FLOAT,
                R100 FLOAT,
                R200 FLOAT,
                R300 FLOAT,
                R400 FLOAT,
                R500 FLOAT)""" % table
	init_database(table, sql)

	table = 'original'
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
	init_databesa(table, sql)
	db.close()
	

