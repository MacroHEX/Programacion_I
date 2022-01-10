#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 4 Ejercicio 5

# Importo la libreria sqlite3
import sqlite3

# Me conecto a la base de datos
db = sqlite3.connect("teléfonos.db")
print ("Conexión exitosa.")

# Creo un cursor
c = db.cursor()

# Llamamos a la base de datos utilizando SELECT y ordenando por nombre
c.execute("SELECT * FROM mistelefono ORDER BY nombre")

# Almaceno la informacion de la tabla en la variable
items = c.fetchall()

# Impresion con formato
print ("Nombre " + "\t\t\tTeléfono")
print ("——————————————————————————————————")
# Imprimo las entradas añadiendo un 0 al numero para visualizacion
for item in items:
    print(str(item[0]) + " \t\t " + "0" + str(item[1]))

# Guardo los cambios
db.commit()

# Cierro la conexión
db.close()