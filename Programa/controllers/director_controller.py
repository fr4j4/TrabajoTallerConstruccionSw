#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from views.director_ui import Ui_Dialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Director(QtGui.QDialog):
	def __init__(self):
		super(Director, self).__init__()
		self.ui=Ui_Dialog()
		self.ui.setupUi	(self)
		self.signals()
		self.accepted=False;
		#self.show()
	
	def signals(self):
		self.ui.BListo.clicked.connect(self.boton_listo_clicked)
		self.ui.BCancelar.clicked.connect(self.boton_cancelar_clicked)

	def boton_listo_clicked(self):
		self.accepted=True;
		self.accept()

	def boton_cancelar_clicked(self):
		self.accepted=False;
		self.reject()

	def accepted(self):#devuelve true si se acepto, false si se canceló
		return self.accepted;

	def setTitle(self,title):
		self.setWindowTitle(title)

	def getData(self,data):
		if(data=="nombre"):
			return self.ui.LNombre.text()
		elif(data=="pais"):
			return self.ui.LPais.text()
		elif(data=="fnac"):
			return self.ui.LNacimiento.text()
		elif(data=="fdef"):
			return self.ui.LDefuncion.text()		

	def putData(self,data,value):
		if(data=="nombre"):
			self.ui.LNombre.setText(value)
		elif(data=="pais"):
			self.ui.LPais.setText(value)
		elif(data=="fnac"):
			self.ui.LNacimiento.setText(value)
		elif(data=="fdef"):
			self.ui.LDefuncion.setText(value)



