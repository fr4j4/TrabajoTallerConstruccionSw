import sys
sys.path.append("..")
from views.login_ui import Ui_Dialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class Login(QtGui.QDialog):
	def __init__(self):
		super(Login, self).__init__()
		self.user=""
		self.pwd=""
		self.ui=Ui_Dialog()
		self.ui.setupUi	(self)
		self.signals()

	def signals(self):
		self.ui.BIngresar.clicked.connect(self.boton_ingresar_clicked)
	
	def showDialog(self):
		self.show()
	
	def getUser(self):
		return self.user
	
	def getPwd(self):
		return self.pwd

	def boton_ingresar_clicked(self):
		self.user=self.ui.LUser.text()
		self.pwd=self.ui.LPass.text()
		self.accept()#se acepta y cierra el dialogo


"""
if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	main = Login()
	sys.exit(app.exec_())
"""