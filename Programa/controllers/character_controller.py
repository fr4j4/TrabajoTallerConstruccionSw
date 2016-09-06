#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from views.chars_ui import Ui_Dialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from dbManager import dbManager

class Character(QtGui.QDialog):
	def __init__(self):
		super(Character, self).__init__()
		self.ui=Ui_Dialog()
		self.ui.setupUi	(self)
		self.dbm=dbManager("data.db")
		self.dbm.connect()
		self.signals()

	def signals(self):
		self.ui.BCerrar.clicked.connect(self.aceptar)
		self.ui.comboBox.currentIndexChanged.connect(self.comboboxChanged)
		self.ui.BGuardar.clicked.connect(self.BGuardar_clicked)
		self.ui.BEliminar.clicked.connect(self.deleteCharacter)

	def exec_(self):
		self.updateCharactersList()
		#self.clearData()
		super(Character,self).exec_()

	def updateCharactersList(self):
		self.ui.comboBox.clear()#vaciar el combobox
		chars=self.dbm.getCharacters()
		for char in chars:
			self.ui.comboBox.addItem(char['name'],int(char['id']))

	def aceptar(self):
		self.accept()

	def comboboxChanged(self):
		self.updateData()
	
	def updateData(self):
		if self.ui.comboBox.currentIndex()>=0:
			id=self.ui.comboBox.itemData(self.ui.comboBox.currentIndex()).toPyObject()
			ch=self.dbm.getCharacter(id)
			self.ui.in_nombre.setText(ch['name'])
			self.ui.in_descripcion.setText(ch['desc'])

	def clearData(self):
		self.ui.in_nombre.setText('')
		self.ui.in_descripcion.setText('')

	def BGuardar_clicked(self):
		if self.validaData():
			if(self.ui.check_new.isChecked()):
				self.addCharacter()
			else:
				self.updateCharacter()
			self.clearData()
			self.updateCharactersList()

	def addCharacter(self):
		#print "addNew"
		self.dbm.addCharacter(self.ui.in_nombre.text().trimmed(),self.ui.in_descripcion.toPlainText().trimmed())

	def updateCharacter(self):
		#print "update"
		id=self.ui.comboBox.itemData(self.ui.comboBox.currentIndex()).toPyObject()
		self.dbm.updateCharacter(self.ui.in_nombre.text().trimmed(),self.ui.in_descripcion.toPlainText().trimmed(),id)

	def deleteCharacter(self):
		resp = QtGui.QMessageBox.question(self, "Eliminar personaje","Desea eliminar el personaje seleccionado?",QMessageBox.Yes | QMessageBox.No)
		if (resp==QtGui.QMessageBox.Yes):
			id=self.ui.comboBox.itemData(self.ui.comboBox.currentIndex()).toPyObject()
			self.dbm.deleteCharacter(id)
			self.updateCharactersList()
			
	def validaData(self):
		b=True
		if(len(self.ui.in_nombre.text().trimmed())==0 or len(self.ui.in_descripcion.toPlainText().trimmed())==0):
			b=False
		return b