# -*- coding: utf-8 -*-
#!/usr/bin/python

# 
#
# Auditor: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
import MySQLdb
import sys,os
import csv
from math import log10
from collections import Counter
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

class Audit_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1008, 640)
        MainWindow.move(50,20)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.conn =MySQLdb.connect(host="localhost",user="root",passwd="",db="fraud_detect")

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.main_frame = QtGui.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 20, 641, 601))
        self.main_frame.setStyleSheet(_fromUtf8("background:rgb(246, 255, 254)"))
        self.main_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.main_frame.setObjectName(_fromUtf8("main_frame"))
        self.updateGui()

        self.label = QtGui.QLabel(self.main_frame)
        self.label.setGeometry(QtCore.QRect(160, 10, 201, 41))
        self.label.setStyleSheet(_fromUtf8("font: 75 italic 18pt \"Century Schoolbook L\";\n"
"color:rgb(0, 0, 255);\n"
"background:rgb(171, 194, 255)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.flagged_frame = QtGui.QFrame(self.centralwidget)
        self.flagged_frame.setGeometry(QtCore.QRect(660, 230, 331, 351))
        self.flagged_frame.setStyleSheet(_fromUtf8("background:rgb(229, 255, 242)"))
        self.flagged_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.flagged_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.flagged_frame.setObjectName(_fromUtf8("flagged_frame"))

        #check if there is a flagged file and display it
        tcursor =self.conn.cursor()
        tcursor.execute("SELECT  * FROM employeeExpense WHERE Flagged='yes'")
        queryResult =tcursor.rowcount
        if queryResult >0:
            
            self.flagged_table()

        else:
            self.lb =QtGui.QLabel(self.flagged_frame)
            self.lb.setText("There are no flagged files yet!\n Run the 'Detect'")
            self.lb.setGeometry(15,90,301,50)
            self.lb.setStyleSheet(_fromUtf8("font: 18pt \"FreeSerif\";\n"
"background: white;\n"
"color:rgb(0, 5, 255)"))

        self.label_2 = QtGui.QLabel(self.flagged_frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 15pt \"FreeSerif\";\n"
"text-decoration: underline;\n"
"color:rgb(0, 85, 255)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.refresh =QtGui.QPushButton(self.flagged_frame)
        self.refresh.setText("Refresh?")
        self.refresh.setGeometry(230,40,90,30)
        self.refresh.setStyleSheet(_fromUtf8("background:rgb(220, 231, 255);\n"
"font: 75 13pt \"Century Schoolbook L\";"))
        self.refresh.clicked.connect(self.flagged_table)

        self.calendarWidget = QtGui.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(670, 20, 296, 200))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuTime = QtGui.QMenu(self.menubar)
        self.menuTime.setObjectName(_fromUtf8("menuTime"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.actionMails =QtGui.QAction(MainWindow)
        self.actionMails.setObjectName(_fromUtf8("actionMails"))
        self.actionMails.setShortcut("CTRL+M")

        self.actionLogout =QtGui.QAction(MainWindow)
        self.actionLogout.setObjectName(_fromUtf8("actionLogout"))
        self.actionLogout.setShortcut("Ctrl+L")
        self.actionClose =QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionClose.setShortcut("Ctrl+Q")

        self.menuFile.addAction(self.actionMails)
        self.menuFile.addSeparator()

        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)

        self.menuFile.triggered[QtGui.QAction].connect(self.handleMenu)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuTime.menuAction())

        self.warning =QtGui.QMessageBox()
        self.warning.setIcon(QtGui.QMessageBox.Warning)

        self.error = QtGui.QMessageBox()
        self.error.setIcon(QtGui.QMessageBox.Critical)

        self.info =QtGui.QMessageBox()
        self.info.setIcon(QtGui.QMessageBox.Information)
        
        self.timer =QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.flagged_table)
        self.color_flag =True

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        realTime = time.ctime()
        removeYear = realTime.strip('2017')
        thisTime = removeYear[10:] #just time alone is what we need

        MainWindow.setWindowTitle(_translate("MainWindow", "Auditors Area", None))
        self.label.setText(_translate("MainWindow", "Main Audit Area", None))
        self.label_2.setText(_translate("MainWindow", "Flagged  Audit Results for Validation", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionMails.setText(_translate("MainWindow","Check Mails",None))
        self.actionLogout.setText(_translate("MainWindow","Logout",None))
        self.actionClose.setText(_translate("MainWindow","Exit",None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuTime.setTitle(_translate("MainWindow", ("Time %s"%thisTime), None))

    def handleMenu(self,q):
        if q.text()=="Check Mails":
            print "handle Mails"
        elif q.text() =="Logout":
           self.info.setWindowTitle("User Session Kill..")
           self.info.setText("You are about to end this session..")
           self.info.exec_()
        elif q.text()=="Exit":
            '''self.info.setWindowTitle("Window Closing..")
            self.info.setText("Quiting the program")
            self.info.exec_()'''
            reply = QtGui.QMessageBox.question(QtGui.QMessageBox(),"Message","Sure You want to quit?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            if reply ==QtGui.QMessageBox.Yes:
                
                sys.exit()
    @QtCore.pyqtSlot()
    def updateGui(self):
        cursor =self.conn.cursor()

        self.tableWidget = QtGui.QTableWidget(self.main_frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 61, 621, 471))
        self.tableWidget.setStyleSheet(_fromUtf8("background:rgb(255, 255, 255)"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(QtCore.QString("File Upload Date;Expense Filename;Employee;Supervisor;Action").split(";"))
        self.tableItem =QtGui.QTableWidgetItem()

        mrows = cursor.execute("SELECT  * FROM employeeExpense WHERE status='Approved'")
        rowcount = cursor.rowcount #will give the number of rows for the table

        self.tableWidget.setRowCount(rowcount)
        cursor.execute("SELECT expencedate,expenseFile,employeeName,Supervisor FROM employeeExpense WHERE status='Approved'")
        for row,form in enumerate(cursor):
            
            for column,item in enumerate(form):
                self.tableWidget.setItem(row,column,QtGui.QTableWidgetItem(str(item)))
                self.button =QtGui.QPushButton("DETECT")
                self.button.setStyleSheet(_fromUtf8("background:rgb(210, 221, 255);color:rgb(95,158,160)"))
                self.button.clicked.connect(self.detect)

                self.tableWidget.setCellWidget(row,4,self.button)

    def flagged_table(self):
        
        cursor =self.conn.cursor()

        self.tableV= QtGui.QTableWidget(self.flagged_frame)
        self.tableV.setGeometry(QtCore.QRect(5, 41, 311, 291))
        self.tableV.setStyleSheet(_fromUtf8("background:rgb(255, 255, 255)"))
        self.tableV.setObjectName(_fromUtf8("tableView"))

        self.tableV.setColumnCount(3)
        self.tableV.setHorizontalHeaderLabels(QtCore.QString("Claim File;Employee;Supervisor").split(";"))
        allrows =cursor.execute("SELECT  * FROM employeeExpense WHERE Flagged='yes'")
        countRows =cursor.rowcount
        self.tableV.setRowCount(countRows)
        #populate the table
        cursor.execute("SELECT  expenseFile,employeeName,Supervisor FROM employeeExpense WHERE Flagged='yes'")

        for row ,data in enumerate(cursor):
            for column,value in enumerate(data):
                self.tableV.setItem(row,column,QtGui.QTableWidgetItem(str(value)))

        QtCore.QTimer.singleShot(1000,self.flagged_table)
    def getItems(self):
        #get the current cell the user in
        try:
            cell =QtGui.qApp.focusWidget()
            index =self.tableWidget.indexAt(cell.pos())
            if index.isValid():
                self.filename =self.tableWidget.item(index.row(),1).text()
                self.Employee =self.tableWidget.item(index.row(),2).text()
                self.SupervisorName =self.tableWidget.item(index.row(),3).text()
                
                return self.filename,self.Employee,self.SupervisorName
        except Exception,error:
            return None

    def read_File(self):
        filename =self.getItems()
        file = str(filename[0]).strip("(PyQt4.QtCore.QString()")

        amounts =[]
        print file
        try:
           with open(file,'r') as InputFile:
            Data = csv.DictReader(InputFile.read().splitlines())
            for row in Data:
                try:
                    amounts.append(row['Amount'])
                except Exception as e:
                    self.error.setWindowTitle("File Reading Error")
                    self.error.setText("Error while reading the file!")
                    self.error.setDetailedText("We had issues reading the file looks the file misses the 'Amount' column!")
                    self.error.exec_()
                    break
            return amounts  
             
        except Exception as e:
            self.error.setWindowTitle("File Error")
            self.error.setText("File not Found Error!")
            self.error.setDetailedText("Looks like the file has been temporarily moved or permanently removed!")
            self.error.exec_()
            return 0
    def finding_leading_digit(self,line):
        numbers ='123456789'
        NumberIndex =len(line)
        for x in xrange(0,NumberIndex):
            if line[x] in numbers:
                return int(line[x])
        return 0
    def run_benford(self):
        employeeName =str(self.getItems()[1]).strip("(PyQt4.QtCore.QString()")
        MySupervisor =str(self.getItems()[2:]).strip("(PyQt4.QtCore.QString() u')")

        valuesList = self.read_File()
        #check if this is not the file we wanted or if the file doesnt exist anymore
        if valuesList is 0 or self.getItems() is None:
            print "Nothing yet"

        else:
            listOfOccurances =[0,0,0,0,0,0,0,0,0]#setting digit occurance to 0 for every digit
            leadingValues =[]
            try:
                for value in valuesList:
                    digit =str(value).lstrip()
                    leadingDigit =self.finding_leading_digit(digit)
                    leadingValues.append(leadingDigit)
                    if leadingDigit != 0:
                        listOfOccurances[leadingDigit-1] +=1

            except Exception as error:
                print error

            #return leadingValues,listOfOccurances
           # print "Occurance by digit %s"%str(Counter(leadingValues)).strip("Counter()")
            SumOfDigitis =0
            for i in (Counter(leadingValues)).values():
                SumOfDigitis +=i

            frequencyOfOccurance =[]
            myKeys =[]
            print "Digit\t\tFrequency of occurance"
            for key,item in (Counter(leadingValues)).items():
                frequencyOfOccurance.append(100 * float(item) /float(SumOfDigitis))
                myKeys.append(key)
               
            self.myDld = QtGui.QWidget()
            self.table =QtGui.QTableWidget()
            self.table.setRowCount(len(myKeys))
            self.table.setColumnCount(5)
            self.table.setHorizontalHeaderLabels(QtCore.QString("First Digit;Actual Distribution;Benford's Law Distribution;Deviation;Anomaly?").split(";"))
            self.table.verticalHeader().hide()

            header =self.table.horizontalHeader()
            header.setResizeMode(QtGui.QHeaderView.ResizeToContents)#can be ResizeTocontents,Stretch,Interactive(default),Fixed
            header.setStretchLastSection(True)

            item = QtGui.QTableWidgetItem()

            Allnumbers =[float(n) for n in range(1,10)]
            benfords =[log10(1+1/d) for d in Allnumbers]
            #print "Actual Distribution and the Distribution as predicted by Benfords Law"
            
            #print "First Digit\t\tActual Distribution\t\tBenford's Distribution\t\tDeviation from the Law"
            flagged_result =[]

            for keys,values,ben in zip(myKeys,frequencyOfOccurance,benfords):
                self.label1 =QtGui.QLabel()
                self.label2 =QtGui.QLabel()
                self.label3 =QtGui.QLabel()
                self.label4 =QtGui.QLabel()
                self.label5 =QtGui.QLabel("Yes")
                self.label5.setStyleSheet(_fromUtf8("font: 75 italic 16pt \"Century Schoolbook L\";\n"
    "color:rgb(0, 0, 250);\n""background:rgb(255, 69, 0)"))
                print "\t%d\t\t\t %5.1f%%\t\t\t\t %5.1f%%\t\t\t\t %5.1f%%" %(keys,values,ben*100.,abs(values - (ben*100.)))
                key =keys
                actual =round(values,2)
                law =round(ben *100. ,2)
                diff =round(abs(values - (ben*100.)),2)
                self.label1.setText(QtCore.QString(str(actual)))
                self.label2.setText(QtCore.QString(str(law)))
                self.label3.setText(QtCore.QString(str(diff)))

                self.label4.setText(QtCore.QString(str(key)))

                self.table.setCellWidget(key-1,0,self.label4)
                self.table.setCellWidget(key-1,1,self.label1)
                self.table.setCellWidget(key-1,2,self.label2)
                self.table.setCellWidget(key-1,3,self.label3)
                if diff>5:
                    #self.table.setStyleSheet(_fromUtf8("background:red"))
                    self.table.setCellWidget(key-1,4,self.label5)
                    flagged_result.append(diff)
                    

            if len(flagged_result) is not 0:
                self.Audit_Result()
            else:
                self.info.setWindowTitle("File opened for view")
                self.info.setText("We did not detect any anomaly in this file.\nYou shall proceed to view it anyway!")
                self.info.exec_()
            layout =QtGui.QVBoxLayout()
            layout.addWidget(self.table)
            self.myDld.setLayout(layout)
            self.myDld.resize(600,400)
            self.myDld.setWindowTitle("Actual Observation against Benford's ")
            self.myDld.show()

    @QtCore.pyqtSlot()
    def detect(self):
        self.run_benford()

    @QtCore.pyqtSlot()
    def Audit_Result(self):
        filename =self.getItems()
        file = str(filename[0]).strip("(PyQt4.QtCore.QString()")
        cursor =self.conn.cursor()
        #check if the file was already added
        query =cursor.execute("SELECT * FROM employeeExpense WHERE Flagged='yes' AND expenseFile ='%s'" %file)
        myrows = cursor.rowcount
        if myrows<1:
            #that file doesnt exist,add it
            update ="UPDATE employeeExpense SET Flagged='yes' WHERE expenseFile= '%s'" %file
            try:
                cursor.execute(update)
                self.conn.commit()
                self.info.setWindowTitle("Success message")
                self.info.setText("File has been successfully added for review added for review ")
                self.info.exec_()
                self.flagged_table()
            except Exception as e:
                self.conn.rollback()
                print "Sorry error %s"% e
        else:
            self.error.setWindowTitle("Error Message")
            self.error.setText("File already flagged. You can just view it though ")
            self.error.exec_()
    def start(self):
        self.timer.start()

if __name__ == "__main__":
   
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui =Audit_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())

