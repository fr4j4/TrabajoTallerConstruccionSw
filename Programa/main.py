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

		self.ui.tabWidget.setCurrentIndex(0)#cambiar a la primera pestaña
		
		self.actualizar_tablas();

	def signals(self):#señales de la ventana principal
		self.ui.tabla_actores.clicked.connect(self.actualiza_foto_actor)
		self.ui.tabla_directores.clicked.connect(self.actualiza_foto_director)
		self.ui.tabla_peliculas.clicked.connect(self.actualiza_foto_pelicula)
		

	def actualizar_tablas(self):
		"""	actualiza todas las tablas obteniendo
			la info del modelo "dbManager"
		"""
		self.actualizar_tabla_peliculas()
		self.actualizar_tabla_actores()
		self.actualizar_tabla_directores()

	def actualizar_tabla_peliculas(self):
		print "actualizando tabla de peliculas!"
		self.ui.tabla_peliculas.setColumnCount(4)
		self.ui.tabla_peliculas.setColumnHidden(0,True)
		self.ui.tabla_peliculas.setHorizontalHeaderLabels(QString("ID;Titulo;Pais;Estreno").split(";"))
		while self.ui.tabla_peliculas.rowCount()>0:
			self.ui.tabla_peliculas.removeRow(0)
		movies= self.dbm.getMovies()

		for mov in movies:
			self.ui.tabla_peliculas.insertRow(self.ui.tabla_peliculas.rowCount())

			item_id=QTableWidgetItem(str(mov['id']))
			item_id.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_peliculas.setItem(self.ui.tabla_peliculas.rowCount()-1,0,item_id)

			item_nombre=QTableWidgetItem(mov['name'])
			item_nombre.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_peliculas.setItem(self.ui.tabla_peliculas.rowCount()-1,1,item_nombre)

			item_pais=QTableWidgetItem(mov['country'])
			item_pais.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_peliculas.setItem(self.ui.tabla_peliculas.rowCount()-1,2,item_pais)

			item_estreno=QTableWidgetItem(mov['estreno'])
			item_estreno.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_peliculas.setItem(self.ui.tabla_peliculas.rowCount()-1,3,item_estreno)



	def actualizar_tabla_actores(self):#actualizar tabla de actores
		print "actualizando tabla de actores!"
		actors= self.dbm.getActors() #obtengo el arreglo de actores para rellenar la tabla
		#eliminar todas las filas (IMPORTANTE!)
		while self.ui.tabla_actores.rowCount()>0:
			self.ui.tabla_actores.removeRow(0)#elimino la primera fila (hasta que no quede ninguna)

		self.ui.tabla_actores.setColumnCount(4)
		self.ui.tabla_actores.setColumnHidden(0,True)#ocultar columna de ID (no es necesario que el usuario la vea)
		#dar nombre a los encabezados de la tabla
		self.ui.tabla_actores.setHorizontalHeaderLabels(QString("ID;Nombre;Nacimiento;Genero").split(";"))
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
			
			
		#print self.ui.tabla_actores.rowCount()

	def actualizar_tabla_directores(self):
		directors= self.dbm.getDirectors()
		self.ui.tabla_directores.setColumnCount(5)
		self.ui.tabla_directores.setColumnHidden(0,True)
		self.ui.tabla_directores.setHorizontalHeaderLabels(QString("ID;Nombre;Pais;Nacimiento;Muerte").split(";"))
		while self.ui.tabla_directores.rowCount()>0:
			self.ui.tabla_directores.removeRow(0)#elimino la primera fila (hasta que no quede ninguna)
		for director in directors:
			self.ui.tabla_directores.insertRow(self.ui.tabla_directores.rowCount())
			
			item_id=QTableWidgetItem(str(director['id']))
			item_id.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_directores.setItem(self.ui.tabla_directores.rowCount()-1,0,item_id)

			item_nombre=QTableWidgetItem(director['name'])
			item_nombre.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_directores.setItem(self.ui.tabla_directores.rowCount()-1,1,item_nombre)

			item_pais=QTableWidgetItem(director['country'])
			item_pais.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_directores.setItem(self.ui.tabla_directores.rowCount()-1,2,item_pais)

			item_nacimiento=QTableWidgetItem(director['birth'])
			item_nacimiento.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_directores.setItem(self.ui.tabla_directores.rowCount()-1,3,item_nacimiento)

			item_muerte=QTableWidgetItem(director['death'])
			item_muerte.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_directores.setItem(self.ui.tabla_directores.rowCount()-1,4,item_muerte)


			#falta completar

	def actualiza_foto_actor(self):
		row=self.ui.tabla_actores.currentRow()
		img=self.dbm.getActorImage(self.ui.tabla_actores.item(row,0).text())
		if(img!=""):
			pixmap = QtGui.QPixmap(img)
			self.ui.actor_image.setPixmap(pixmap)
		else:
			self.ui.actor_image.setPixmap(self.default_actor_pixmap)

	def actualiza_foto_director(self):
		row=self.ui.tabla_directores.currentRow()
		img=self.dbm.getDirectorImage(self.ui.tabla_directores.item(row,0).text())
		if(img!=""):
			pixmap = QtGui.QPixmap(img)
			self.ui.director_image.setPixmap(pixmap)
		else:
			self.ui.director_image.setPixmap(self.default_director_pixmap)


	def actualiza_foto_pelicula(self):
		row=self.ui.tabla_peliculas.currentRow()
		img=self.dbm.getMovieImage(self.ui.tabla_peliculas.item(row,0).text())
		if(img!=""):
			pixmap = QtGui.QPixmap(img)
			self.ui.pelicula_image.setPixmap(pixmap)
		else:
			self.ui.pelicula_image.setPixmap(self.default_pelicula_pixmap)

	def imprimeAlgo(self):#funcion para probar las señales (sólo imprime)
		print "Algo"

if __name__ == '__main__':
	print "Iniciando..."
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())