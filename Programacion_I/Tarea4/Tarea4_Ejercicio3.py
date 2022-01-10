#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 4 Ejercicio 3

# Importo la libreria sqlite3
import sqlite3

# Me conecto a la base de datos
db = sqlite3.connect("teléfonos.db")
# Imprimo un mensaje para verificar que el codigo se ejecuto
print ("Conexión exitosa.")

# Creo un cursor
c = db.cursor()

# Añado un dato a la tabla
c.execute("INSERT INTO mistelefono VALUES ('Martin Medina', 972254105)")
# Imprimo un mensaje para verificar que el codigo se ejecuto
print ("Datos añadidos con exito")

# Guardo los cambios
db.commit()

# Cierro la conexión
db.close()