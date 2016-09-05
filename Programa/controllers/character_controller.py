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

	def exec_(self):
		self.updateCharactersList()
		super(Character,self).exec_()

	def updateCharactersList(self):
		self.ui.comboBox.clear()#vaciar el combobox
		chars=self.dbm.getCharacters()
		for char in chars:
			self.ui.comboBox.addItem(char['name'],int(char['id']))

	def aceptar(self):
		self.accept()