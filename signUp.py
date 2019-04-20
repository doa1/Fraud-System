import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

_fromUtf8= QString.fromUtf8 
class RegisterUser(QWidget):
	"""docstring for RegisterUser"""
	def __init__(self, parent=None):
		#super(RegisterUser, self).__init__(parent)
		QWidget.__init__(self,parent)
		
		self.setStyleSheet(_fromUtf8("background:rgb(172, 183, 255)"))
		#self.setGeometry(200,150,680,450)
		layout = QHBoxLayout()
		self.fbox =QFormLayout()

		self.user_Icon=QLabel()
		self.user_Icon.setPixmap(QPixmap("1.jpg"))
		layout.addWidget(self.user_Icon)

		self.emp_nameLabel=QLabel("Enter Employee Name: ")
		self.emp_nameLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \"Century Schoolbook L\";"))
		self.emp_nameField =QLineEdit()
		self.emp_nameField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))

		self.fbox.addRow(self.emp_nameLabel,self.emp_nameField)

		self.emp_IdLabel = QLabel("Enter Employee Id (Reg/No):")
		self.emp_IdLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \"Century Schoolbook L\";"))
		self.emp_IdField =QLineEdit()
		self.emp_IdField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))
		self.fbox.addRow(self.emp_IdLabel,self.emp_IdField)


		self.emp_EmailLabel =QLabel("Enter Your Email Address: ")
		self.emp_EmailLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \"Century Schoolbook L\";"))
		self.emp_EmailField =QLineEdit()
		self.emp_EmailField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))

		self.fbox.addRow(self.emp_EmailLabel,self.emp_EmailField)

		self.passLabel =QLabel("Enter Your Password: ")
		self.passLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \"Century Schoolbook L\";"))
		self.passField =QLineEdit()
		self.passField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))
		self.passField.setEchoMode(QLineEdit.Password)
		self.fbox.addRow(self.passLabel,self.passField)

		self.passConfLabel =QLabel("Enter Password Confirm: ")
		self.passConfLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \"Century Schoolbook L\";"))
		self.passConfField =QLineEdit()
		self.passConfField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))
		self.passConfField.setEchoMode(QLineEdit.Password)
		self.fbox.addRow(self.passConfLabel,self.passConfField)

		self.btns=QHBoxLayout()

		self.signupBtn =QPushButton("Register!")
		self.signupBtn.setStyleSheet(_fromUtf8("background:rgb(220, 231, 255);\n"
"font: 75 16pt \"Century Schoolbook L\";"))
		self.signupBtn.clicked.connect(self.Register)

		self.resetBtn =QPushButton("Reset!")
		
		self.resetBtn.setStyleSheet(_fromUtf8("background:rgb(220, 231, 255);\n"
"font: 75 13pt \"Century Schoolbook L\";"))
		self.resetBtn.clicked.connect(self.Reset)
		self.fbox.addRow(self.resetBtn,self.signupBtn)

		layout.addStretch()

		layout.addLayout(self.fbox)

		self.setWindowTitle("User Signup !")

		self.setLayout(layout)
		#self.resize(500,400)
		self.error =QMessageBox()
		self.error.setIcon(QMessageBox.Critical)
		self.warning =QMessageBox()
		self.warning.setIcon(QMessageBox.Warning)
		self.info =QMessageBox()
		self.info.setIcon(QMessageBox.Information)
	def Reset(self):
		self.emp_nameField.setText("")
		self.emp_EmailField.setText("")
		self.passField.setText("")
		self.emp_IdField.setText("")
		self.passConfField.setText("")
	def Register(self):
		import re
		userId =self.emp_IdField.text()
		username =self.emp_nameField.text()
		email =self.emp_EmailField.text()
		password =self.passField.text()
		passconf =self.passConfField.text()

		#email validation
		
		
		checker =re.search(r'(.*)@(.*?).com.*',str(email),re.M|re.I)
		commonpass=['admin123','admintest','admintest123','sysadmin123','password',username,'adminpass','systempass','qwerty123','password123']

		#check if all fields are field
		if (len(str(username)) <1):
			self.emp_nameField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.warning.setWindowTitle("Sign Up Error!")

			self.warning.setText("Employee Name is required!")
			self.warning.setDetailedText("Hint:Your FirstName,(optionally midl ename),and lastname or the reverse order")
			self.warning.exec_()
			self.emp_nameField.setStyleSheet('QLineEdit {background-color:#fff}')

		elif (len(str(username)) <10):
			self.emp_nameField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.warning.setWindowTitle("Sign Up Error!")

			self.warning.setText("Employee Name is too Short")
			self.warning.setDetailedText("Hint:Your Employee name should have a minimum of 10 characters!\nLike 'Ochieng Doa'")
			self.warning.exec_()
			self.emp_nameField.setStyleSheet('QLineEdit {background-color:#fff}')

		elif str(username).title() == 'Ochieng Doa' or str(username).title()=='Doa Ochieng':
			self.emp_nameField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.warning.setWindowTitle("Sign Up Error!")

			self.warning.setText("Employee Name cannot be used!")
			self.warning.setDetailedText("Please ensure you use only the name in your National Id or the Academic Credentials")
			self.warning.exec_()
			self.emp_nameField.setStyleSheet('QLineEdit {background-color:#fff}')
		elif (len(str(userId)) < 1):
			self.emp_IdField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.warning.setWindowTitle("Sign Up Error!")
			self.warning.setText("Employee ID is required!")
			self.warning.setDetailedText("Hint: Your Employee Registration Number(always unique to you) is the Employee ID")
			self.warning.exec_()
			self.emp_IdField.setStyleSheet('QLineEdit {background-color:#fff}')

		elif(len(str(email)) <1):
			self.emp_EmailField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.warning.setWindowTitle("Sign Up Error!")
			self.warning.setText("User Email is required!")
			self.warning.setDetailedText("Hint: Email Address is similar to this:\nOchiengDoa@gmail.com")
			self.warning.exec_()
			self.emp_EmailField.setStyleSheet('QLineEdit {background-color:#fff}')

		elif email =='OchiengDoa@gmail.com' or email =='ochiengdoa@gmail.com' or email =='doaochieng@gmail.com':
			self.emp_EmailField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.warning.setWindowTitle("Sign Up Error")
			self.warning.setText("You cannot use this email!")
			self.warning.setDetailedText("This email is for demonstration only!\nPlease enter the email provided by your service provider")
			self.warning.exec_()
			self.emp_EmailField.setStyleSheet('QLineEdit {background-color:#fff}')

		elif  not checker :
			self.emp_EmailField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.error.setWindowTitle("Sign Up Error")
			self.error.setText("Wrong Email Address Format!")
			self.error.setDetailedText("Email Address must of the correct format!\nHint: Email Address is similar to this:\n'OchiengDoa@gmail.com' or 'ochiengdoa@gmail.com'")
			self.error.exec_()
			self.emp_EmailField.setStyleSheet('QLineEdit {background-color:#fff}')

		elif(len(str(password)) < 1):
			self.passField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.warning.setWindowTitle("Sign Up Error!")
			self.warning.setText("User password is required!")
			self.warning.setDetailedText("Hint: Your Password is the Secret code you will use during login")
			self.warning.exec_()
			self.passField.setStyleSheet('QLineEdit {background-color:#fff}')

		elif(len(str(passconf))< 1):
			self.passConfField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.warning.setWindowTitle("Sign Up Error!")
			self.warning.setText("Enter Password Confirmation!")
			self.warning.setDetailedText("You must reenter the above password as a confirmation!")
			self.warning.exec_()
			self.passConfField.setStyleSheet('QLineEdit {background-color:#fff}')

		elif(len(str(password)) < 8 or len(str(passconf)) <8):
			self.passField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.warning.setWindowTitle("Sign Up Error!")
			self.warning.setText("Password length must be atleast 8 characters!")
			self.warning.setDetailedText("For security reason,your password must be at least 8 characters long\nPassword must also contain atleast a number and special character")
			self.warning.exec_()
		elif password in commonpass:
			self.passField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.error.setWindowTitle("User Sign Up Error")
			self.error.setText("The password Entered too weak")
			self.error.setDetailedText("For your account security,you need to use a stronger password which is not too easy to guess")
			self.error.exec_()
			self.passField.setStyleSheet('QLineEdit {background-color:#fff}')

		elif password != passconf:
			self.passField.setStyleSheet('QLineEdit {background-color:#f6989d}')
			self.error.setWindowTitle("User Sign Up Error")
			self.error.setText("The  Password entered and password confirmation Must Match!")
			self.error.setDetailedText("Ensure the password entered and the password confirmation is the same!")
			self.error.exec_()
			self.passField.setStyleSheet('QLineEdit {background-color:#f}')

			#when validation done,connect to the dbs and add the user

		else:
			import MySQLdb
			import time
			#get the current localtime
			localtime =time.asctime(time.localtime(time.time()))

			#hash the user password with md5
			import md5
			hashpass =md5.new(str(password).strip()).hexdigest()

			conn= MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="fraud_detect")

			cursor =conn.cursor()

			query = "SELECT Employee_ID FROM users "

			#execute the query to check if the employee id entered already exit
			try:
				cursor.execute(query)
				results =cursor.fetchall()
				for row in results:
					dbuserId =row[0]

					if userId == dbuserId:
						self.error.setWindowTitle("User Database Error")
						self.error.setText("That Employee Id is already in use!")
						self.error.setDetailedText("Please ensure you enter your unique employee id\nIf you think this is a system error,please contact the admin!")
						self.error.exec_()
						break;

					else:
						insertQuery="INSERT INTO users(Employee_ID,UserName,UserEmail,UserPass,regDate) VALUES('%s','%s','%s','%s',NOW())"\
						%(userId,username,email,hashpass)
						try:
							#execute the query
							cursor.execute(insertQuery)
							#if things good,apply the changes
							conn.commit()

							#return success message
							self.info.setWindowTitle("Success Message!")
							self.info.setText("User Was Successfully Added!")
							self.info.setDetailedText("Please note these details since you will repeatedly need them in any account transations")
							self.info.exec_()
							break
						except Exception as e:
							#undo the changes
							conn.rollback()
							self.warning.setWindowTitle("User Database Error")
							self.warning.setText("Oops!\nCould not add the user!")
							self.warning.setDetailedText("Something just went wrong while adding the user details\nBe Patient while we fix this!")
							self.warning.exec_()
							
			except Exception,e:
				self.warning.setWindowTitle("User Database Error")
				self.warning.setText("Oops!\nAn Error Occured!")
				self.warning.setDetailedText("Hey!\nLooks Like Our Server is Currently Down!\nBe Patient while we fix this!")
				self.warning.exec_()


def main():
	app =QApplication(sys.argv)
	win =RegisterUser()
	win.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()