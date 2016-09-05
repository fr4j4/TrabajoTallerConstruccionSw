#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from views.elenco_ui import Ui_Dialog
from controllers.character_controller import Character
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
		self.character=Character()
		
		self.setWindowTitle("Administrar elencos")
		#self.ui.BPersonajes.setEnabled(False)
	
	def signals(self):
		self.ui.BCerrar.clicked.connect(self.boton_listo_clicked)
		self.ui.CPelicula.currentIndexChanged.connect(self.updateElencoList)
		self.ui.BAgregar.clicked.connect(self.agregarAElenco)
		self.ui.BEliminar.clicked.connect(self.eliminarAElenco)
		self.ui.BPersonajes.clicked.connect(self.adminPersonajes)

	def adminPersonajes(self):
		self.character.exec_()

	def exec_(self):
		self.ui.message_label.setStyleSheet("color:green;")
		self.ui.message_label.setText("")
		self.updateMoviesList()
		self.updateActorsList()
		self.updateCharactersList()
		super(Elenco,self).exec_()

	def eliminarAElenco(self):
		row=row=self.ui.tabla.currentRow()
		if(row>=0):
			resp = QtGui.QMessageBox.question(self, "Eliminar actor del elenco","Desea eliminar el actor seleccionado del elenco?",QMessageBox.Yes | QMessageBox.No)
			if (resp==QtGui.QMessageBox.Yes):
				id=self.ui.tabla.item(row,0).text()
				self.dbm.removeActorCharacter(id)
				self.updateElencoList()
				self.ui.message_label.setStyleSheet("color:blue")
				self.ui.message_label.setText("Actor eliminado del elenco!")
		else:
			self.ui.message_label.setStyleSheet("color:orange")
			self.ui.message_label.setText("Seleccione primero un item de la tabla!")

			

	def agregarAElenco(self):
		self.ui.message_label.setText("")
		movie_id=self.ui.CPelicula.itemData(self.ui.CPelicula.currentIndex()).toPyObject()
		actor_id=self.ui.CActor.itemData(self.ui.CActor.currentIndex()).toPyObject()
		character_id=self.ui.CPersonaje.itemData(self.ui.CPersonaje.currentIndex()).toPyObject()
		if(self.dbm.checkElenco(actor_id,character_id,movie_id)==False):
			self.dbm.addActorCharacter(actor_id,character_id,movie_id)
			self.ui.message_label.setStyleSheet("color:green;")
			self.ui.message_label.setText("Actor-Personaje agregado correctamente al elenco!.")
			self.updateElencoList()
		else:
			self.ui.message_label.setStyleSheet("color:red;")
			self.ui.message_label.setText("Error! actor-personaje ya se encuentra en el elenco.")

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
		while self.ui.tabla.rowCount()>0:
			self.ui.tabla.removeRow(0)#elimino la primera fila (hasta que no quede ninguna)

		self.ui.tabla.setColumnCount(4)	
		self.ui.tabla.setColumnHidden(0,True)
		movie_id=self.ui.CPelicula.itemData(self.ui.CPelicula.currentIndex()).toPyObject();
		self.ui.tabla.setHorizontalHeaderLabels(QString(u"ID;Actor;Personaje;Descripción").split(";"))
		if(movie_id!=None):
			elenco=self.dbm.getElenco(movie_id)
			for e in elenco:
				self.ui.tabla.insertRow(self.ui.tabla.rowCount())

				item_id=QTableWidgetItem(str(e['id']))
				item_id.setFlags(QtCore.Qt.ItemIsEnabled)
				self.ui.tabla.setItem(self.ui.tabla.rowCount()-1,0,item_id)

				item_actor=QTableWidgetItem(str(e['actor']))
				item_actor.setFlags(QtCore.Qt.ItemIsEnabled)
				self.ui.tabla.setItem(self.ui.tabla.rowCount()-1,1,item_actor)

				item_char=QTableWidgetItem(str(e['char']))
				item_char.setFlags(QtCore.Qt.ItemIsEnabled)
				self.ui.tabla.setItem(self.ui.tabla.rowCount()-1,2,item_char)

				item_desc=QTableWidgetItem(e['desc'])
				item_desc.setFlags(QtCore.Qt.ItemIsEnabled)
				self.ui.tabla.setItem(self.ui.tabla.rowCount()-1,3,item_desc)

	def boton_listo_clicked(self):
		self.isAccepted=True;
		self.accept()