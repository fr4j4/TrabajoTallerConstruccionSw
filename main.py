#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main_ui import Ui_MainWindow
from controllers.login_controller import Login
from controllers.director_controller import Director 
from controllers.actor_controller import Actor 
from controllers.movie_controller import Pelicula
from controllers.elenco_controller import Elenco
from dbManager import dbManager

class Main(QtGui.QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		print("Qt version:", QtCore.QT_VERSION_STR)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.login=Login()
		self.director=Director()
		self.actor=Actor()
		self.pelicula=Pelicula()
		self.elenco=Elenco()
		self.init()
		#si los datos de login no corresponden, se mstrará denuevo la ventana de login
		
		self.login.exec_()#ejecutamos el login
		#mientras los datos de login sean erroneos, se consultará nuevamente
		while self.dbm.checkLogin(self.login.getUser(),self.login.getPwd())==False:
			if self.login.isAccepted()==False:
				break
			self.login.setErrorMessage("Datos no registrados!")
			self.login.exec_()
		
		#si se presiono "ingresar"...
		if self.login.isAccepted():
			self.show()
		else:
			#si se presiono "salir"..
			sys.exit(0)
		
		


	def init(self):#procedimientos de inicialización (ejecutar al inicio)
		self.dbm=dbManager("data.db")
		self.dbm.connect()

		self.default_actor_pixmap = QtGui.QPixmap(('images/default_person.png'))
		self.default_director_pixmap = QtGui.QPixmap(('images/default_person.png'))
		self.default_pelicula_pixmap = QtGui.QPixmap(('images/default_movie.jpg'))
		
		self.ui.actor_image.setPixmap(self.default_actor_pixmap)
		self.ui.director_image.setPixmap(self.default_director_pixmap)
		self.ui.pelicula_image.setPixmap(self.default_pelicula_pixmap)
		
		self.ui.actor_filter_comboBox.setEnabled(False)
		self.ui.movie_filter_comboBox.setEnabled(False)


		self.signals()

		self.ui.tabWidget.setCurrentIndex(0)#cambiar a la primera pestaña
		self.actualizar_tablas();

	def signals(self):#señales de la ventana principal
		self.ui.pushButton.clicked.connect(self.showElenco)

		self.ui.tabla_actores.clicked.connect(self.tabla_actores_clicked)
		self.ui.tabla_directores.clicked.connect(self.tabla_directores_clicked)
		self.ui.tabla_peliculas.clicked.connect(self.tabla_peliculas_clicked)
		
		self.ui.actor_filter_comboBox.currentIndexChanged.connect(self.actor_combobox_clicked)
		self.ui.movie_filter_comboBox.currentIndexChanged.connect(self.movie_combobox_clicked)

		self.ui.filter_actor_checkBox.stateChanged.connect(self.actor_filter_checkBox_clicked)
		self.ui.filter_pelicula_checkBox.stateChanged.connect(self.pelicula_filter_checkBox_clicked)
	
		self.ui.BNuevo_3.clicked.connect(self.nuevo_director)
		self.ui.BEditar_3.clicked.connect(self.editar_director)
		self.ui.BEliminar_3.clicked.connect(self.eliminar_director)

		self.ui.tabla_directores.doubleClicked.connect(self.editar_director)
		self.ui.tabla_peliculas.doubleClicked.connect(self.editar_pelicula)
		self.ui.tabla_actores.doubleClicked.connect(self.editar_actor)

		#relacionado con actores
		self.ui.BNuevo_2.clicked.connect(self.nuevo_actor)
		self.ui.BEditar_2.clicked.connect(self.editar_actor)
		self.ui.BEliminar_2.clicked.connect(self.eliminar_actor)

		#Señales para peliculas!!!
		self.ui.BNuevo.clicked.connect(self.nueva_pelicula)
		self.ui.BEditar.clicked.connect(self.editar_pelicula)
		self.ui.BEliminar.clicked.connect(self.eliminar_pelicula)

	def actualizar_tablas(self):
		"""	actualiza todas las tablas obteniendo
			la info del modelo "dbManager"
		"""
		self.actualizar_tabla_peliculas()
		self.actualizar_tabla_actores()
		self.actualizar_tabla_directores()

		self.actualiza_combobox_actores()
		self.actualiza_combobox_peliculas()

	def showElenco(self):
		self.elenco.exec_()
		self.actualizar_tablas()

	def actualizar_tabla_peliculas(self,filter=False):
		#print "actualizando tabla de peliculas!"

		self.ui.pelicula_image.setPixmap(self.default_pelicula_pixmap)
		self.ui.pelicula_name_label.setText('');

		self.ui.tabla_peliculas.setColumnCount(5)
		self.ui.tabla_peliculas.setColumnHidden(0,True)
		self.ui.tabla_peliculas.setHorizontalHeaderLabels(QString("ID;Titulo;Pais;Estreno;N. Actores").split(";"))
		while self.ui.tabla_peliculas.rowCount()>0:
			self.ui.tabla_peliculas.removeRow(0)
		
		movies=None
		if(filter==False):
			movies=self.dbm.getMovies()
		else:
			#obtengo la id del actor para hacer la búsqieda con filtro
			actor_id=self.ui.actor_filter_comboBox.itemData(self.ui.actor_filter_comboBox.currentIndex()).toPyObject()
			#actor_id=0
			movies=self.dbm.getMoviesByActor(actor_id)

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

			item_numActors=QTableWidgetItem(str(mov['num_actors']))
			item_numActors.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_peliculas.setItem(self.ui.tabla_peliculas.rowCount()-1,4,item_numActors)

	def actualizar_tabla_actores(self,filter=False):#actualizar tabla de actores
		#print "actualizando tabla de actores!"
		self.ui.actor_image.setPixmap(self.default_actor_pixmap)
		self.ui.actor_name_label.setText('');
		#eliminar todas las filas (IMPORTANTE!)
		while self.ui.tabla_actores.rowCount()>0:
			self.ui.tabla_actores.removeRow(0)#elimino la primera fila (hasta que no quede ninguna)

		actors= None

		if(filter==False):#si NO debo filtrar por películas...
			actors=self.dbm.getActors()#obtengo el arreglo de actores para rellenar la tabla
		else:#en caso de filtrar por películas
			#obtengo la id del actor para hacer la búsqieda con filtro
			movie_id=self.ui.movie_filter_comboBox.itemData(self.ui.movie_filter_comboBox.currentIndex()).toPyObject()
			actors=self.dbm.getActorsByMovie(movie_id)

		self.ui.tabla_actores.setColumnCount(5)
		self.ui.tabla_actores.setColumnHidden(0,True)#ocultar columna de ID (no es necesario que el usuario la vea)
		#dar nombre a los encabezados de la tabla
		self.ui.tabla_actores.setHorizontalHeaderLabels(QString("ID;Nombre;Nacimiento;Genero;N. Peliculas").split(";"))
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

			
			item_numPelis=QTableWidgetItem(str(actor['num_pelis']))
			item_numPelis.setFlags(QtCore.Qt.ItemIsEnabled)
			self.ui.tabla_actores.setItem(self.ui.tabla_actores.rowCount()-1,4,item_numPelis)
			

	def actualizar_tabla_directores(self):
		self.ui.director_image.setPixmap(self.default_director_pixmap)
		self.ui.director_name_label.setText('');

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

	def actualiza_combobox_actores(self):
		self.ui.actor_filter_comboBox.clear()#vaciar el combobox
		actors=self.dbm.getActors()
		for actor in actors:
			self.ui.actor_filter_comboBox.addItem(actor[u'name'],int(actor['id']))

	def actualiza_combobox_peliculas(self):
		self.ui.movie_filter_comboBox.clear()#vaciar el combobox
		movies=self.dbm.getMovies()
		for mov in movies:
			self.ui.movie_filter_comboBox.addItem(mov[u'name'],int(mov['id']))	

	def actualiza_foto_actor(self,id):
		img=self.dbm.getActorImage(id)
		if(img!=""):
			pixmap = QtGui.QPixmap(img)
			self.ui.actor_image.setPixmap(pixmap)
		else:
			self.ui.actor_image.setPixmap(self.default_actor_pixmap)

	def actualiza_foto_director(self,id):
		img=self.dbm.getDirectorImage(id)
		if(img!=""):
			pixmap = QtGui.QPixmap(img)
			self.ui.director_image.setPixmap(pixmap)
		else:
			self.ui.director_image.setPixmap(self.default_director_pixmap)

	def actualiza_foto_pelicula(self,id):
		img=self.dbm.getMovieImage(id)
		if(img!=""):
			pixmap = QtGui.QPixmap(img)
			self.ui.pelicula_image.setPixmap(pixmap)
		else:
			self.ui.pelicula_image.setPixmap(self.default_pelicula_pixmap)

	def tabla_directores_clicked(self):
		row=self.ui.tabla_directores.currentRow()
		id=self.ui.tabla_directores.item(row,0).text()
		name=self.ui.tabla_directores.item(row,1).text()
		self.ui.director_name_label.setText(name);
		self.actualiza_foto_director(id)

	def tabla_peliculas_clicked(self):
		row=self.ui.tabla_peliculas.currentRow()
		id=self.ui.tabla_peliculas.item(row,0).text()
		name=self.ui.tabla_peliculas.item(row,1).text()
		self.ui.pelicula_name_label.setText(name);
		self.actualiza_foto_pelicula(id)
		self.actualiza_descripcion_pelicula(id)
	
	def tabla_actores_clicked(self):
		row=self.ui.tabla_actores.currentRow()
		id=self.ui.tabla_actores.item(row,0).text()
		name=self.ui.tabla_actores.item(row,1).text()
		self.ui.actor_name_label.setText( name );
		self.actualiza_foto_actor(id)

	def actor_combobox_clicked(self,actor_id):
		if(self.ui.filter_actor_checkBox.isChecked()):#si el checkbox esta marcado, filtrar
			self.actualizar_tabla_peliculas(filter=True)

	def movie_combobox_clicked(self,movie_id):
		if(self.ui.filter_pelicula_checkBox.isChecked()):
			self.actualizar_tabla_actores(filter=True)

	def actor_filter_checkBox_clicked(self):
		if(self.ui.filter_actor_checkBox.isChecked()):
			self.ui.actor_filter_comboBox.setEnabled(True)
			self.actualizar_tabla_peliculas(filter=True);
		else:
			self.ui.actor_filter_comboBox.setEnabled(False)
			self.actualizar_tabla_peliculas()

	def pelicula_filter_checkBox_clicked(self):
		if(self.ui.filter_pelicula_checkBox.isChecked()):
			self.ui.movie_filter_comboBox.setEnabled(True)
			self.actualizar_tabla_actores(filter=True);
		else:
			self.ui.movie_filter_comboBox.setEnabled(False)
			self.actualizar_tabla_actores()

	def actualiza_descripcion_pelicula(self,id):
		self.ui.pelicula_description_text.setText("");
		desc=self.dbm.getMovieDescription(id)
		self.ui.pelicula_description_text.setText(desc);

	def nuevo_director(self):
		self.director.setTitle("Agregar nuevo director")
		self.director.clearData()
		self.director.exec_()
		if(self.director.accepted() and self.director.validaData()):
			print "agregar_director"
			fecha_defuncion=self.director.getData('fdef')
			if(self.director.isDead()==False):
				fecha_defuncion=""
			self.dbm.addDirector(self.director.getData('nombre'),self.director.getData('pais'),self.director.getData('fnac'),fecha_defuncion,self.director.getData('img'))
			self.actualizar_tablas()

	def editar_director(self):
		row=self.ui.tabla_directores.currentRow()
		if(row>=0):
			self.director.clearData()
			id=self.ui.tabla_directores.item(row,0).text()
			dir=self.dbm.getDirector(id)
			print dir['name']
			self.director.putData('nombre',dir['name'])
			self.director.putData('fnac',dir['birth'])
			self.director.putData('fdef',dir['death'])
			self.director.putData('pais',dir['country'])
			self.director.putData('img',dir['img'])
			self.director.setTitle("Editar director")
			self.director.exec_()

			defuncion=self.director.getData('fdef')
			if(self.director.isDead()==False):
				defuncion=""

			if(self.director.accepted() and self.director.validaData()):
				self.dbm.updateDirector(id,self.director.getData('nombre'),self.director.getData('pais'),self.director.getData('fnac'),defuncion,self.director.getData('img'))
				self.actualizar_tablas()

	def eliminar_director(self):
		row=self.ui.tabla_directores.currentRow()
		if row>=0:
		 	resp = QtGui.QMessageBox.question(self, "Eliminar director","Desea eliminar el director seleccionado?",QMessageBox.Yes | QMessageBox.No)
			if (resp==QtGui.QMessageBox.Yes):
				print "borrar"
				id=self.ui.tabla_directores.item(row,0).text()
				self.dbm.deleteDirector(id)
				self.actualizar_tablas()

	def nuevo_actor(self):
		self.actor.setTitle("Agregar nuevo actor")
		self.actor.clearData()
		self.actor.exec_()
		if(self.actor.accepted()and self.actor.validaData()):
			self.dbm.addActor(self.actor.getData('nombre'),self.actor.getData('fnac'),self.actor.getData('genero'),self.actor.getData('img'))
			self.actualizar_tablas()
	#nuevo
	def editar_actor(self):
		row=self.ui.tabla_actores.currentRow()
		if(row>=0):
			self.actor.clearData()
			id=self.ui.tabla_actores.item(row,0).text()
			dir=self.dbm.getActor(id)
			print dir['name']
			self.actor.putData('nombre',dir['name'])
			self.actor.putData('fnac',dir['birth'])
			self.actor.putData('genero',dir['genre'])
			self.actor.putData('img',dir['img'])
			self.actor.setTitle("Editar actor")
			self.actor.exec_()

			if(self.actor.accepted()and self.actor.validaData()):
				self.dbm.updateActor(id,self.actor.getData('nombre'),self.actor.getData('fnac'),self.actor.getData('genero'),self.actor.getData('img'))
				self.actualizar_tablas()

	def eliminar_actor(self):
		row=self.ui.tabla_actores.currentRow()
		if row>=0:
		 	resp = QtGui.QMessageBox.question(self, "Eliminar actor","Desea eliminar el actor seleccionado?",QMessageBox.Yes | QMessageBox.No)
			if (resp==QtGui.QMessageBox.Yes):
				print "borrar"
				id=self.ui.tabla_actores.item(row,0).text()
				self.dbm.deleteActor(id)
				self.actualizar_tablas()
	def printSomething(self):
		print "something"

	def nueva_pelicula(self):
		self.pelicula.setTitle("Agregar nueva pelicula")
		self.pelicula.clearData()
		self.pelicula.exec_()
		if(self.pelicula.accepted() and self.pelicula.validaData()):
			self.dbm.addMovie(self.pelicula.getData('nombre'),self.pelicula.getData('descripcion'),self.pelicula.getData('estreno'),self.pelicula.getData('pais'),self.pelicula.getData('img'))
			self.actualizar_tablas()
	
	def editar_pelicula(self):
		row=self.ui.tabla_peliculas.currentRow()
		if(row>=0):
			self.pelicula.clearData()
			id=self.ui.tabla_peliculas.item(row,0).text()
			dir=self.dbm.getMovie(id)
			print dir['name']
			self.pelicula.putData('nombre',dir['name'])
			self.pelicula.putData('descripcion',dir['desc'])
			self.pelicula.putData('estreno',dir['estreno'])
			self.pelicula.putData('pais',dir['country'])
			self.pelicula.putData('img',dir['img'])
			self.pelicula.setTitle("Editar pelicula")
			self.pelicula.exec_()

			if(self.pelicula.accepted() and self.pelicula.validaData()):
				self.dbm.updateMovie(id,self.pelicula.getData('nombre'),self.pelicula.getData('descripcion'),self.pelicula.getData('estreno'),self.pelicula.getData('pais'),self.pelicula.getData('img'))
				self.actualizar_tablas()
				print self.pelicula.getData('img')

	def eliminar_pelicula(self):
		row=self.ui.tabla_peliculas.currentRow()
		if row>=0:
		 	resp = QtGui.QMessageBox.question(self, "Eliminar pelicula","Desea eliminar la pelicula seleccionada?",QMessageBox.Yes | QMessageBox.No)
			if (resp==QtGui.QMessageBox.Yes):
				print "borrar"
				id=self.ui.tabla_peliculas.item(row,0).text()
				self.dbm.deleteMovie(id)
				self.actualizar_tablas()

if __name__ == '__main__':
	print "Iniciando..."
	app = QtGui.QApplication(sys.argv)
	main = Main()
	sys.exit(app.exec_())