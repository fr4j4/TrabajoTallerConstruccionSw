#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3
db1="data.db"
#db2="new.db"
conn1=sqlite3.connect(db1)
#conn2=sqlite3.connect(db2)
cursor1=conn1.cursor()
#cursor2=conn2.cursor()
fetch=None

"""
#migrar actores
query='SELECT * FROM actor'
cursor1.execute(query)
fetch=cursor1.fetchall()
cursor2.execute("DELETE FROM actors")
conn2.commit()
for f in fetch:
	query2="INSERT INTO actors (name,birth,genre,img) values('{0}','{1}','{2}','')".format(f[1],f[2],f[3],f[4])
	#print query2
	cursor2.execute(query2)

#migrar peliculas
query='SELECT * FROM pelicula'
cursor1.execute(query)
fetch=cursor1.fetchall()
cursor2.execute("DELETE FROM movies")
conn2.commit()
for f in fetch:
	desc=f[4]
	name=f[1]
	estreno=f[2]
	country=f[3]
	query2='INSERT INTO movies (name,[desc],estreno,country) values("'+name+'","'+desc+'","'+estreno+'","'+country+'")'#.format(f[1],f[4],f[2],f[3])
	cursor2.execute(query2)

#migrar personajes
query='SELECT * FROM elenco'
cursor1.execute(query)
fetch=cursor1.fetchall()
cursor2.execute("DELETE FROM characters")
conn2.commit()
for f in fetch:alter table directors add column img
	desc=f[4]
	name=f[3]
	query_aux='SELECT id FROM charactalter table directors add column imgers WHERE desc = "'+desc+'" or name = "'+name+'"'
	#print query_aux
	cursor2.execute(query_aux)
	if cursor2.fetchone()==None:
		#print cursor2.fetchone()
		query2='INSERT INTO characters (name,[desc]) values("'+name+'","'+desc+'")'
		cursor2.execute(query2)
"""
#migrar directores
"""
query='SELECT * FROM director'
cursor1.execute(query)
fetch=cursor1.fetchall()
cursor2.execute("DELETE FROM directors")
conn2.commit()
for f in fetch:
	name=f[1].encode('utf-8')
	country=str(f[2]).encode('utf-8')
	birth=str(f[3]).encode('utf-8')
	death=str(f[4]).encode('utf-8')
	if(death=="None"):
		death=""
	query2="INSERT INTO directors (name,country,birth,death,img) values('{0}','{1}','{2}','{3}','')".format(name,country,birth,death)
	print query2
	cursor2.execute(query2)
conn2.commit()
conn1.close()
conn2.close()
"""
for i in range(5,40):
	query = 'UPDATE actors SET img="images/actores/{0}.jpg" WHERE id={0};'.format(i)
	print query
	cursor1.execute(query)
	conn1.commit()
conn1.close()