from PyQt4 import QtSql
import os
import csv

db =QtSql.QSqlDatabase.addDatabase("QMYSQL")
db.setHostName("localhost")
db.setDatabaseName("fraud_detect")
db.setUserName("root")
db.setPassword("")
ok = db.open()
if ok==True:
	print "Connection nice"

	query =QtSql.QSqlQuery()
	query.exec_("SELECT * FROM employeeExpense")

	print "Username\tPassword"
	while (query.next()):
		date = query.value(1).toString()
		file =query.value(2).toString()
		descript = query.value(3).toString()
		empname =query.value(5).toString()

		print date+"\t"+file+"\t"+descript+"\t"+empname
	with open(file,"rb") as fileIn:
		for data in csv.reader(fileIn):
			print data
	head,tail =os.path.split(str(file))
	myrealfile =tail
	print myrealfile
	query.exec_("DELETE FROM employeeExpense WHERE expenseId =15")

else:
	print "Should not create a connection first!"
	os.system("service mysql start")
