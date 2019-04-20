import sys
import re
import os
from PyQt4 import QtCore, QtGui
try:
    from home import Ui_MainWindow
    from supervisorHome import Supervisor_MainWindow
    from AuditMenu import Audit_MainWindow
except ImportError as er:
    print er

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

        MainWindow.setObjectName(_fromUtf8("Admin Login"))
        MainWindow.resize(655, 381)
        MainWindow.setStyleSheet(_fromUtf8("background:rgb(172, 183, 255)"))
        self.formLayoutWidget = QtGui.QWidget(MainWindow)
        self.formLayoutWidget.setGeometry(QtCore.QRect(280, 90, 321, 111))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.user_label = QtGui.QLabel(self.formLayoutWidget)
        self.user_label.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \"Century Schoolbook L\";"))
        self.user_label.setObjectName(_fromUtf8("user_label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.user_label)
        self.user_lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.user_lineEdit.setStyleSheet(_fromUtf8("background:rgb(237, 255, 254)"))
        self.user_lineEdit.setObjectName(_fromUtf8("user_lineEdit"))

        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.user_lineEdit)
        self.pass_label = QtGui.QLabel(self.formLayoutWidget)
        self.pass_label.setStyleSheet(_fromUtf8("color:rgb(0, 31, 94);\n"
"font: 75 15pt \"Century Schoolbook L\";"))
        self.pass_label.setObjectName(_fromUtf8("pass_label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.pass_label)
        self.pass_lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.pass_lineEdit.setStyleSheet(_fromUtf8("background:rgb(230, 244, 255)"))
        self.pass_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.pass_lineEdit.setObjectName(_fromUtf8("pass_lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.pass_lineEdit)
        self.image_icon = QtGui.QLabel(MainWindow)
        self.image_icon.setGeometry(QtCore.QRect(40, 100, 250, 150))
        #elf.image_icon.setPixmap(QtGui.QPixmap("1.jpg"))
        self.image_icon.setObjectName(_fromUtf8("image_icon"))
        self.login = QtGui.QPushButton(MainWindow)
        self.login.setGeometry(QtCore.QRect(490, 220, 93, 30))

        self.login.setStyleSheet(_fromUtf8("background:rgb(220, 231, 255);\n"
"font: 75 13pt \"Century Schoolbook L\";"))
        self.login.setObjectName(_fromUtf8("login"))
        self.login.clicked.connect(self.Login)
        self.exit = QtGui.QPushButton(MainWindow)
        self.exit.setGeometry(QtCore.QRect(340, 220, 93, 30))
        self.exit.setStyleSheet(_fromUtf8("background:rgb(220, 231, 255);\n"
"font: 75 13pt \"Century Schoolbook L\";"))
        self.exit.setObjectName(_fromUtf8("exit"))
        #when exit button clicked,quit
        self.exit.clicked.connect(self.quit)

        self.image_icon_2 = QtGui.QLabel(MainWindow)
        self.image_icon_2.setGeometry(QtCore.QRect(70, 39, 581, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.image_icon_2.setFont(font)
        self.image_icon_2.setStyleSheet(_fromUtf8("color:rgb(0, 85, 255);"))
        self.image_icon_2.setObjectName(_fromUtf8("image_icon_2"))
        #set message MainWindows
        self.warning =QtGui.QMessageBox()
        self.warning.setIcon(QtGui.QMessageBox.Warning)

        self.error = QtGui.QMessageBox()
        self.error.setIcon(QtGui.QMessageBox.Critical)

        self.info =QtGui.QMessageBox()
        self.info.setIcon(QtGui.QMessageBox.Information)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Auditor/Supervisor Login", None))
        self.user_label.setText(_translate("MainWindow", "Username:", None))
        self.pass_label.setText(_translate("MainWindow", "Password:", None))
        self.image_icon.setPixmap(QtGui.QPixmap("1.jpg"))
        self.login.setText(_translate("MainWindow", "Login", None))
        self.exit.setText(_translate("MainWindow", "Quit", None))
        self.image_icon_2.setText(_translate("MainWindow", "Enter Your Login Details (Email and Password) to continue:", None))


    def quit(self):
        self.warning.setWindowTitle("Stopping the Server")
        self.warning.setText("Wait while server stops....")
        self.warning.setDetailedText("Closing the program means releasing mysql resource to be used by other system program\nBe patient kindly while we stop the services for you..")
        self.warning.exec_()
        os.system("service mysql stop")
        print "Quiting the login window...",sys.exit(0)
        """self.homeWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.homeWindow)
        #self.homeWindow.resize(700,500)
        self.homeWindow.show()

        MainWindow.close()"""


    def Login(self):
        import MySQLdb
        #get the user inputs
        username=self.user_lineEdit.text()
        password=self.pass_lineEdit.text()
        #email validation
        checker =re.search(r'(.*)@(.*?).com|.org|.net|.ke|.edu.*',str(username),re.M|re.I)
        #check if the user entered anythin
        try:
            conn =MySQLdb.connect(host="localhost",user="root",passwd="",db="fraud_detect")
       
            #prepare the cursor
            cursor=conn.cursor()

            if (len(str(username)) < 1):
                self.user_lineEdit.setStyleSheet('QLineEdit {background-color:red}')
                self.warning.setWindowTitle("Admin Login Error")
                self.warning.setText("Username is required!")
                self.warning.setDetailedText("You must enter your unique email address to proceed ")
                self.warning.exec_()
                self.user_lineEdit.setStyleSheet('QLineEdit {background-color:#fff}')
            elif (len(str(password)) < 1):
                self.pass_lineEdit.setStyleSheet('QLineEdit {background-color:red}')
                self.warning.setWindowTitle("Admin Login Error")
                self.warning.setText("Password is  required!")
                self.warning.setDetailedText("Your password is necessary for accessing the control panel")
                self.warning.exec_()
                self.pass_lineEdit.setStyleSheet('QLineEdit {background-color:#fff}')

            elif not checker:
                self.user_lineEdit.setStyleSheet('QLineEdit {background-color:red}')
                self.warning.setWindowTitle("Admin Login Error")
                self.warning.setText("Email address is invalid!")
                self.warning.setDetailedText("You a valid email address to proceed ")
                self.warning.exec_()
                self.user_lineEdit.setStyleSheet('QLineEdit {background-color:#fff}')
            else:

                query="SELECT id,email,password,UserRole FROM admin WHERE email ='%s'" %username

                cursor.execute(query)
                if cursor.rowcount>0:
                    rows =cursor.fetchall()
                    names =[]
                    passwords=[]
                    userType =[]
                    ids =[]
                    for row in rows:
                        userId =row[0]
                        dbuser=row[1]
                        dbpass=row[2]
                        dbuserRole =row[3]
                        ids.append(userId)
                        names.append(dbuser)
                        passwords.append(dbpass)
                        userType.append(dbuserRole)

            
                    if  password not in passwords:
                        
                        self.pass_lineEdit.setStyleSheet('QLineEdit {background-color:red}')
                        self.error.setWindowTitle("Admin Login Error")
                        self.error.setText("Incorrect User Password !")
                        self.error.setDetailedText("Hint:\nEnsure you enter the correct password and retry!")
                        self.error.exec_()
                        self.user_lineEdit.setStyleSheet('QLineEdit {background-color:#fff}')
                        self.pass_lineEdit.setStyleSheet('QLineEdit {background-color:#fff}')
                        
                        self.pass_lineEdit.setText("")
                        
                    else:
                        userType
                        print userType[0] 
                        if  str(userType[0]) =='Supervisor':  # i mean not auditor 
                            try:
                                cursor.execute("UPDATE admin SET login_status = 1 WHERE id =%d"%ids[0])
                                conn.commit()

                                self.info.setWindowTitle("Login Success")
                                self.info.setText("Login was Successful")
                                self.info.setDetailedText("You are successfully logged in as a supervisor!")
                                self.info.exec_()
                                #redirect the user to the control panel
                                

                                self.supervisorWindow =QtGui.QMainWindow()
                                self.ui =Supervisor_MainWindow()
                                self.ui.setupUi(self.supervisorWindow)
                                self.supervisorWindow.show()
                                MainWindow.close()

                        
                            except Exception as e:
                                print e
                                conn.rollback()
                        else:
                            #u r an auditor,get to the auditor pane;
                            try:
                                cursor.execute("UPDATE admin SET login_status = 1 WHERE id =%d"%ids[0])
                                conn.commit()
                                self.info.setWindowTitle("Login Success")
                                self.info.setText("Login was Successful")
                                self.info.setDetailedText("You are successfully logged in as a supervisor!")
                                self.info.exec_()

                                #redirect the auditor
                                self.auditScreen = QtGui.QMainWindow()
                                self.Ui =Audit_MainWindow()
                                self.Ui.setupUi(self.auditScreen)
                                self.auditScreen.show()
                                MainWindow.close()
                            except Exception as e:
                                print e
                                conn.rollback()
                else:
                    self.user_lineEdit.setStyleSheet('QLineEdit {background-color:red}')
                    self.pass_lineEdit.setStyleSheet('QLineEdit {background-color:red}')
                    self.error.setWindowTitle("Admin Login Error")
                    self.error.setText("Such user does not exist in this system!\nEnsure you are registered and authorised to use the system!")
                    self.error.setDetailedText("Hint:\nConfirm your login details and retry again\nIf you think this is a system error,please contact admin")
                    self.error.exec_()
                    self.user_lineEdit.setStyleSheet('QLineEdit {background-color:#fff}')
                    self.pass_lineEdit.setStyleSheet('QLineEdit {background-color:#fff}')
                    self.user_lineEdit.setText("")
                    self.pass_lineEdit.setText("")
                    
        except Exception as e:
            self.warning.setWindowTitle("SQL Server Error")
            self.warning.setText("Connection to the database server failed!")
            self.warning.setDetailedText("Seems You are trying to access the System before starting the server!\nWorry not,we'll start for you in a moment!")
            self.warning.exec_()
            
            os.system("service mysql start")
            self.info.setWindowTitle("SQL Server Connection")
            self.info.setText("Starting mysql server...\n\nServer Successfully Started!")
            self.info.exec_()
            print

if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = login_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

