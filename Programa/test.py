from models.Actor import *
from models.Director import *

#a=Actor()
#a.nombre="Francisco Gonzalez"
#a.genero="m"
#a.birthday="1992-1-10"
#a.imagen=""
#a.save()

d=Director()
d.pais="Chile"
d.nombre="Francisco"
d.genero="m"
d.fecha_nacimiento="1992-10-01"
d.save()
print(Director.getWhere('id','>=','0'))
#Director.customQuery('Delete from director where id>=8')