from dbManager import *

dbm=dbManager('database.db')
dbm.connect()
dbm.close()
var=dbm.getPeliculas()
print var