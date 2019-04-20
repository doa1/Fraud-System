import sys
from PyQt4 import QtCore, QtGui, QtSql
try:
	import sportsconnection
except:
	pass

def initializeModel(model):
	model.setTable('users')
	model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
	model.select()
	model.setHeaderData(0,QtCore.Qt.Horizontal,"ID")
	model.setHeaderData(1,QtCore.Qt.Horizontal,"Name")
	model.setHeaderData(2,QtCore.Qt.Horizontal,"Email")
	model.setHeaderData(3,QtCore.Qt.Horizontal,"Password")
	model.setHeaderData(4,QtCore.Qt.Horizontal,"Reg Date")

def createView(title,model):
	view =QtGui.QTableView()
	view.setModel(model)
	view.setWindowTitle(title)

	return view

def addRow():
	print model.rowCount()
	ret = model.insertRows(model.rowCount(),1)

	print ret

def findrows(i):
	delrow = i.row()

if __name__ == '__main__':
	app =QtGui.QApplication(sys.argv)
	db =QtSql.QSqlDatabase.addDatabase("QMYSQL")
	db.setDatabaseName('fraud_detect')

	model =QtSql.QSqlTableModel()
	delrow =-1
	initializeModel(model)

	view1 = createView("Table Model View1",model)
	view1.clicked.connect(findrows)

	dlg = QtGui.QDialog()
	layout =QtGui.QVBoxLayout()
	layout.addWidget(view1)

	btn = QtGui.QPushButton("Add A row")
	btn.clicked.connect(addRow)
	layout.addWidget(btn)

	btn1 =QtGui.QPushButton("del a row")
	btn1.clicked.connect(lambda:model.removeRow(view1.currentIndex().row()))
	layout.addWidget(btn1)

	dlg.setLayout(layout)
	dlg.setWindowTitle("Db demo1")
	dlg.show()
	sys.exit(app.exec_())

