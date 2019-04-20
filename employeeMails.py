
from PyQt4 import QtCore, QtGui
import MySQLdb
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
        Form.resize(673, 576)
        Form.setStyleSheet(_fromUtf8("background:rgb(205, 225, 255)"))
        #some global variables
        self.conn =MySQLdb.connect(host="localhost",user="root",passwd="",db="fraud_detect")
        self.leftList = QtGui.QListWidget(Form)
        self.leftList.setGeometry(QtCore.QRect(30, 170, 256, 471))
        self.leftList.setObjectName(_fromUtf8("leftList"))
        self.menuLabel = QtGui.QLabel(Form)
        self.menuLabel.setGeometry(QtCore.QRect(70, 30, 191, 20))
        self.menuLabel.setStyleSheet(_fromUtf8("background:rgb(62, 155, 255);\n"
"font: 75 16pt \"Latin Modern Mono Prop Light\";"))
        self.menuLabel.setObjectName(_fromUtf8("menuLabel"))

        #add items to the list widget accordingly

        self.leftList.insertItem(0,'Check Inbox')
        self.leftList.insertItem(1,'Compose Message')
        self.leftList.insertItem(2,'Check Sent Mails')
        self.leftList.setStyleSheet(_fromUtf8("background:rgb(166, 190, 254);font: 15pt \"Latin Modern Math\";color:rgb(0,0,77);"))

        #activate the slots
        self.leftList.currentRowChanged.connect(self.display)
        #use vertical layout
        self.mainLayout =QtGui.QVBoxLayout()
        self.mainLayout.addWidget(self.menuLabel)
        
        #create stacks
        self.Inbox = QtGui.QWidget()
        self.Compose =QtGui.QWidget()
        self.Sent =QtGui.QWidget()

        self.Stack =QtGui.QStackedWidget()
        #add the stacks to the main widget
        self.Stack.addWidget(self.Inbox)
        self.Stack.addWidget(self.Compose)
        self.Stack.addWidget(self.Sent)

        #call methods associated with different stacks
        self.InboxGui()
        self.ComposeGui()
        self.SentGui()
        #create a layout for the lists,and the stack

        self.hbox =QtGui.QHBoxLayout()
        self.hbox.addWidget(self.leftList)
        self.hbox.addWidget(self.Stack)

        self.mainLayout.addLayout(self.hbox)

        Form.setLayout(self.mainLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Employee Mail System", None))
        self.menuLabel.setText(_translate("Form", "Menu Items", None))


    def InboxGui(self):
        layout =QtGui.QFormLayout()
        nm =QtGui.QLineEdit()
        nm.setStyleSheet(_fromUtf8("background:#fff"))

        layout.addRow("Name ",nm)
        addr =QtGui.QLineEdit()
        addr.setStyleSheet(_fromUtf8("background:#fff"))
        strt =QtGui.QLineEdit()
        strt.setStyleSheet(_fromUtf8("background:#fff"))
        layout.addRow("Address",addr)
        layout.addRow("Street",strt)
        self.Inbox.setLayout(layout)
    def ComposeGui(self):
        layout =QtGui.QFormLayout()
        receiverL =QtGui.QLabel("Receiver")
        receiverName =QtGui.QComboBox()
        cursor =self.conn.cursor()
        cursor.execute("SELECT username FROM admin WHERE UserRole ='Supervisor'")
        results =cursor.fetchall()

        users=[]
        for row in results:
            user =row[0]
            users.append(user)
        #add users to the combobox
        receiverName.addItems(users)

        #retrieve the selected receiver
        selected =receiverName.itemData(receiverName.currentIndex()).toPyObject()
        #print selected
        layout.addRow(receiverL,receiverName)
        subject =QtGui.QLineEdit()
        subject.setStyleSheet(_fromUtf8("background:white"))
        layout.addRow(QtGui.QLabel("Subject: "),subject)

        Message =QtGui.QTextEdit()
        Message.setStyleSheet(_fromUtf8("background:white"))
        layout.addRow(QtGui.QLabel("You Message: "),Message)

        sendBtn =QtGui.QPushButton("Send Message")
        resetBtn =QtGui.QPushButton("Reset ")
        sendBtn.setStyleSheet(_fromUtf8("background:rgb(176,196,222)"))
        resetBtn.setStyleSheet(_fromUtf8("background:rgb(176,196,222)"))
        layout.addRow(resetBtn,sendBtn)
        self.Compose.setLayout(layout)
    def SentGui(self):
        pass
    def display(self,i):
        self.Stack.setCurrentIndex(i)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

