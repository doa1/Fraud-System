from PyQt4 import QtCore, QtGui
import MySQLdb
import csv
import os,sys
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

class Supervisor_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1010, 600)
        MainWindow.setStyleSheet(_fromUtf8("background:rgb(210, 221, 255)"))

        self.conn =MySQLdb.connect(host="localhost",user="root",passwd="",db="fraud_detect")

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.expense_frame = QtGui.QFrame(self.centralwidget)
        self.expense_frame.setGeometry(QtCore.QRect(0, 220, 1010, 331))
        self.expense_frame.setStyleSheet(_fromUtf8("background:rgb(245, 255, 255)"))
        self.expense_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.expense_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.expense_frame.setObjectName(_fromUtf8("expense_frame"))

        self.nameLabel = QtGui.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(750,138,215,40)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.nameLabel.setStyleSheet(_fromUtf8("color:rgb(0,85,0);font:75 16pt \"Latin Modern Sans Quotation\";"))

        #setting up table object
        self.tableUpdate()

        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 0, 296, 200))
        self.calendarWidget.setStyleSheet(_fromUtf8("background:rgb(246, 255, 254);\n"
"font: 75 10pt \"Bitstream Vera Serif\";\n"
"color:rgb(138, 170, 134)"))
        

        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        

        self.profile_frame = QtGui.QFrame(self.centralwidget)
        self.profile_frame.setGeometry(QtCore.QRect(740, -20, 261, 151))
        self.profile_frame.setStyleSheet(_fromUtf8("background:rgb(151, 219, 255)"))
        self.profile_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.profile_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.profile_frame.setObjectName(_fromUtf8("profile_frame"))
        self.picLabel =QtGui.QLabel(self.profile_frame)
        self.picLabel.setGeometry(1,2,260,152)
        self.picLabel.setObjectName(_fromUtf8("picLabel"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 179, 291, 31))
        self.label.setStyleSheet(_fromUtf8("color:rgb(95, 170, 103);\n"
"font: 75 oblique 14pt \"Bitstream Vera Serif\";\n"
"text-decoration: underline;\n"
"background:rgb(242, 255, 254)"))
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHealp = QtGui.QMenu(self.menubar)
        self.menuHealp.setObjectName(_fromUtf8("menuHealp"))

        MainWindow.setMenuBar(self.menubar)
        

        self.actionLogout =QtGui.QAction(MainWindow)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.actionLogout.setShortcut("Ctrl+l")

        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionClose.setShortcut("Ctrl+Q")
        self.menuFile.setStyleSheet(_fromUtf8("color:blue"))

        self.actionAudits =QtGui.QAction(MainWindow)
        self.actionAudits.setObjectName(_fromUtf8("actionAudits"))
        self.actionAudits.setShortcut("Ctrl+R")

        
        self.menuFile.addAction(self.actionAudits)
        self.menuFile.addSeparator()

        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addSeparator()

        self.menuFile.addAction(self.actionClose)
        self.menuFile.triggered[QtGui.QAction].connect(self.handleMenu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHealp.menuAction())

        self.warning =QtGui.QMessageBox()
        self.warning.setIcon(QtGui.QMessageBox.Warning)

        self.error = QtGui.QMessageBox()
        self.error.setIcon(QtGui.QMessageBox.Critical)

        self.info =QtGui.QMessageBox()
        self.info.setIcon(QtGui.QMessageBox.Information)

        #some globals initialised here
        self.thisSupervisor =None
        self.validatedDate =None
        self.validatedFile =None
        self.validatedEmployee =None

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        cursor = self.conn.cursor()
        cursor.execute("SELECT username FROM admin WHERE UserRole='Supervisor'AND login_status=1 ")
        if cursor.rowcount>0:

            res =cursor.fetchall()
            #print res
            if res:
                loggedSuperVisor =str(res).strip("(),'")
                self.thisSupervisor =loggedSuperVisor
        else:
            self.error.setWindowTitle("User Login problem")
            self.error.setText("You must be logged in first to access the system\nQuiting the program...")
            self.error.exec_()
            sys.exit()
        MainWindow.setWindowTitle(_translate("MainWindow", "Supervisor's Control Panel", None))

        self.nameLabel.setText(_translate("MainWindow", self.thisSupervisor, None))
        
        self.label.setText(_translate("MainWindow", "Expense Approval System", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHealp.setTitle(_translate("MainWindow", "Help", None))
        
        self.actionAudits.setText(_translate("MainWindow","Audit Results",None))
        self.actionLogout.setText(_translate("MainWindow","Logout",None))

        self.actionClose.setText(_translate("MainWindow", "Close", None))

        self.picLabel.setPixmap(QtGui.QPixmap("1.jpg"))

    def handleMenu(self,action):
       
        if action.text() =="Audit Results":
            self.flagged_audits()
        elif action.text()=="Logout":
            response =QtGui.QMessageBox.question(QtGui.QMessageBox(),"Message","Do you really want to kill your current session",QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
            if response ==QtGui.QMessageBox.Yes:
                
                self.LogoutUser()
        elif action.text()=="Close":
          reply = QtGui.QMessageBox.question(QtGui.QMessageBox(),"Message","Sure You want to quit?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
          if reply ==QtGui.QMessageBox.Yes:
                
                sys.exit()

    def LogoutUser(self):
        cursor =self.conn.cursor()
        query ="SELECT email FROM admin WHERE login_status=1"
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
                update ="UPDATE admin SET login_status=0 WHERE email='%s'" %(str(users[0]))
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
    @QtCore.pyqtSlot()
    def tableUpdate(self):
        self.myTable = QtGui.QTableWidget(self.expense_frame)
        self.myTable.setGeometry(QtCore.QRect(0, 30, 991, 339))
        self.myTable.setStyleSheet(_fromUtf8("background:rgb(245,245,245)"))
        self.myTable.setWindowTitle("Some Data Samples")

        

        #creating the cursor
        cursor = self.conn.cursor()
        #using the dbs result to set the table rows
        mrows = cursor.execute("SELECT  * FROM employeeExpense WHERE status='Pending'")
        rowcount = cursor.rowcount #will give the number of rows for the table

        self.myTable.setRowCount(rowcount)
        self.myTable.setColumnCount(7)
        styleSheet="QHeaderView::section{Background-color:rgb(255,250,240);color:rgb(0,100,127);font:75 12pt;border-radius:14px}"
        self.myTable.setStyleSheet(styleSheet)
        self.myTable.setHorizontalHeaderLabels(QtCore.QString("File Id;Upload Date ;Expense Filename;Description;Approval Status;Employee Name;Action").split(";"))
        self.header =self.myTable.horizontalHeader()
        self.header.setResizeMode(QtGui.QHeaderView.Stretch)#can be ResizeTocontents,Stretch,Interactive(default),Fixed
        self.header.setStretchLastSection(True)

        self.myTable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        #self.myTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.myTable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.myTable.verticalHeader().hide() #hides the vertical numbering of the table
        #time to fill up the table with data
        self.tableItem =QtGui.QTableWidgetItem()
        #retrieve data only for the logged in user
        cursor.execute("SELECT username FROM admin WHERE login_status=1 AND UserRole='Supervisor'")
        res =cursor.fetchall()
        if res:
            loggedUser =str(res).strip("(),'")
            print loggedUser
            cursor.execute("SELECT * FROM employeeExpense WHERE status='Pending' AND Supervisor='%s'" %loggedUser)
            if cursor.fetchall():
                
                for row,form in enumerate(cursor):
                    
                    for column,item in enumerate(form):
                        self.myTable.setItem(row,column,QtGui.QTableWidgetItem(str(item)))
                        self.button =QtGui.QPushButton("VIEW Expense")
                        self.button.setStyleSheet(_fromUtf8("background:rgb(210, 221, 255);color:rgb(95,158,160)"))
                        self.button.clicked.connect(self.handle_file)

                        self.myTable.setCellWidget(row,6,self.button)
            else:
                message =QtGui.QLabel(self.expense_frame)
                message.setGeometry(QtCore.QRect(90,150,650,50))
                message.setStyleSheet(_fromUtf8("font: 75 italic 16pt \"Century Schoolbook L\";\n"
"color:rgb(255, 0, 255);\n"
"background:rgb(171, 194, 255)"))
                message.setText("No Expense File uploaded has been uploaded to your account   Yet!")
            
    
    @QtCore.pyqtSlot()
    def flagged_audits(self):
        cursor =self.conn.cursor()
        self.tbGui = QtGui.QWidget()
        layout =QtGui.QVBoxLayout()
        self.tbGui.setWindowTitle("Supervisor's Action")
        self.tableV= QtGui.QTableWidget(self.tbGui)
        self.tableV.setGeometry(QtCore.QRect(5, 41, 311, 291))
        self.tableV.setStyleSheet(_fromUtf8("background:rgb(255, 255, 255)"))
        self.tableV.setObjectName(_fromUtf8("tableView"))

        self.tableV.setColumnCount(4)
        self.tableV.setHorizontalHeaderLabels(QtCore.QString("Claim Date;Claim File;Employee;").split(";"))
        allrows =cursor.execute("SELECT  * FROM employeeExpense WHERE Flagged='yes'")
        countRows =cursor.rowcount
        self.tableV.setRowCount(countRows)
        #populate the table
        cursor.execute("SELECT  expenceDate,expenseFile,employeeName FROM employeeExpense WHERE Flagged='yes'")

        for row ,data in enumerate(cursor):
            for column,value in enumerate(data):
                self.tableV.setItem(row,column,QtGui.QTableWidgetItem(str(value)))
                self.validateBtn =QtGui.QPushButton("VALIDATE")
                self.validateBtn.setStyleSheet(_fromUtf8("background:rgb(210, 221, 255);color:rgb(95,158,160)"))
                self.validateBtn.clicked.connect(self.validateClaim)

                self.tableV.setCellWidget(row,3,self.validateBtn)

        layout.addWidget(self.tableV)
        self.tbGui.setLayout(layout)
        self.tbGui.resize(500,200)
        self.tbGui.show()
    @QtCore.pyqtSlot()
    def handle_file(self):
       #print "You clicked on row "+str(row+1)+ self.myTable.item(row,col).text()+" and column "+str(col+1)
       #retrieve the cell content,if pending,retrieve the fileid,filename
       #open a dialogue to view the file ,approve or decline the expense
       self.myDialog =QtGui.QWidget()
       self.layout =QtGui.QVBoxLayout()
       minLayout =QtGui.QFormLayout()

       userLabel =QtGui.QLabel("Employee Name:")
       userName =QtGui.QLineEdit()
       minLayout.addRow(userLabel,userName)

       fileLabel =QtGui.QLabel("File Description: ")
       fileDesc =QtGui.QTextEdit()

       minLayout.addRow(fileLabel,fileDesc)
       approveBtn =QtGui.QPushButton("Approve")
       approveBtn.clicked.connect(self.Approve_Expense)

       declineBtn =QtGui.QPushButton("Decline")
       declineBtn.clicked.connect(self.decline_Expense)

       btnsLayout =QtGui.QHBoxLayout()
       btnsLayout.addWidget(declineBtn)
       btnsLayout.addStretch()
       btnsLayout.addWidget(approveBtn)
       #do something about the time
       self.model = QtGui.QStandardItemModel(self.myDialog)

       self.tableview = QtGui.QTableView(self.myDialog)
       self.tableview.setModel(self.model)
       self.tableview.horizontalHeader().setStretchLastSection(True)

       self.layout.addWidget(self.tableview)
       self.layout.addLayout(minLayout)
       self.layout.addLayout(btnsLayout)

       cell =QtGui.qApp.focusWidget()
       index =self.myTable.indexAt(cell.pos())
       if index.isValid():
           self.fileId= self.myTable.item(index.row(),0).text()
           filename =self.myTable.item(index.row(),2).text()

           fileDescription =self.myTable.item(index.row(),3).text()
           EmployeeName =self.myTable.item(index.row(),5).text()
           self.expenseStatus =self.myTable.item(index.row(),4).text()

           #check if the clicked file is csv and read it
           if os.path.basename(str(filename)).endswith("csv"):
               with open(filename,"r") as FileInput:
                    try:
                        for row in csv.reader(FileInput.read().splitlines()):
                            self.items =[QtGui.QStandardItem(field) for field in row]
                            self.model.appendRow(self.items)
                    except Exception as e:
                        print e
               userName.setText(EmployeeName)
               fileDesc.setText(fileDescription)
           else:
                #the file is an excel file,do what is necessary
                pass
           
       self.myDialog.setLayout(self.layout)
       self.myDialog.resize(500,300)
       self.myDialog.setWindowTitle("View The Expence")
       self.myDialog.show()

    def Approve_Expense(self,SelectedFile):
        SelectedFile=int(self.fileId)
        stateIndex =self.expenseStatus
        cursor =self.conn.cursor()
        updateQuery ="UPDATE employeeExpense SET status ='Approved' WHERE expenseId=%d" %(SelectedFile)
        try:
            cursor.execute(updateQuery)
            self.conn.commit()
            #close the window and update the table
            #self.myTable.item(1,4).setText("Approved")

            print (stateIndex)
            
            self.myDialog.close()
            self.button.setEnabled(False)
        
        except Exception as e:
            self.conn.rollback()
            print e
        

    def decline_Expense(self):
        self.myDialog.close()

    def validateClaim(self):
       self.validateDialog =QtGui.QWidget()
       self.model2 = QtGui.QStandardItemModel(self.validateDialog)

       self.tableview2 = QtGui.QTableView(self.validateDialog)
       self.tableview2.setModel(self.model2)
       self.tableview2.horizontalHeader().setStretchLastSection(True)
       layout =QtGui.QVBoxLayout()
       validClaim =QtGui.QPushButton("Mark as Valid?")
       validClaim.setStyleSheet(_fromUtf8("background:rgb(210, 221, 255);color:rgb(95,158,160)"))
       validClaim.clicked.connect(self.claimIsValid)

       falseClaim =QtGui.QPushButton("Mark as False?")
       falseClaim.clicked.connect(self.claimIsFalse)
       falseClaim.setStyleSheet(_fromUtf8("background:rgb(210, 221, 255);color:rgb(95,158,160)"))

       layout.addWidget(self.tableview2)

       outerW =QtGui.QHBoxLayout()
       outerW.addWidget(validClaim)
       outerW.addStretch()
       outerW.addWidget(falseClaim)

       layout.addLayout(outerW)
       cell =QtGui.qApp.focusWidget()
       index =self.tableV.indexAt(cell.pos())
       if index.isValid():
           filedate= self.tableV.item(index.row(),0).text()
           filename =self.tableV.item(index.row(),1).text()
           Employee =self.tableV.item(index.row(),2).text()
           
           self.validatedDate =filedate
           self.validatedEmployee =Employee
           self.validatedFile =filename

           #print filedate,filename,Employee,validatedBy

           #check if the clicked file is csv and read it
           if os.path.basename(str(filename)).endswith("csv"):
               with open(filename,"r") as FileInput:
                    try:
                        for row in csv.reader(FileInput.read().splitlines()):
                            self.items =[QtGui.QStandardItem(field) for field in row]
                            self.model2.appendRow(self.items)
                    except Exception as e:
                        print e
               
           else:
                #the file is an excel file,do what is necessary
                pass

       self.validateDialog.setLayout(layout)
       self.validateDialog.setWindowTitle("Mark The Claim as  Valid or False") 
       self.validateDialog.resize(500,300)  
       self.validateDialog.show()
    def claimIsValid(self):
        validatedBy =self.thisSupervisor
        #need to remoove this file from flagged list
        cursor =self.conn.cursor()
        update ="UPDATE  employeeExpense SET Flagged ='no' WHERE expenseFile ='%s'"%self.validatedFile
        try:
            cursor.execute(update)
            self.conn.commit()
            self.info.setWindowTitle("Success Message")
            self.info.setText("File Successfully removed from the flagged List!")
            self.info.exec_()
            self.validateDialog.close()
        except Exception as e:
            self.conn.rollback()
            print e
    def claimIsFalse(self):
        validatedBy =self.thisSupervisor
        print self.validatedDate,self.validatedEmployee,self.validatedFile
if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Supervisor_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

