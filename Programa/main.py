#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main_ui import Ui_MainWindow
from dbManager import dbManager
class Main(QtGui.QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		print("Qt version:", QtCore.QT_VERSION_STR)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self) 
		self.init();
		self.show()

	def init(self):#procedimientos de inicialización (ejecutar al inicio)
		self.dbm=dbManager("data.db")
		self.dbm.connect()

		self.default_actor_pixmap = QtGui.QPixmap(('images/default_person.png'))
		self.default_director_pixmap = QtGui.QPixmap(('images/default_person.png'))
		self.default_pelicula_pixmap = QtGui.QPixmap(('images/default_movie.jpg'))
		
		self.ui.actor_image.setPixmap(self.default_actor_pixmap)
		self.ui.director_image.setPixmap(self.default_director_pixmap)
		self.ui.pelicula_image.setPixmap(self.default_pelicula_pixmap)
		
		self.signals()

		self.ui.tabWidget.setCurrentIndex(1)#cambiar a la primera pestaña
		
		self.actualizar_tablas();

	def signals(self):#señales de la ventana principal
		self.ui.tabla_actores.clicked.connect(self.actualiza_foto_actor)
		

	def actualizar_tablas(self):
		"""	actualiza todas las tablas obteniendo
			la info del modelo "dbManager"
		"""
		self.actualizar_tabla_peliculas()
		self.actualizar_tabla_actores()
		self.actualizar_tabla_directores()

	def actualizar_tabla_peliculas(self):
		print "actualizando tabla de peliculas!"

	def actualizar_tabla_actores(self):#actualizar tabla de actores
		print "actualizando tabla de actores!"
		actors= self.dbm.getActors() #obtengo el arreglo de actores para rellenar la tabla
		#eliminar todas las filas (IMPORTANTE!)
		while self.ui.tabla_actores.rowCount()>0:
			self.ui.tabla_actores.removeRow(0)#elimino la primera fila (hasta que no quede ninguna)

		self.ui.tabla_actores.setColumnCount(4)
		self.ui.tabla_actores.setColumnHidden(0,True)#ocultar columna de ID (no es necesario que el usuario la vea)
		#dar nombre a los encabezados de la tabla
		self.ui.tabla_actores.setHorizontalHeaderLabels(QString("ID 1;Nombre;Fecha nacimiento;Genero").split(";"))
		#insertar nuevamente todas las filas
		for actor in actors:
			self.ui.tabla_actores.insertRow(self.ui.tabla_actores.rowCount())#inserto una fila vacía

			item_id=QTableWidgetItem(str(actor['id']))#creo un item y le asigno la id como valor
			item_id.setFlags(QtCore.Qt.ItemIsEnabled)#hago que el item no se pueda editar
			self.ui.tabla_actores.setItem(self.ui.tabla_actores.rowCount()-1,0,item_id)

			item_nombre=QTableWidgetItem(str(actor['name']))#creo un item y le asigno la id como valor
			item_nombre.setFlags(QtCore.Qt.ItemIsEnabled)#hago que el item no se pueda editar
			self.ui.tabla_actores.setItem(self.ui.tabla_actores.rowCount()-1,1,item_nombre)

			item_cumple=QTableWidgetItem(str(actor['birth']))#creo un item y le asigno la id como valor
			item_cumple.setFlags(QtCore.Qt.ItemIsEnabled)#hago que el item no se pueda editar
			self.ui.tabla_actores.setItem(self.ui.tabla_actores.rowCount()-1,2,item_cumple)

			item_genero=QTableWidgetItem(str(actor['genre']).upper())#creo un item y le asigno la id como valor
			item_genero.setFlags(QtCore.Qt.ItemIsEnabled)#hago que el item no se pueda editar
			self.ui.tabla_actores.setItem(self.ui.tabla_actores.rowCount()-1,3,item_genero)
			
			
		print self.ui.tabla_actores.rowCount()


	def actualizar_tabla_directores(self):
		actors= self.dbm.getDirectors()
		while self.ui.tabla_actores.rowCount()>0:
			self.ui.tabla_actores.removeRow(0)#elimino la primera fila (hasta que no quede ninguna)

		print "actualizando tabla de directores!"

	def actualiza_foto_actor(self):
		row=self.ui.tabla_actores.currentRow()
		img=self.dbm.getActorImage(self.ui.tabla_actores.item(row,0).text())
		print img
		if(img!=""):
			pixmap = QtGui.QPixmap(img)
			self.ui.actor_image.setPixmap(pixmap)
		else:
			self.ui.actor_image.setPixmap(self.default_actor_pixmap)


	def imprimeAlgo(self):#funcion para probar las señales (sólo imprime)
		print "Algo"

if __name__ == '__main__':
	print "Iniciando..."
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())