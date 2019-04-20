import sys
from PyQt4 import QtCore,QtGui
try:
	from PyQt4 import QtSql
except Exception as e:
	print e
def initializeModel(model):
	model.setTable("mytable")
	model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
	model.select()
	model.setHeaderData(0,QtCore.Qt.Horizontal,"ID")
	model.setHeaderData(1, QtCore.Qt.Horizontal, "First Name")
	model.setHeaderData(2, QtCore.Qt.Horizontal,"Last Name")


def createView(title,model):
	view = QtGui.QTableView()
	view.setModel(model)
	view.setWindowTitle(title)

	return view

def addRow():
	print model.rowCount()
	ret = model.insertRows(model.rowCount(),1)
	print ret

def findrow(i):
	delrow = i.row()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)

	db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
	db.setDatabaseName("dbname.db")
	model = QtSql.QSqlTableModel()

	delrow =- 1
	initializeModel(model)
	view1 = createView("Table Model (View1)",model)

	view1.clicked.connect(findrow)

	dlg =QtGui.QDialog()
	layout =QtGui.QVBoxLayout()
	layout.addWidget(view1)

	button = QtGui.QPushButton("Add A row")
	button.clicked.connect(addRow)

	layout.addWidget(button)
	btn1 = QtGui.QPushButton("Add A Row")
	btn1.clicked.connect(lambda:model.removeRow(view1.currentIndex().row()))

	layout.addWidget(btn1)
	dlg.setLayout(layout)
	dlg.setWindowTitle("Database Demo")
	dlg.show()

	sys.exit(app.exec_())