import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import MySQLdb
import settings

db = MySQLdb.connect(settings.host, settings.user, settings.pwd, settings.db)
cursor = db.cursor()

tables = settings.tables
ylabels = ["Rate(%)", "Rate(%)", "Flow(MB)", "Numbers", "Ser-Time(ms)"]
number = 0
for i in range(0, len(tables)):
	number = number + 1
	sql = "SELECT * FROM %s" % tables[i]
	y = []
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			y.append(row[0])
	except:
		print "Error: unable to fetch data"

	
	'''
	x_value = 0.001;
	try:
		space = x_value/(len(y)*1.0)
	except:
		print 'Error devide!'
	x = np.arange(0, x_value, space)
	'''

	x = range(len(y))
	plt.figure(number)
	plt.plot(x, y)

	plt.ylabel(ylabels[i])
	plt.xlabel('Time(S)')
	plt.title(tables[i])
	plt.show()
db.close()
