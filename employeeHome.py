from PyQt4 import QtCore, QtGui
import sys
try:
    from employeeLogin import login_MainWindow
    from employeeRegister import Reg_MainWindow
except Exception as err:
    print err

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(807, 467)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("FreeSans"))
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        Form.setFont(font)
        Form.setStyleSheet(_fromUtf8("background:rgb(166, 190, 254);\n"
"color:rgb(3, 3, 83);\n"
"font: italic 13pt \"FreeSans\";"))
        self.home = QtGui.QLabel(Form)
        self.home.setGeometry(QtCore.QRect(300, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Schoolbook L"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(9)
        self.home.setFont(font)
        self.home.setStyleSheet(_fromUtf8("\n"
"font: 75 18pt \"Century Schoolbook L\";\n"
"color:rgb(2, 2, 2)"))
        self.home.setObjectName(_fromUtf8("home"))
        self.note = QtGui.QLabel(Form)
        self.note.setGeometry(QtCore.QRect(30, 70, 64, 20))
        self.note.setStyleSheet(_fromUtf8("\n"
"font: 75 16pt \"Century Schoolbook L\";\n"
"color:rgb(2, 2, 2)"))
        self.note.setObjectName(_fromUtf8("note"))
        self.note_2 = QtGui.QLabel(Form)
        self.note_2.setGeometry(QtCore.QRect(100, 70, 671, 20))
        self.note_2.setObjectName(_fromUtf8("note_2"))
        self.note_3 = QtGui.QLabel(Form)
        self.note_3.setGeometry(QtCore.QRect(90, 120, 621, 20))
        self.note_3.setObjectName(_fromUtf8("note_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(90, 90, 291, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 140, 421, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 180, 191, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(350, 160, 421, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 230, 691, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.loginbtn = QtGui.QPushButton(Form)
        self.loginbtn.setGeometry(QtCore.QRect(110, 320, 93, 30))
        self.loginbtn.setStyleSheet(_fromUtf8("background:rgb(220, 244, 255);\n"
"font: 63 13pt \"Latin Modern Roman Demi\";"))
        self.loginbtn.setObjectName(_fromUtf8("loginbtn"))

        self.loginbtn.clicked.connect(self.logme)
        self.exitBtn = QtGui.QPushButton(Form)
        self.exitBtn.setGeometry(QtCore.QRect(450, 320, 93, 30))
        self.exitBtn.setStyleSheet(_fromUtf8("background:rgb(220, 244, 255);\n"
"font: 63 13pt \"Latin Modern Roman Demi\";"))
        self.exitBtn.setObjectName(_fromUtf8("exitBtn"))
        self.exitBtn.clicked.connect(self.Register)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Employee HomePage", None))
        self.home.setText(_translate("Form", "Employee Home", None))
        self.note.setText(_translate("Form", "Note:", None))
        self.note_2.setText(_translate("Form", "All Employees are required to upload documents detailing all forms of transactions", None))
        self.note_3.setText(_translate("Form", "The documents must be in a csv format and contain the following details:", None))
        self.label.setText(_translate("Form", " and any expense   to this System.", None))
        self.label_2.setText(_translate("Form", "tranasaction type,amount spent,your employee name,", None))
        self.label_3.setText(_translate("Form", "date of the transaction.", None))
        self.label_4.setText(_translate("Form", "name of your supervisor who authorised the transaction,", None))
        self.label_5.setText(_translate("Form", "To be able to do this ,You must log in first. Otherwise you will be required to signup first with your employee details.", None))
        self.loginbtn.setText(_translate("Form", "Login", None))
        self.exitBtn.setText(_translate("Form", "Register", None))

    def logme(self):
        self.empLogin =QtGui.QMainWindow() #creating an instance of a dialog window
        self.ui =login_MainWindow() #calling the dialog class
        self.ui.setupUi(self.empLogin)#entering the main event loop
        self.empLogin.show()

        #close the current window
        Form.close()

    def Register(self):
       # sys.exit(0)
       self.regWind =QtGui.QMainWindow()
       self.ui =Reg_MainWindow()
       self.ui.setupUi(self.regWind)
       self.regWind.show()

       Form.close()


if __name__ == "__main__":
   
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

