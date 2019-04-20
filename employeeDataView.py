from PyQt4 import QtCore, QtGui
import os
import sys
import time
import openpyxl
import csv
from datetime import date
#from PyQt4 import QtSql
import MySQLdb
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    from employeeMails import Ui_Form
except Exception as e:
    print e
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #just declaring some global variables...
        self.descrptn =None
        self.myfile =None
        self.conn =MySQLdb.connect(host="localhost",user="root",passwd="",db="fraud_detect")
        self.tableGui=None
        self.superV =None
        #the window class and the widgets
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(900, 600)
        MainWindow.move(50,20)
        MainWindow.setStyleSheet(_fromUtf8("background:rgb(216, 212, 255)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.dataFrame = QtGui.QFrame(self.centralwidget)
        self.dataFrame.setGeometry(QtCore.QRect(0, 210, 891, 371))
        self.dataFrame.setStyleSheet(_fromUtf8("background:rgb(170, 170, 255)"))
        self.dataFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.dataFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.dataFrame.setObjectName(_fromUtf8("dataFrame"))
        self.label = QtGui.QLabel(self.dataFrame)
        self.label.setGeometry(QtCore.QRect(160, 20, 441, 31))
        self.label.setStyleSheet(_fromUtf8("background:rgb(119, 170, 143);\n"
"color:rgb(0, 85, 0);\n"
"font: 75 18pt \"Latin Modern Sans Quotation\";"))
        self.label.setObjectName(_fromUtf8("label"))

        self.mainTable()


        self.profileFrame = QtGui.QFrame(self.centralwidget)
        self.profileFrame.setGeometry(QtCore.QRect(689, -1, 201, 138))
        self.profileFrame.setStyleSheet(_fromUtf8("background:rgb(215, 246, 255)"))
        self.profileFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.profileFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.profileFrame.setObjectName(_fromUtf8("profileFrame"))
        self.profilePicLabel = QtGui.QLabel(self.profileFrame)
        self.profilePicLabel.setGeometry(QtCore.QRect(5, 5, 191, 135))
        self.profilePicLabel.setObjectName(_fromUtf8("profilePicLabel"))
        self.nameLabel = QtGui.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(670,138,215,40)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.nameLabel.setStyleSheet(_fromUtf8("color:rgb(0,85,0);font:75 16pt \"Latin Modern Sans Quotation\";"))

        self.CalendarFrame = QtGui.QFrame(self.centralwidget)
        self.CalendarFrame.setGeometry(QtCore.QRect(10, 0, 331, 211))
        self.CalendarFrame.setStyleSheet(_fromUtf8("background:rgb(119, 170, 140)"))

        self.CalendarFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.CalendarFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.CalendarFrame.setObjectName(_fromUtf8("CalendarFrame"))
        self.calendarWidget = QtGui.QCalendarWidget(self.CalendarFrame)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 10, 296, 200))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.calendarWidget.setStyleSheet(_fromUtf8("color:black"))


        #set message pop ups
        self.warning =QtGui.QMessageBox()
        self.warning.setIcon(QtGui.QMessageBox.Warning)

        self.error = QtGui.QMessageBox()
        self.error.setIcon(QtGui.QMessageBox.Critical)

        self.info =QtGui.QMessageBox()
        self.info.setIcon(QtGui.QMessageBox.Information)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menubar.setStyleSheet(_fromUtf8("color:teal"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuTime = QtGui.QMenu(self.menubar)
        self.menuTime.setObjectName(_fromUtf8("menuTime"))
        MainWindow.setMenuBar(self.menubar)

        self.actionOpenCsv = QtGui.QAction(MainWindow)
        self.actionOpenCsv.setObjectName(_fromUtf8("actionOpenCsv"))
        self.actionMails = QtGui.QAction(MainWindow)
        self.actionMails.setObjectName(_fromUtf8("actionMails"))
        self.actionMails.setShortcut("Ctrl+M")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut("Ctrl+Q")

        self.actionOpenCsv.setShortcut("Ctrl+O")
        self.actionLogout =QtGui.QAction(MainWindow)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.actionLogout.setShortcut("Ctrl+l")

        self.menuFile.triggered[QtGui.QAction].connect(self.doFileAction)
        
        self.menuFile.addAction(self.actionOpenCsv)

        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMails)
        
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addSeparator()

        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuTime.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        cursor = self.conn.cursor()
        cursor.execute("SELECT username FROM users WHERE login_status=1")
        res =cursor.fetchall()
        if res:
            loggedEmp =str(res).strip("(),'")
        realTime = time.ctime()
        removeYear = realTime.strip('2017')
        thisTime = removeYear[10:] #just time alone is what we need

        MainWindow.setWindowTitle(_translate("MainWindow", "Employee's Main Screen", None))
        self.label.setText(_translate("MainWindow", "My Expenses Files Approval Table", None))
        self.profilePicLabel.setPixmap(QtGui.QPixmap("1.jpg"))
        self.nameLabel.setText(_translate("MainWindow",loggedEmp,None))
        self.menuFile.setTitle(_translate("MainWindow", "Menu", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuTime.setTitle(_translate("MainWindow", ("Time: %s" %thisTime), None))
        self.actionOpenCsv.setText(_translate("MainWindow", "Upload Expense File", None))
        self.actionMails.setText(_translate("MainWindow", "Mails", None))
        self.actionLogout.setText(_translate("MainWindow","Logout",None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

    def doFileAction(self,action):
        if action.text() =="Upload Expense File":
            #print "Will open a new file.."
            self.showCsvFile()

        elif action.text()=="Mails":
            #print "mails"
            self.Form =QtGui.QWidget()
            self.ui =Ui_Form()
            self.ui.setupUi(self.Form)
            self.Form.show()


            

        elif action.text() =="Logout":
            #print "Logging out the user"
            self.LogoutUser()
    

        elif action.text()=="Exit":
            print "Program Closing...",sys.exit()

    def LogoutUser(self):
        cursor =self.conn.cursor()
        query ="SELECT Employee_ID  FROM users WHERE login_status=1"
        cursor.execute(query)
        results =cursor.fetchall()
        users =[]
        if cursor.rowcount > 0:
            #print "Theres a loggedi n user"
            for user in results:
                loginuse =user[0]
                users.append(loginuse)
            if len(users) >0:
                #reset the logged status of the user
                #print users[0] gets the id of the logged in user
                update ="UPDATE users SET login_status=0 WHERE Employee_ID='%s'" %(str(users[0]))
                try:
                    cursor.execute(update)
                    self.conn.commit()
                    #print "Logout success"
                    self.info.setWindowTitle("Success Message!")
                    self.info.setText("User Successfully Logged out!")
                    self.info.setDetailedText("Program will quit since your session is no longer active!")
                    self.info.exec_()
                    sys.exit()

                except Exception as e:
                    #something went wrong
                    self.conn.rollback()
                    print e
        else:
            print "No logged in user currently"

    def showCsvFile(self):

        self.openCsvFile(self.CsvFileUpload())
        


    def openCsvFile(self,filename):
        head,tail =os.path.split(str(filename))
        self.myext = tail # i only need the file name not the directory dude
        self.myfile = filename 
        
        self.tableGui = QtGui.QWidget()
        self.model = QtGui.QStandardItemModel()
        self.tableView = QtGui.QTableView()
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        #determine the type of the file uploaded first and handle it necessarily
        if os.path.basename(str(filename)).endswith("csv"):
            with open(filename,"r") as fileInput:
                try:
                    for row in csv.reader(fileInput.read().splitlines()):#handles all the csv file size
                        self.items = [QtGui.QStandardItem(field) 
                                        for field in row]
                        self.model.appendRow(self.items)
                except Exception as err:
                    print err

        elif os.path.basename(str(filename)).endswith("xlsx") or os.path.basename(str(filename)).endswith("xls"):
            print "excel file to be handled!"

        else:
            print "Unknown file type"

        self.layout = QtGui.QVBoxLayout()

        self.updateBtn =QtGui.QPushButton("Upload File")

        self.updateBtn.clicked.connect(self.UpdateGUi)
        self.updateBtn.setStyleSheet(_fromUtf8("color:rgb(0,85,0);background:rgb(220, 231, 255);font: 75 13pt \"Century Schoolbook L\""))

        self.exitBtn =QtGui.QPushButton("Cancel Upload")
        self.exitBtn.setStyleSheet(_fromUtf8("color:rgb(0,85,0);background:rgb(220, 231, 255);font: 75 13pt \"Century Schoolbook L\""))

        self.exitBtn.clicked.connect(self.tableGui.close)#closes the current context->widget

        self.descrptnLabel =QtGui.QLabel("Expense File Description:")
        self.descrptn =QtGui.QTextEdit()

        self.supervisorLabel =QtGui.QLabel("Enter Your Supervisor:")
        self.superV =QtGui.QLineEdit()
        
        #self.descrptn.setInputMask("Enter Some Description For the Expense File")

        self.form =QtGui.QFormLayout()
        self.form.addRow(self.supervisorLabel,self.superV)
        self.form.addRow(self.descrptnLabel,self.descrptn)
        
        self.hbox =QtGui.QHBoxLayout()
        self.hbox.addWidget(self.exitBtn)
        self.hbox.addStretch()

        self.hbox.addWidget(self.updateBtn)
        self.hbox.addStretch()
       
        self.layout.addWidget(self.tableView)
        self.layout.addStretch()
        self.layout.addLayout(self.form)
        self.layout.addLayout(self.hbox)


        #self.UpdateUi(mydate,myfile,descrptnText,mystatus)

        #set the layout for the widget
        self.tableGui.setLayout(self.layout)

        self.tableGui.setWindowTitle("CSV Expense File")
        self.tableGui.resize(700,300)
        self.tableGui.show()
                

    def CsvFileUpload(self):
        self.fileDialog = QtGui.QFileDialog()
        self.mode =QtGui.QFileDialog.AnyFile
        self.fileDialog.setFileMode(self.mode)
        self.filter ="Csv Files(*.csv *.xls *xlsx)"
        self.fileDialog.setFilter(self.filter)

        self.filenames = QtCore.QStringList()

        if self.fileDialog.exec_():
            self.filenames =self.fileDialog.selectedFiles()

            self.fileOp =self.filenames[0]

            return self.fileOp
        else:
            return "Error Occured"
    def refreshGui(self):
        cursor =self.conn.cursor()
        cursor.execute("SELECT * FROM employeeExpense")
        for row,form in enumerate(cursor):
            for column,item in enumerate(form):
                self.ExpenceTableView.setItem(row,column,QtGui.QTableWidgetItem(str(item)))
        #self.ExpenceTableView.show()

    def UpdateGUi(self):
        now = date.today()
        mdate =now
        self.mfile =str(self.myfile)
        description =self.descrptn.toPlainText()
        supervisor =self.superV.text()
        cursor =self.conn.cursor() 

        print supervisor
        sup =cursor.execute("SELECT username FROM admin WHERE username ='%s'" %supervisor)
        supervisors =cursor.fetchall()
        #1st check if the file already exists
        checkFile=cursor.execute("SELECT expenseFile from employeeExpense WHERE expenseFile ='%s' " %self.mfile)
        checkFilequery =cursor.fetchall()

        if not os.path.basename(self.mfile).endswith("csv") :
                self.error.setWindowTitle("File Upload Error")
                self.error.setText("You must select a file to upload!")
                self.error.setDetailedText("You did not choose any file!\nPlease select One to continue!")
                self.error.exec_()
                self.tableGui.close()

        elif  checkFilequery:
                self.error.setWindowTitle("File Upload Error")
                self.error.setText("That File  already exists!")
                self.error.setDetailedText("This files seems to be already in the system.\nPlease upload another one or if you think it's name collision,you can rename your file!")
                self.error.exec_()
                self.tableGui.close()
        
                         
        elif (len(str(supervisor)) <1):
            self.warning.setWindowTitle("Input field Error")
            self.warning.setText("Supervisor name is required!")
            self.warning.setDetailedText("Please provide the name of your supervisor to whom the file is being sent!")
            self.warning.exec_()

        elif not supervisors:
            self.warning.setWindowTitle("Input field Error")
            self.warning.setText("There is no such supervisor!")
            self.warning.setDetailedText("Provide the username of the particular supervisor!")
            self.warning.exec_()
        elif (len(str(description))<1):
            self.warning.setWindowTitle("Input field Error")
            self.warning.setText("Description field cannot be empty!")
            self.warning.setDetailedText("Please provide some text description of the particular expense to be approved!")
            self.warning.exec_()
         

        else: 
                #all fields are there as requried
                print "There is no such file yet,supervisor name good,upload it!"
                #retrieve username of the logged employee
                userQuery ="SELECT UserName FROM users WHERE login_status=1"
                cursor.execute(userQuery)
                results =cursor.fetchall() #the result is a tuple
                usernames =[]
                for row in results:
                    dbuser =row[0]
                    usernames.append(dbuser)
                
                if len(usernames) >0:
                    insertExpense ="INSERT INTO employeeExpense(expenceDate,expenseFile,expenceText,employeeName,Supervisor)VALUES('%s','%s','%s','%s','%s')"\
                    %(mdate,self.mfile,str(description).strip("-.,'"""),str(usernames[0]),str(supervisor))

                    try:
                        cursor.execute(insertExpense)
                        self.conn.commit()
                        self.info.setWindowTitle("Success Message!")
                        self.info.setText("File Upload Was Successful!")
                        self.info.setDetailedText("File was successfully uploaded to the server!")
                        self.info.exec_()
                        #self.refreshGui()
                        
                    except Exception as e:
                        self.conn.rollback()
                        print e

                    self.tableGui.close()
                    self.refreshGui()
   
                self.tableGui.close()#closes the dialog

    def mainTable(self):
        #creating the cursor
        self.ExpenceTableView = QtGui.QTableWidget(self.dataFrame)
        self.ExpenceTableView.setGeometry(QtCore.QRect(0, 60, 870, 339))
        self.ExpenceTableView.setStyleSheet(_fromUtf8("background:rgb(255, 255, 255)"))
        self.ExpenceTableView.setObjectName(_fromUtf8("ExpenceTableView"))
        
        cursor = self.conn.cursor()
        #using the dbs result to set the table rows
        mrows = cursor.execute("SELECT  * FROM employeeExpense")
        rowcount = cursor.rowcount


        self.tableItem =QtGui.QTableWidgetItem()
        #initiate table
        self.ExpenceTableView.setWindowTitle("Some Data Samples")
        
        self.ExpenceTableView.setRowCount(rowcount)
        self.ExpenceTableView.setColumnCount(5)
        styleSheet="QHeaderView::section{Background:rgb(102,205,170);color:rgb(0,100,127);font:75 12pt;border-radius:14px}"
        self.ExpenceTableView.setStyleSheet(styleSheet)

        #set headers
        self.ExpenceTableView.setHorizontalHeaderLabels(QtCore.QString("File Upload Date ;Expense Filename;Expense  Description;Supervisor;Expense Approval Status;").split(";"))
        
        #let the columns assume the whole area
        self.header =self.ExpenceTableView.horizontalHeader()
        self.header.setResizeMode(QtGui.QHeaderView.Stretch)#can be ResizeTocontents,Stretch,Interactice(default),Fixed
        self.header.setStretchLastSection(True)
        #add data to the table,but just display data for the currently logged in user
        
        cursor.execute("SELECT username FROM users WHERE login_status=1")
        res =cursor.fetchall()
        if res:
            loggedUser =str(res).strip("(),'")
            print loggedUser
            cursor.execute("SELECT expenceDate,expenseFile,expenceText,Supervisor,status FROM employeeExpense WHERE employeeName='%s'" %loggedUser)
            for row,form in enumerate(cursor):
                
                for column,item in enumerate(form):
                    self.ExpenceTableView.setItem(row,column,QtGui.QTableWidgetItem(str(item)))
            #show the table
            """LOOKS LIKE I WANT THE STATUS TO COME OUT CLEAN!!!!"""

            #loop through headers and find column number for given column name
            headercount =self.ExpenceTableView.columnCount()
            #row =((field) (for field in range(0,rowcount)))
            columnName ="Expense Approval Status"
            for x in range(0,headercount,1):
                headerText =self.ExpenceTableView.horizontalHeaderItem(x).text()#RETRIEVE THE HEADER TEXT FOR TARGET COLUMN
                if columnName == headerText:
                    matchColumn =x
                    break
            for row in range(rowcount):
                try:
            
                    cell =self.ExpenceTableView.item(row,matchColumn).text()
                    #apply a different color to the cell depending of status text
                    if cell =="Pending":
                        
                        self.ExpenceTableView.item(row,matchColumn).setBackground(QtGui.QColor(255,215,0))
                    elif cell =="Declined":
                        self.ExpenceTableView.item(row,matchColumn).setBackground(QtGui.QColor(255,69,0))
                    else:
                        self.ExpenceTableView.item(row,matchColumn).setBackground(QtGui.QColor(154,205,50))

            
                except Exception as r:
                    message =QtGui.QLabel(self.dataFrame)
                    message.setGeometry(QtCore.QRect(120,250,440,50))
                    message.setStyleSheet(_fromUtf8("font: 75 italic 16pt \"Century Schoolbook L\";\n"
"color:rgb(255, 0, 250);\n"
"background:rgb(171, 194, 255)"))
                    message.setText("You have not uploaded any Expense File Yet!")
            self.ExpenceTableView.show()
    

if __name__ == "__main__":
    
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

