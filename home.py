from PyQt4 import QtCore, QtGui

try:
    from login import login_MainWindow

except ImportError as err:
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(787, 449)
        font = QtGui.QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(_fromUtf8("background:rgb(140, 146, 255)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.home = QtGui.QLabel(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(320, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Latin Modern Roman Demi"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.home.setFont(font)
        self.home.setStyleSheet(_fromUtf8("color:rgb(0, 104, 152);\n"
"font: 73 18pt \"Latin Modern Roman Demi\";\n"
"background:rgb(207, 255, 181)\n"
""))
        self.home.setObjectName(_fromUtf8("home"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 160, 521, 20))
        self.label.setStyleSheet(_fromUtf8("font: oblique 14pt \"Cantarell\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 160, 81, 20))
        self.label_2.setStyleSheet(_fromUtf8("\n"
"\n"
"font: 75 22pt \"Century Schoolbook L\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 190, 431, 20))
        self.label_3.setStyleSheet(_fromUtf8("font: 75 oblique 14pt \"Cantarell\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.login = QtGui.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(190, 270, 93, 30))
        self.login.setStyleSheet(_fromUtf8("background:rgb(219, 227, 255);\n"
"font: 13pt \"FreeSerif\";"))
        self.login.setObjectName(_fromUtf8("login"))
        #adding slot to the login btn
        self.login.clicked.connect(self.logme)

        self.Dialog =None

        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(460, 270, 93, 30))
        self.exit.setStyleSheet(_fromUtf8("background:rgb(211, 240, 255);\n"
"font: 13pt \"FreeSerif\";"))
        self.exit.setObjectName(_fromUtf8("exit"))
        self.exit.clicked.connect(self.quit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "FRAUD DETECTION SYSTEM!", None))
        self.home.setText(_translate("MainWindow", "  Home", None))
        self.label.setText(_translate("MainWindow", "To access the main Fraud Detect Window,You need to log in!", None))
        self.label_2.setText(_translate("MainWindow", "Note:", None))
        self.label_3.setText(_translate("MainWindow", "You must be the internal  auditor to be logged in", None))
        self.login.setText(_translate("MainWindow", "Login", None))
        self.exit.setText(_translate("MainWindow", "Exit", None))

    def quit(self):
        print "Quiting the main Program.....",sys.exit()


    def logme(self):
        print "Opening the login window!"
        self.loginWindow=QtGui.QMainWindow() #create an object of a new dialog window
        self.ui =login_MainWindow() #creating an object of the existing dialog window

        self.ui.setupUi(self.loginWindow)
        self.loginWindow.show()
        MainWindow.close()#hides the current window




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

