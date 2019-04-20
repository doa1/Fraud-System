#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Ochieng Doa
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
import re
try:
    _fromUtf8 = QtCore.QString.fromUtf8
    from employeeLogin import Ui_Dialog
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

class Reg_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(_fromUtf8("background:rgb(172, 183, 255)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.emp_nameLabel = QtGui.QLabel(self.centralwidget)
        self.emp_nameLabel.setGeometry(QtCore.QRect(230, 90, 271, 20))
        self.emp_nameLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \\\"Century Schoolbook L\\\";"))
        self.emp_nameLabel.setObjectName(_fromUtf8("emp_nameLabel"))
        self.emp_IdLabel = QtGui.QLabel(self.centralwidget)
        self.emp_IdLabel.setGeometry(QtCore.QRect(230, 150, 271, 20))
        self.emp_IdLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \\\"Century Schoolbook L\\\";"))
        self.emp_IdLabel.setObjectName(_fromUtf8("emp_IdLabel"))
        self.emp_EmailLabel = QtGui.QLabel(self.centralwidget)
        self.emp_EmailLabel.setGeometry(QtCore.QRect(230, 220, 251, 20))
        self.emp_EmailLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \\\"Century Schoolbook L\\\";"))
        self.emp_EmailLabel.setObjectName(_fromUtf8("emp_EmailLabel"))
        self.passLabel = QtGui.QLabel(self.centralwidget)
        self.passLabel.setGeometry(QtCore.QRect(230, 300, 221, 20))
        self.passLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \\\"Century Schoolbook L\\\";"))
        self.passLabel.setObjectName(_fromUtf8("passLabel"))
        self.passConfLabel = QtGui.QLabel(self.centralwidget)
        self.passConfLabel.setGeometry(QtCore.QRect(220, 380, 281, 20))
        self.passConfLabel.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \\\"Century Schoolbook L\\\";"))
        self.passConfLabel.setObjectName(_fromUtf8("passConfLabel"))
        self.passConfField = QtGui.QLineEdit(self.centralwidget)
        self.passConfField.setGeometry(QtCore.QRect(510, 370, 271, 32))
        self.passConfField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))
        self.passConfField.setObjectName(_fromUtf8("passConfField"))

        self.passConfField.setEchoMode(QtGui.QLineEdit.Password)
        self.emp_nameField = QtGui.QLineEdit(self.centralwidget)
        self.emp_nameField.setGeometry(QtCore.QRect(510, 80, 271, 32))
        self.emp_nameField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254);"))
        self.emp_nameField.setObjectName(_fromUtf8("emp_nameField"))
        self.emp_IdField = QtGui.QLineEdit(self.centralwidget)
        self.emp_IdField.setGeometry(QtCore.QRect(510, 140, 271, 32))
        self.emp_IdField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))
        self.emp_IdField.setObjectName(_fromUtf8("emp_IdField"))
        self.emp_EmailField = QtGui.QLineEdit(self.centralwidget)
        self.emp_EmailField.setGeometry(QtCore.QRect(510, 220, 271, 32))
        self.emp_EmailField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))
        self.emp_EmailField.setObjectName(_fromUtf8("emp_EmailField"))
        self.passField = QtGui.QLineEdit(self.centralwidget)
        self.passField.setGeometry(QtCore.QRect(510, 300, 271, 32))
        self.passField.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))
        self.passField.setObjectName(_fromUtf8("passField"))
        self.passField.setEchoMode(QtGui.QLineEdit.Password)
        self.resetBtn = QtGui.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(430, 450, 93, 30))
        self.resetBtn.setStyleSheet(_fromUtf8("background:rgb(220, 231, 255);\n"
"font: 75 15pt \\\"Century Schoolbook L\\\";"))
        self.resetBtn.setObjectName(_fromUtf8("resetBtn"))

        self.resetBtn.clicked.connect(self.Reset)
        self.signupBtn = QtGui.QPushButton(self.centralwidget)
        self.signupBtn.setGeometry(QtCore.QRect(670, 450, 93, 30))
        self.signupBtn.setStyleSheet(_fromUtf8("background:rgb(220, 231, 255);\n"
"font: 75 15pt \\\"Century Schoolbook L\\\";"))
        self.signupBtn.setObjectName(_fromUtf8("signupBtn"))

        self.signupBtn.clicked.connect(self.Register)
        self.image_label = QtGui.QLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(13, 90, 205, 160))
        self.image_label.setObjectName(_fromUtf8("image_label"))
        self.date_label = QtGui.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(310, 9, 261, 41))
        self.date_label.setStyleSheet(_fromUtf8("background:rgb(255, 247, 185);\n"
"font: 15pt \"Latin Modern Roman Slanted\";"))
        self.date_label.setObjectName(_fromUtf8("date_label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        self.error =QtGui.QMessageBox()
        self.error.setIcon(QtGui.QMessageBox.Critical)
        self.warning =QtGui.QMessageBox()
        self.warning.setIcon(QtGui.QMessageBox.Warning)
        self.info =QtGui.QMessageBox()
        self.info.setIcon(QtGui.QMessageBox.Information)

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.dtime =time.ctime()
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee Registeration Window", None))
        self.emp_nameLabel.setText(_translate("MainWindow", "Enter Employeee Full Name:", None))
        self.emp_IdLabel.setText(_translate("MainWindow", "Enter Employee Id (Reg/No):", None))
        self.emp_EmailLabel.setText(_translate("MainWindow", "Enter Your Email Address:", None))
        self.passLabel.setText(_translate("MainWindow", "Enter Your Password :", None))
        self.passConfLabel.setText(_translate("MainWindow", "Enter Password Confirmation :", None))
        self.resetBtn.setText(_translate("MainWindow", "Reset", None))
        self.signupBtn.setText(_translate("MainWindow", "Register", None))
        #self.image_label.setText(_translate("MainWindow", "icon", None))
        self.image_label.setPixmap(QtGui.QPixmap('1.jpg'))
        self.date_label.setText(_translate("MainWindow", self.dtime, None))

    def Reset(self):
        self.emp_nameField.setText("")
        self.emp_EmailField.setText("")
        self.passField.setText("")
        self.emp_IdField.setText("")
        self.passConfField.setText("")

    def Register(self):
       
        userId =self.emp_IdField.text()
        username =self.emp_nameField.text()
        email =self.emp_EmailField.text()
        password =self.passField.text()
        passconf =self.passConfField.text()

        #email validation
        
        
        checker =re.search(r'(.*)@(.*?).com|.org|.net|.ke|.edu.*',str(email),re.M|re.I)
        #id validation
        
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

        elif not (re.match(r'[a-zA-Z0-9]{3}/[0-9]{3}/[0-9]{2}',str(userId))):
            self.emp_IdField.setStyleSheet('QLineEdit {background-color:#f6989d}')
            self.warning.setWindowTitle("Sign Up Error!")
            self.warning.setText("Employee ID must be valid!")
            self.warning.setDetailedText("Hint: Your Employee Registration Number should be in the format (bit/022/13) -case insensitive!")
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
            self.error.setText("Invalid Email Address Format!")
            self.error.setDetailedText("You entered a wrong Email Address format!\nHint: Email Address is similar to this:\n'OchiengDoa@gmail.com' or 'ochiengdoa@gmail.com'")
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
            self.passField.setStyleSheet('QLineEdit {background-color:#fff}')
        elif password in commonpass:
            self.passField.setStyleSheet('QLineEdit {background-color:#f6989d}')
            self.error.setWindowTitle("User Sign Up Error")
            self.error.setText("The password Entered too weak")
            self.error.setDetailedText("For your account security,you need to use a stronger password !")
            self.error.exec_()
            self.passField.setStyleSheet('QLineEdit {background-color:#fff}')

        elif password != passconf:
            self.passField.setStyleSheet('QLineEdit {background-color:#f6989d}')
            self.error.setWindowTitle("User Sign Up Error")
            self.error.setText("The  Password entered and password confirmation Must Match!")
            self.error.setDetailedText("Ensure the password entered and the password confirmation is the same!")
            self.error.exec_()
            self.passField.setStyleSheet('QLineEdit {background-color:#fff}')

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
                ids =[]
                for row in results:
                    dbuserId =row[0]
                    ids.append(dbuserId)

                if userId in ids:
                    self.error.setWindowTitle("User Database Error")
                    self.error.setText("That Employee Id is already in use!")
                    self.error.setDetailedText("Please ensure you enter your unique employee id\nIf you think this is a system error,please contact the admin!")
                    self.error.exec_()
                    

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
                        self.loginWindow =QtGui.QDialog()
                        self.ui =Ui_Dialog()
                        self.ui.setupUi(self.loginWindow)
                        self.loginWindow.show()
                        MainWindow.close()
                        
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
                from os import system
                system("service mysql start")




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Reg_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

