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
		self.logged=False
		self.accepted=False
		self.signals()

	def signals(self):
		self.ui.BIngresar.clicked.connect(self.boton_ingresar_clicked)
		self.ui.BSalir.clicked.connect(self.quit)
	
	def showDialog(self):
		self.show()
	
	def getUser(self):
		return self.user
	
	def getPwd(self):
		return self.pwd

	def setErrorMessage(self,msg):
		self.ui.error_label.setText("")
		self.ui.error_label.setText(msg)

	def isAccepted(self):
		return self.accepted

	def boton_ingresar_clicked(self):
		self.user=self.ui.LUser.text()
		self.pwd=self.ui.LPass.text()
		self.accepted=True
		self.accept()#se acepta y cierra el dialogo
	
	def quit(self):
		self.accepted=False
		self.reject()
