#Tarea 4 Ejercicio 6

# Importo la libreria sqlite3
import sqlite3

# Me conecto a la base de datos
db = sqlite3.connect("teléfonos.db")
print ("Conexión exitosa.")

# Creo un cursor
c = db.cursor()

# Actualizo los registros utilizando la id de la fila
c.execute("UPDATE mistelefono SET teléfono = 982386665 WHERE teléfono = 972254105")        

# Llamamos a la base de datos utilizando SELECT y ordenando por nombre
c.execute("SELECT * FROM mistelefono ORDER BY nombre")

# Imprimo la tabla con formato
items = c.fetchall()
print ("Nombre " + "\t\t\tTeléfono")
print ("——————————————————————————————————")
for item in items:
    print(str(item[0]) + " \t\t " + "0" + str(item[1]))

# Guardo los cambios
db.commit()

# Cierro la conexión
db.close()