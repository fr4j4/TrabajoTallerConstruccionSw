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
		self.isAccepted=False;
		self.dead=False;
		self.ui.LDefuncion.setEnabled(False)
		#self.show()
	
	def signals(self):
		self.ui.BListo.clicked.connect(self.boton_listo_clicked)
		self.ui.BCancelar.clicked.connect(self.boton_cancelar_clicked)
		self.ui.CheckDead.stateChanged.connect(self.check_dead_clicked)
		self.ui.toolButton.clicked.connect(self.boton_buscar_imagen_clicked)

	def boton_listo_clicked(self):
		self.isAccepted=True;
		self.accept()

	def check_dead_clicked(self):
		if(self.ui.CheckDead.isChecked()):
			self.dead=True
			self.ui.LDefuncion.setEnabled(True)
		else:
			self.dead=False
			self.ui.LDefuncion.setEnabled(False)

	def isDead(self):
		return self.dead

	def boton_buscar_imagen_clicked(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file','',"Image files (*.jpg *.gif)")
		self.putData('img',fname)
		self.ui.Display.setPixmap(QtGui.QPixmap((fname)))

	def boton_cancelar_clicked(self):
		self.isAccepted=False;
		self.reject()

	def accepted(self):#devuelve true si se acepto, false si se canceló
		return self.isAccepted;

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
		elif(data=="img"):
			return self.ui.LImagen.text()		

	def clearData(self):
		self.putData('nombre','')
		self.putData('pais','')
		self.putData('fnac','2000-01-01')
		self.putData('fdef','2000-01-01')
		self.putData('img','')
		self.ui.Display.setPixmap(QtGui.QPixmap(("")))

	def putData(self,data,value):
		if(data=="nombre"):
			self.ui.LNombre.setText(value)
		elif(data=="pais"):
			self.ui.LPais.setText(value)
		elif(data=="fnac"):
			self.ui.LNacimiento.setDate(QtCore.QDate.fromString(value, 'yyyy-MM-dd'))
		elif(data=="fdef"):
			self.ui.LDefuncion.setDate(QtCore.QDate.fromString(value, 'yyyy-MM-dd'))
		elif(data=="img"):
			self.ui.LImagen.setText(value)	

"""
myPythonicDate='2014-04-17'
qtDate = QtCore.QDate.fromString(myPythonicDate, 'yyyy-MM-dd')
print qtDate.year(), qtDate.month(), qtDate.day()
"""

