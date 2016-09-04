#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from views.movie_ui import Ui_Dialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Pelicula(QtGui.QDialog):
	def __init__(self):
		super(Pelicula, self).__init__()
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
		self.ui.BBox.clicked.connect(self.boton_buscar_imagen_clicked)

	def boton_listo_clicked(self):
		self.isAccepted=True;
		self.accept()

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
		elif(data=="estreno"):
			return self.ui.LEstreno.text()
		elif(data=="pais"):
			return self.ui.LPais.text()
		elif(data=="descripcion"):
			return self.ui.LDescripcion.text()
		elif(data=="img"):
			return self.ui.LImagen.text()		

	def clearData(self):
		self.putData('nombre','')
		self.putData('estreno','2000-01-01')
		self.putData('pais','')
		self.putData('descripcion','')
		self.putData('img','')
		self.ui.Display.setPixmap(QtGui.QPixmap(("")))

	def putData(self,data,value):
		#print "[put-data] "+data+"="+value
		if(data=="nombre"):
			self.ui.LNombre.setText(value)
		elif(data=="estreno"):
			self.ui.LEstreno.setDate(QtCore.QDate.fromString(value,'yyyy-MM-dd'))
		elif(data=="pais"):
			self.ui.LPais.setText(value)
		elif(data=="descripcion"):
			self.ui.LDescripcion.setText(value)
		elif(data=="img"):
			self.ui.LImagen.setText(value)
			self.ui.Display.setPixmap(QtGui.QPixmap((value)))
