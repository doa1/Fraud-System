import re
inp ="he-mee"

if (re.match(r'[a-zA-Z0-9]{2}-[a-zA-Z0-9]{3}$',inp)):
	print "goood"

else:
	print "bad"

regNo ="BIT/022/13000"
if  (re.match(r'[a-zA-Z0-9]{3}/[0-9]{3}/[0-9]{2}',regNo)):
	print "Reg gud"