import sqlite3
import os
class Actor(object):
	def __init__(self):
		global table
		uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
		self.table="actor"
		self.id=-1;
		self.nombre=""
		self.birthday=""
		self.genero=""
		self.imagen=""
		self.conn= sqlite3.connect(uppath(__file__,2)+'/database.db')
		self.cursor=self.conn.cursor();

	#Metodos no estaticos (requieren una instancia para ser llamados)
	def setTableName(self,tname):
		self.table=tname

	def save(self):
		query="INSERT INTO "+self.table+" (nombre,birthday,genero,imagen) values ('{0}','{1}','{2}','{3}');".format(self.nombre,self.birthday,self.genero,self.imagen)
		#print query
		self.cursor.execute(query)
		self.conn.commit()
		#guardar la informacion en la base de datos
	
	#Metodos estaticos (no requieren una instancia para ser llamados)
	@staticmethod
	def getAll():
		lista=list()
		table="actor";
		uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
		conn = sqlite3.connect(uppath(__file__,2)+'/database.db')
		cursor=conn.cursor();
		query="SELECT * FROM "+table+";"
		cursor.execute(query)
		fetch=cursor.fetchall()
		conn.close()
		for f in fetch:
			tmp={}#creo un diccionario temporal vacio y lo lleno 
			tmp['id']=f[0]
			tmp['nombre']=f[1]
			tmp['birthday']=f[2]
			tmp['genero']=f[3]
			tmp['img']=f[4]
			lista.append(tmp)#agrego el diccionario temporal a la lista
		return lista

	@staticmethod
	def getWhere(param,operator,value):
		table="actor";
		lista=list()
		uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
		conn = sqlite3.connect(uppath(__file__,2)+'/database.db')
		cursor=conn.cursor();
		query="SELECT * FROM "+table+" where ["+param+"]"+operator+"'"+value+"';"
		cursor.execute(query)
		fetch=cursor.fetchall()#obtengo todos los datos
		conn.close()
		for f in fetch:
			tmp={}#creo un diccionario temporal vacio y lo lleno 
			tmp['id']=f[0]
			tmp['nombre']=f[1]
			tmp['birthday']=f[2]
			tmp['genero']=f[3]
			tmp['img']=f[4]
			lista.append(tmp)#agrego el diccionario temporal a la lista
		return lista

	@staticmethod
	def getFirstWhere(param,operator,value):
		table="actor";
		dictionary={}
		uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
		conn = sqlite3.connect(uppath(__file__,2)+'/database.db')
		cursor=conn.cursor();
		query="SELECT * FROM "+table+" where ["+param+"]"+operator+"'"+value+"';"
		cursor.execute(query)
		fetch=cursor.fetchone()
		conn.close()
		dictionary['id']=fetch[0]
		dictionary['nombre']=fetch[1]
		dictionary['birthday']=fetch[2]
		dictionary['genero']=fetch[3]
		dictionary['img']=fetch[4]
		return dictionary

	@staticmethod
	def customQuery(query):
		table="actor";
		lista=list()
		uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
		conn = sqlite3.connect(uppath(__file__,2)+'/database.db')
		cursor=conn.cursor();
		cursor.execute(query)
		fetch=cursor.fetchall()#obtengo todos los datos
		conn.commit()
		conn.close()
		return fetch

