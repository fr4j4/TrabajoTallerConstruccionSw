#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from main_ui import Ui_MainWindow
from dbManager import dbManager
class Main(QtGui.QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.show()


if __name__ == '__main__':
	print "Iniciando..."
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())