#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from views.actor_ui import Ui_Dialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Actor(QtGui.QDialog):
	def __init__(self):
		super(Actor, self).__init__()
		self.ui=Ui_Dialog()
		self.ui.setupUi	(self)
		self.signals()
		self.isAccepted=False;
		self.ui.LGenero.addItem("--- Seleccione ---");
		self.ui.LGenero.addItem("Masculino");
		self.ui.LGenero.addItem("Femenino");
	
	def signals(self):
		self.ui.BListo.clicked.connect(self.boton_listo_clicked)
		self.ui.BCancelar.clicked.connect(self.boton_cancelar_clicked)
		self.ui.toolButton.clicked.connect(self.boton_buscar_imagen_clicked)

	def boton_listo_clicked(self):
		self.isAccepted=True;
		self.accept()

	def boton_cancelar_clicked(self):
		self.isAccepted=False;
		self.reject()

	def boton_buscar_imagen_clicked(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file','',"Image files (*.jpg *.gif)")
		self.putData('img',fname)
		self.ui.Display.setPixmap(QtGui.QPixmap((fname)))
	
	def setTitle(self,title):
		self.setWindowTitle(title)

	def accepted(self):#devuelve true si se acepto, false si se canceló
		return self.isAccepted;

	def getData(self,data):
		if(data=="nombre"):
			return self.ui.LNombre.text()
		elif(data=="fnac"):
			return self.ui.LFecha.text()
		elif(data=="img"):
			return self.ui.LImagen.text()
		elif(data=="genero"):
			g=""
			if self.ui.LGenero.currentIndex()==1:
				g="M"
			elif self.ui.LGenero.currentIndex()==2:
				g="F"
			return g		

	def clearData(self):
		self.putData('nombre','')
		self.putData('fnac','2000-01-01')
		self.putData('img','')
		self.putData('genero','')
		self.ui.Display.setPixmap(QtGui.QPixmap(("")))
		self.ui.LGenero.setCurrentIndex(0)

	def putData(self,data,value):
		print "actor: [put-data] "+data+"="+value
		if(data=="nombre"):
			self.ui.LNombre.setText(value)
		elif(data=="fnac"):
			self.ui.LFecha.setDate(QtCore.QDate.fromString(value,'yyyy-MM-dd'))
		elif(data=="img"):
			self.ui.LImagen.setText(value)
			self.ui.Display.setPixmap(QtGui.QPixmap((value)))
		elif(data=="genero"):
			if data.upper()=="F":
				self.ui.LGenero.setCurrentIndex(1)
			elif data.upper()=="M":
				self.ui.LGenero.setCurrentIndex(1)
			else:
				self.ui.LGenero.setCurrentIndex(0)
	