import MySQLdb
admin ="Auditor"
conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="fraud_detect")
cursor =conn.cursor()
try:
	cursor.execute("SELECT email From admin WHERE UserRole ='Auditor'" )

	res =cursor.fetchall()
	print str(res).strip("(),")
	if  res :
		print "1hell"
		print str(res).strip("(),'")

except Exception as e:
	print e


