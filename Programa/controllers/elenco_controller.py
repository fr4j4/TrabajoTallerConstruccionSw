#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from views.elenco_ui import Ui_Dialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dbManager import dbManager

class Elenco(QtGui.QDialog):
	def __init__(self):
		super(Elenco, self).__init__()
		self.ui=Ui_Dialog()
		self.ui.setupUi	(self)
		self.dbm=dbManager("data.db")
		self.dbm.connect()
		self.signals()
		self.setWindowTitle("Administrar elencos")
	
	def signals(self):
		self.ui.BCerrar.clicked.connect(self.boton_listo_clicked)
		self.ui.CPelicula.currentIndexChanged.connect(self.updateElencoList)

	def exec_(self):
		self.updateMoviesList()
		self.updateActorsList()
		self.updateCharactersList()
		super(Elenco,self).exec_()

	def updateMoviesList(self):
		self.ui.CPelicula.clear()#vaciar el combobox
		movies=self.dbm.getMovies()
		for mov in movies:
			self.ui.CPelicula.addItem(mov[u'name'],int(mov['id']))
	def updateActorsList(self):
		self.ui.CActor.clear()#vaciar el combobox
		actors=self.dbm.getActors()
		for act in actors:
			self.ui.CActor.addItem(act[u'name'],int(act['id']))

	def updateCharactersList(self):
		self.ui.CPersonaje.clear()#vaciar el combobox
		chars=self.dbm.getCharacters()
		for char in chars:
			self.ui.CPersonaje.addItem(char[u'name'],int(char['id']))

	def updateElencoList(self):
		print self.ui.CPelicula.itemData(self.ui.CPelicula.currentIndex()).toPyObject()

	def boton_listo_clicked(self):
		self.isAccepted=True;
		self.accept()