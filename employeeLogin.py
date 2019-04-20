
from PyQt4 import QtCore, QtGui
import sys
import os
import md5
from employeeDataView import Ui_MainWindow
try:
	#from signUp import RegisterUser
	from employeeHome import Ui_Form
	from employeeRegister import Reg_MainWindow

except Exception as e:
	print e

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class login_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(669, 353)
        MainWindow.setStyleSheet(_fromUtf8("background:rgb(134, 134, 255);\n"
"font: 75 12pt \"Century Schoolbook L\";"))
        self.signupBtn= QtGui.QPushButton(MainWindow)
        self.signupBtn.setGeometry(QtCore.QRect(390, 250, 93, 30))
        self.signupBtn.setStyleSheet(_fromUtf8("background:rgb(228, 248, 255);\n"
"color:rgb(0, 0, 86);\n"
"font: 14pt \"Latin Modern Math\";"))
        self.signupBtn.setObjectName(_fromUtf8("signupBtn"))

        self.signupBtn.clicked.connect(self.exitGui)

        self.loginBtn= QtGui.QPushButton(MainWindow)
        self.loginBtn.setGeometry(QtCore.QRect(570, 250, 93, 30))
        self.loginBtn.setStyleSheet(_fromUtf8("background:rgb(228, 248, 255);\n"
"color:rgb(0, 0, 86);\n"
"font: 14pt \"Latin Modern Math\";"))
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        #set signals n slots
        self.loginBtn.clicked.connect(self.LoginNow)


        self.UserNlabel = QtGui.QLabel(MainWindow)
        self.UserNlabel.setGeometry(QtCore.QRect(280, 80, 131, 31))
        self.UserNlabel.setStyleSheet(_fromUtf8("color:rgb(199, 245, 255);\n"
"font: 14pt \"Droid Serif\";"))
        self.UserNlabel.setObjectName(_fromUtf8("UserNlabel"))
        self.Passslabel = QtGui.QLabel(MainWindow)
        self.Passslabel.setGeometry(QtCore.QRect(280, 160, 191, 20))
        self.Passslabel.setStyleSheet(_fromUtf8("color:rgb(199, 245, 255);\n"
"font: 14pt \"Droid Serif\";"))
        self.Passslabel.setObjectName(_fromUtf8("Passslabel"))
        self.usernField = QtGui.QLineEdit(MainWindow)
        self.usernField.setGeometry(QtCore.QRect(480, 80, 181, 32))
        self.usernField.setStyleSheet(_fromUtf8("background:rgb(228, 248, 255)"))
        self.usernField.setObjectName(_fromUtf8("usernField"))
        self.passField = QtGui.QLineEdit(MainWindow)
        self.passField.setGeometry(QtCore.QRect(480, 150, 181, 32))
        self.passField.setStyleSheet(_fromUtf8("background:rgb(228, 248, 255)"))
        self.passField.setObjectName(_fromUtf8("passField"))
        self.passField.setEchoMode(QtGui.QLineEdit.Password)


        self.image = QtGui.QLabel(MainWindow)
        self.image.setGeometry(QtCore.QRect(30, 50, 251, 181))
        self.image.setObjectName(_fromUtf8("image"))
        #set message alert objects
        self.error=QtGui.QMessageBox()
        self.error.setIcon(QtGui.QMessageBox.Critical)

        self.warning =QtGui.QMessageBox()
        self.warning.setIcon(QtGui.QMessageBox.Warning)

        self.info =QtGui.QMessageBox()
        self.info.setIcon(QtGui.QMessageBox.Information)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee Login", None))
        self.loginBtn.setText(_translate("MainWindow", "Login", None))
        self.signupBtn.setText(_translate("MainWindow", "Cancel", None))
        #self.HomeBtn.setText(_translate("MainWindow", "Back", None))
        self.UserNlabel.setText(_translate("MainWindow", "Employee ID: ", None))
        self.Passslabel.setText(_translate("MainWindow", "Employee Password: ", None))
        self.image.setPixmap(QtGui.QPixmap("lock.png"))

    def exitGui(self):
    	#call the signup window
    	self.homWindow =QtGui.QMainWindow()
    	self.ui=Ui_Form()
    	self.ui.setupUi(self.homWindow)
    	self.homWindow.show()
    	MainWindow.close()

    def LoginNow(self):
    	name =self.usernField.text()
    	password=self.passField.text()
        hashedPassword = md5.new(str(password).strip()).hexdigest()

    	if len(name )<1:
    		self.usernField.setStyleSheet('QLineEdit {background-color:red}')
    		self.warning.setWindowTitle("Login Error!")
    		self.warning.setText("Username is required!")
    		self.warning.setDetailedText("You must be enter username( your employee id) in order to proceed! ")
    		self.warning.exec_()
    		self.usernField.setStyleSheet('QLineEdit {background-color:#fff}')
    		
    	elif len(password) <1:
    		self.passField.setStyleSheet('QLineEdit {background-color:red}')
    		self.warning.setWindowTitle("Login Error!")
    		self.warning.setText("Password is required!")
    		self.warning.setDetailedText("You must enter your account password in order to proceed")
    		self.warning.exec_()
    		self.passField.setStyleSheet('QLineEdit {background-color:#fff}')

    	else:
    		#connect to dbs and authenticate the user
    		import MySQLdb
    		
    		try:
    			db =MySQLdb.connect("localhost","root","","fraud_detect")
    		except:
    			self.error.setWindowTitle("Server Error")
    			self.error.setText("Connection to the server failed!")
    			self.error.setDetailedText("You are seeing this error because your server is not running!\nPlease ensure the mysql database server is started before you continue.")

    			self.error.exec_()

    			self.info.setWindowTitle("Server Starting")
    			self.info.setText("We'll start the server for you!")
    			self.info.setDetailedText('Be patient please')
    			self.info.exec_()

    			os.system("service mysql start")
    		else:
    			#prepare the cursor
    			cursor=db.cursor()
    			query ='SELECT * FROM users'
    			#execute the query
                try:
                    cursor.execute(query)
                    results =cursor.fetchall()
                    names =[]
                    passwords =[]

                    for row in results:
                        dbnames=row[1]
                        dbpass =row[4]
                        names.append(dbnames)
                        passwords.append(dbpass)

                    if name not in names:
                        self.usernField.setStyleSheet('QLineEdit {background-color:red}')
                        self.passField.setStyleSheet('QLineEdit {background-color:red}')
                        self.error.setWindowTitle("User Login Error")
                        self.error.setText("The Username does not exist")
                        self.error.setDetailedText("Looks like you are trying to access the system with a user details are not in the system.\nPlease click the Signup Button to register!")
                        self.error.exec_()
                        self.usernField.setStyleSheet('QLineEdit {background-color:white}')
                        self.passField.setStyleSheet('QLineEdit {background-color:#fff}')
                        self.usernField.setText("")
                        self.passField.setText("")
           
                    elif hashedPassword not in passwords:
                        self.passField.setStyleSheet('QLineEdit {background-color:red}')
                        self.error.setWindowTitle("User Login Error")
                        self.error.setText("Incorrect Password!\nPlease Try again.")
                        self.error.setDetailedText("The password Entered did not match the.\nClick Forgot Password button if you want to recover your password!")
                        self.error.exec_()
                        self.passField.setStyleSheet('QLineEdit {background-color:#fff}')
                        self.passField.setText("")
                        
                        
                    else:
                        try:
                            cursor.execute("UPDATE users SET login_status=1 WHERE Employee_ID='%s'" %name)

                            db.commit()

                            self.info.setWindowTitle("Login Success!")
                            self.info.setText("You have successfully been logged in!")
                            self.info.setDetailedText("Wait for a few minutes as you are being redirected!")
                            self.info.exec_()

                            #redirect the user to the main window"""
                            try:
                                self.MainWindow =QtGui.QMainWindow()
                                self.ui =Ui_MainWindow()
                                self.ui.setupUi(self.MainWindow)
                                self.MainWindow.show()
                                MainWindow.close()
                        
                            except Exception as e:
                                print e
                            
                        except Exception as e:
                            print  e
                            db.rollback()
                        
                            
                except:    				
    				self.warning.setWindowTitle("Server Error!")
		    		self.warning.setText("Error While Reading from the server")
		    		self.warning.setDetailedText("Oops! Looks like our server is having issues\nPlease be retry again later after a few minutes(10 minutes)\nContact us if the problem persists!")
		    		self.warning.exec_()

		    		




if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = login_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

