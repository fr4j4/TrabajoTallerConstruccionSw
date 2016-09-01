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

	def getActorImage(self,id):#obtiene la ruta de la imagen de un actor a partir de la IS
		img=""
		query='SELECT img FROM actors where id='+str(id)+";"
		self.cursor.execute(query)
		fetch=self.cursor.fetchone()
		if(fetch!=None):
			img=fetch[0]
		return img

	def getDirectorImage(self,id):#obtiene la ruta de la imagen de un actor a partir de la IS
		img=""
		query='SELECT img FROM directors where id='+str(id)+";"
		self.cursor.execute(query)
		fetch=self.cursor.fetchone()
		if(fetch!=None):
			img=fetch[0]
		return img

	def getMovieImage(self,id):#obtiene la ruta de la imagen de un actor a partir de la IS
		img=""
		query='SELECT img FROM movies where id='+str(id)+";"
		self.cursor.execute(query)
		fetch=self.cursor.fetchone()
		if(fetch!=None):
			img=fetch[0]
		return img
	
	def getDirector(self,id):
		if self.connected:
			query='SELECT * FROM directors WHERE id={0}'.format(id)
			self.cursor.execute(query)
			f=self.cursor.fetchone()
			lista ={}
			lista['id']=f[0]
			lista['name']=unicode(f[1])
			lista['country']=f[2].encode('utf-8')
			lista['birth']=f[3].encode('utf-8')
			lista['death']=f[4].encode('utf-8')
			lista['img']=f[5].encode('utf-8')
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getActors(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM actors'
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=unicode(f[1])
				tmp['birth']=f[2].encode('utf-8')
				tmp['genre']=f[3].encode('utf-8')
				tmp['img']=f[4].encode('utf-8')
				tmp['num_pelis']=f[5]
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
				tmp['name']=unicode(f[1])
				tmp['country']=unicode(f[2])
				tmp['birth']=f[3].encode('utf-8')
				tmp['death']=f[4].encode('utf-8')
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
				tmp['id_actor']=f[1].encode('utf-8')
				tmp['id_pelicula']=f[2].encode('utf-8')
				tmp['personaje']=unicode(f[3])
				tmp['descripcion']=unicode(f[4])
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getMovies(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM movies'
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=unicode(f[1])
				tmp['desc']=unicode(f[2])
				tmp['estreno']=f[3].encode('utf-8')
				tmp['country']=unicode(f[4])
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def checkLogin(self,user,pwd):
		b=False
		query="SELECT count(usuario) from login where usuario= '{0}' and pass= '{1}'".format(user,pwd)
		self.cursor.execute(query)
		fetch=self.cursor.fetchone()
		b=fetch[0]==1
		return b

	def getMoviesByActor(self,actor_id):#filtrar la busqueda por id del actor
		if self.connected:
			lista=list()
			query='select movies.* from movies join actor_character where  movies.id=actor_character.movie_id and actor_character.actor_id='+str(actor_id)
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=unicode(f[1])
				tmp['desc']=unicode(f[2])
				tmp['estreno']=f[3].encode('utf-8')
				tmp['country']=unicode(f[4])
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getActorsByMovie(self,movie_id):#filtrar la busqueda por id del actor
		if self.connected:
			lista=list()
			query='select actors.* from actors join actor_character where  actor_character.actor_id=actors.id and actor_character.movie_id='+str(movie_id)
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=unicode(f[1])
				tmp['birth']=f[2].encode('utf-8')
				tmp['genre']=f[3].encode('utf-8')
				tmp['img']=f[4].encode('utf-8')
				tmp['num_pelis']=f[5]
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getMovieDescription(self,id):
		desc=""
		query='SELECT desc FROM movies where id='+str(id)+";"
		self.cursor.execute(query)
		fetch=self.cursor.fetchone()
		if(fetch!=None):
			desc=fetch[0]
		return desc


	def addDirector(self,nombre,pais,fnac,fdef,img):
		query="INSERT INTO directors (name,country,birth,death,img)  VALUES ('{0}','{1}','{2}','{3}','{4}')".format(nombre,pais,fnac,fdef,img)
		#print query
		self.cursor.execute(query)
		self.conn.commit()

	def updateDirector(self,id,nombre,pais,fnac,fdef,img):
		query="UPDATE directors set name='{0}',country='{1}',birth='{2}',death='{3}',img='{4}' WHERE id={5}".format(nombre,pais,fnac,fdef,img,id)
		#print query
		self.cursor.execute(query)
		self.conn.commit()

