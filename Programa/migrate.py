import sqlite3
db1="database.db"
db2="database2.db"
conn1=sqlite3.connect(db1)
conn2=sqlite3.connect(db2)
cursor1=conn1.cursor()
cursor2=conn2.cursor()
fetch=None

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
for f in fetch:
	desc=f[4]
	name=f[3]
	query_aux='SELECT id FROM characters WHERE desc = "'+desc+'" or name = "'+name+'"'
	#print query_aux
	cursor2.execute(query_aux)
	if cursor2.fetchone()==None:
		#print cursor2.fetchone()
		query2='INSERT INTO characters (name,[desc]) values("'+name+'","'+desc+'")'
		cursor2.execute(query2)
conn2.commit()
conn1.close()
conn2.close()