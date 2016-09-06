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

	def getMovie(self,id):
		if self.connected:
			query='SELECT * FROM movies WHERE id={0}'.format(id)
			self.cursor.execute(query)
			f=self.cursor.fetchone()
			lista ={}
			lista['id']=f[0]
			lista['name']=unicode(f[1])
			lista['desc']=unicode(f[2])
			lista['estreno']=f[3]
			lista['country']=unicode(f[4])
			lista['img']=unicode(f[5])
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getActor(self,id):
		if self.connected:
			query='SELECT * FROM actors WHERE id={0}'.format(id)
			self.cursor.execute(query)
			f=self.cursor.fetchone()
			lista ={}
			lista['id']=f[0]
			lista['name']=unicode(f[1])
			lista['birth']=f[2].encode('utf-8')
			lista['genre']=f[3].encode('utf-8')
			lista['img']=f[4].encode('utf-8')
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"	

	def getActors(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM actors '+" ORDER BY name ASC"
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=unicode(f[1])
				tmp['birth']=f[2].encode('utf-8')
				tmp['genre']=f[3].encode('utf-8')
				tmp['img']=f[4].encode('utf-8')
				tmp['num_pelis']= self.getTotalMovies(tmp['id'])
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getTotalMovies(self,actor_id):
		if self.connected:
			lista=list()
			query = 'SELECT COUNT(movie_id) as NPeliculas FROM actor_character WHERE actor_id =' + str(actor_id)
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}
				tmp['num_pelis']=f[0]
				return tmp['num_pelis']
			
	def getDirectors(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM directors'+" ORDER BY name ASC"
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
			query='SELECT * FROM characters ORDER BY name'
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=f[1].encode('utf-8')
				tmp['desc']=f[2].encode('utf-8')
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getCharacter(self,id):
		if self.connected:
			query='SELECT * FROM characters WHERE id={0}'.format(id)
			self.cursor.execute(query)
			f=self.cursor.fetchone()
			lista ={}
			lista['id']=f[0]
			lista['name']=unicode(f[1])
			lista['desc']=unicode(f[2])
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"	

	def addCharacter(self,name,desc):
		query="INSERT INTO characters (name,desc) VALUES('{0}','{1}')".format(name.toUtf8(),desc.toUtf8())
		#print query
		self.cursor.execute(query)
		self.conn.commit()

	def updateCharacter(self,name,desc,id):
		query="UPDATE characters SET name = '{0}', desc= '{1}' WHERE id={2}".format(name.toUtf8(),desc.toUtf8(),id)
		#print query
		self.cursor.execute(query)
		self.conn.commit()

	def deleteCharacter(self,id):
		query ="DELETE FROM characters WHERE id ={0}".format(id)
		self.cursor.execute(query)
		self.conn.commit()

	def getElenco(self,id):
		if self.connected:
			lista=list()
			query='SELECT actor_character.id,actors.name,characters.name,characters.desc FROM actor_character join actors join characters where movie_id= {0} and actor_id=actors.id and characters.id=character_id;'.format(id)
			#print query
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}
				tmp['id']=f[0]
				tmp['actor']=f[1]
				tmp['char']=f[2]
				tmp['desc']=f[3]
				lista.append(tmp)
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getMovies(self):
		if self.connected:
			lista=list()
			query='SELECT * FROM movies '+" ORDER BY name ASC"
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=unicode(f[1])
				tmp['desc']=unicode(f[2])
				tmp['estreno']=f[3].encode('utf-8')
				tmp['country']=unicode(f[4])
				tmp['num_actors']= self.getTotalActorsByMovie(tmp['id'])
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getTotalActorsByMovie(self,movie_id):
		if self.connected:
			lista=list()
			query = 'SELECT COUNT(actor_id) FROM actor_character WHERE movie_id ='+str(movie_id)
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}
				tmp['num_actors']=f[0]
				return tmp['num_actors']

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
			query='select movies.* from movies join actor_character where  movies.id=actor_character.movie_id and actor_character.actor_id='+str(actor_id)+" ORDER BY name ASC"
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=unicode(f[1])
				tmp['desc']=unicode(f[2])
				tmp['estreno']=f[3].encode('utf-8')
				tmp['country']=unicode(f[4])
				tmp['num_actors']= self.getTotalActorsByMovie(tmp['id'])
				lista.append(tmp)#agrego el diccionario temporal a la lista
			return lista
		else:
			print "No puede solicitar datos si no esta conectado a una base de datos"

	def getActorsByMovie(self,movie_id):#filtrar la busqueda por id de la pelicula
		if self.connected:
			lista=list()
			query='select actors.* from actors join actor_character where  actor_character.actor_id=actors.id and actor_character.movie_id='+str(movie_id)+" ORDER BY name ASC"
			self.cursor.execute(query)
			fetch=self.cursor.fetchall()
			for f in fetch:
				tmp={}#creo un diccionario temporal vacio y lo lleno 
				tmp['id']=f[0]
				tmp['name']=unicode(f[1])
				tmp['birth']=f[2].encode('utf-8')
				tmp['genre']=f[3].encode('utf-8')
				tmp['img']=f[4].encode('utf-8')
				tmp['num_pelis']= self.getTotalMovies(tmp['id'])
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

	def deleteDirector(self,id):
		query="DELETE FROM directors where id = {0} ;".format(id)
		#print query
		self.cursor.execute(query)
		self.conn.commit()

	def addMovie(self,nombre,descr,estreno,pais,img):
		query="INSERT INTO movies (name,desc,estreno,country,img)  VALUES ('{0}','{1}','{2}','{3}','{4}')".format(nombre,descr,estreno,pais,img)
		#print query
		self.cursor.execute(query)
		self.conn.commit()

	def updateMovie(self,id,nombre,descr,estreno,pais,img):
		query="UPDATE movies set name='{0}', desc='{1}', country='{2}', img='{3}',estreno='{4}' WHERE id={5}".format(nombre,descr.toUtf8().replace('\'','\"'),pais,img,estreno,id)
		#print query
		self.cursor.execute(query)
		self.conn.commit()

	def deleteMovie(self,id):
		query="DELETE FROM movies where id = {0} ;".format(id)
		#print query
		self.cursor.execute(query)
		self.conn.commit()

	def addActor(self,name,birth,genre,img):
		query="INSERT INTO actors (name,birth,genre,img)  VALUES ('{0}','{1}','{2}','{3}');".format(name,birth,genre,img)
		#print query
		self.cursor.execute(query)
		self.conn.commit()
	
	def updateActor(self,id,nombre,fnac, genero, img):
		query="UPDATE actors set name='{0}',birth='{1}',genre='{2}',img='{3}' WHERE id={4}".format(nombre,fnac,genero,img,id)
		#print query
		self.cursor.execute(query)
		self.conn.commit()

	def deleteActor(self,id):
		query="DELETE FROM actors where id = {0} ;".format(id)
		#print query
		self.cursor.execute(query)
		self.conn.commit()	

	def addActorCharacter(self,a_id,c_id,m_id):
		query="INSERT INTO actor_character (actor_id,character_id,movie_id) VALUES ({0},{1},{2});".format(a_id,c_id,m_id)		
		#print query
		self.cursor.execute(query)
		self.conn.commit()

	def removeActorCharacter(self,id):
		query ="DELETE FROM actor_character WHERE id={0};".format(id)
		self.cursor.execute(query)
		self.conn.commit()

	def checkElenco(self,a_id,c_id,m_id):#true si existe el registro, false si no existe
		b=True 
		query="SELECT COUNT(*) FROM actor_character WHERE actor_id={0} and character_id={1} and movie_id={2}".format(a_id,c_id,m_id)
		self.cursor.execute(query)
		fetch=self.cursor.fetchone()
		#print "count: "+str(fetch[0])
		if(fetch[0]==0):
			b=False
		return b
