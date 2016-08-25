import sqlite3
import os
#Codigo para accesar a la base de datos
class dbManager(object):
	def __init__(self,dbName):
		uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
		self.dbName=uppath(__file__,1)+'/'+dbName
		self.connected=False
	
	def connect(self):
		self.conn= sqlite3.connect(self.dbName)
		self.cursor=self.conn.cursor();
		self.connected=True

	def close(self):
		self.conn.close()
		self.connected=False

	def getActors(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM actors'
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=f[1]
				tmp['birth']=f[2]
				tmp['genre']=f[3]
				tmp['img']=f[4]
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getDirectors(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM directors'
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=f[1]
				tmp['country']=f[2]
				tmp['birth']=f[3]
				tmp['death']=f[4]
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getCharacters(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM characters'
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['id_actor']=f[1]
				tmp['id_pelicula']=f[2]
				tmp['personaje']=f[3]
				tmp['descripcion']=f[4]
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getMovies(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM pelicula'
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=f[1]
				tmp['desc']=f[2]
				tmp['estreno']=f[3]
				tmp['country']=f[4]
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

