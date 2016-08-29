from PyQt4 import QtGui
import sys
from views.principal import Ui_MainWindow
from dbManager import dbManager

class App(QtGui.QMainWindow):
	def __init__(self, parent=None):
		super(self.__class__, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		dbm=dbManager('database.db')
		dbm.connect()
		self.show()

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main=App(app)
	sys.exit(app.exec_())