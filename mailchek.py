import re
email = raw_input("Enter Your email: ")
checker =re.search(r'(.*)@(.*?).com.*',str(email),re.M|re.I)

if  not checker :
	print email,'is not an email'
	
else:
	print 'Email Good! ',checker.group()