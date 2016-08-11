import sqlite3
import os
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

	def getActores(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM actor'
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
						tmp={}#creo un diccionario temporal vacio y lo lleno 
						tmp['id']=f[0]
						tmp['nombre']=f[1]
						tmp['birthday']=f[2]
						tmp['genero']=f[3]
						tmp['img']=f[4]
						lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getDirectores(self):
			if self.connected:
				lista=list()
				query='SELECT * FROM director'
				self.cursor.execute(query)
				fetch=self.cursor.fetchall()
				for f in fetch:
							tmp={}#creo un diccionario temporal vacio y lo lleno 
							tmp['id']=f[0]
							tmp['nombre']=f[1]
							tmp['pais']=f[2]
							tmp['fecha_nacimiento']=f[3]
							tmp['fecha_defuncion']=f[4]
							lista.append(tmp)#agrego el diccionario temporal a la lista
				return lista
			else:
				print "No puede solicitar datos si no esta conectado a una base de datos"

	def getElencos(self):
			if self.connected:
				lista=list()
				query='SELECT * FROM elenco'
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

	def getPeliculas(self):
				if self.connected:
					lista=list()
					query='SELECT * FROM pelicula'
					self.cursor.execute(query)
					fetch=self.cursor.fetchall()
					for f in fetch:
								tmp={}#creo un diccionario temporal vacio y lo lleno 
								tmp['id']=f[0]
								tmp['nombre']=f[1]
								tmp['estreno']=f[2]
								tmp['pais']=f[3]
								tmp['descripcion']=f[4]
								lista.append(tmp)#agrego el diccionario temporal a la lista
					return lista
				else:
					print "No puede solicitar datos si no esta conectado a una base de datos"

