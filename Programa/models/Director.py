import sqlite3
import os
class Director(object):

	def __init__(self):
		global table
		uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
		self.table="director"
		self.id=-1;
		self.nombre=""
		self.pais=""
		self.fecha_nacimiento=""
		self.fecha_defuncion=""
		self.conn= sqlite3.connect(uppath(__file__,2)+'/database.db')
		self.cursor=self.conn.cursor();
	#Metodos no estaticos (requieren una instancia para ser llamados)
	def setTableName(self,tname):
		self.table=tname

	def save(self):
		query="INSERT INTO "+self.table+" (nombre,pais,fecha_nacimiento,fecha_defuncion) values ('{0}','{1}','{2}','{3}');".format(self.nombre,self.pais,self.fecha_nacimiento,self.fecha_defuncion)
		#print query
		self.cursor.execute(query)
		self.conn.commit()
		#guardar la informacion en la base de datos

	@staticmethod
	def getAll():
		lista=list()
		table="director";
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
			tmp['pais']=f[2]
			tmp['fecha_nacimiento']=f[3]
			tmp['fecha_defuncion']=f[4]
			lista.append(tmp)#agrego el diccionario temporal a la lista
		return lista

	@staticmethod
	def getWhere(param,operator,value):
		table="director";
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
			tmp['pais']=f[2]
			tmp['fecha_nacimiento']=f[3]
			tmp['fecha_defuncion']=f[4]
			lista.append(tmp)#agrego el diccionario temporal a la lista
		return lista

	@staticmethod
	def getFirstWhere(param,operator,value):
		table="director";
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
		dictionary['pais']=fetch[2]
		dictionary['fecha_nacimiento']=fetch[3]
		dictionary['fecha_defuncion']=fetch[4]
		return dictionary

	@staticmethod
	def customQuery(query):
		table="director";
		lista=list()
		uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
		conn = sqlite3.connect(uppath(__file__,2)+'/database.db')
		cursor=conn.cursor();
		cursor.execute(query)
		fetch=cursor.fetchall()#obtengo todos los datos
		conn.commit()
		conn.close()
		return fetch