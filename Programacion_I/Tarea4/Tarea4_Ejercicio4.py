#Tarea 4 Ejercicio 4

# Importo la libreria sqlite3
import sqlite3

# Me conecto a la base de datos
db = sqlite3.connect("teléfonos.db")
# Imprimo un mensaje para verificar que el codigo se ejecuto
print ("Conexión exitosa.")

# Creo un cursor
c = db.cursor()

# Creo una lista con datos para pasar a la tabla
datos_familia = [   ('Loida Ainoa', 972578176),
                    ('Jessica Damián', 982996795),
                    ('Osvaldo Toni', 971251950),
                ]

# Añado varios datos a la tabla desde la lista datos_familia
c.executemany("INSERT INTO mistelefono VALUES(?,?)", datos_familia)
# Imprimo un mensaje para verificar que el codigo se ejecuto
print ("Datos añadidos con exito")

# Guardo los cambios
db.commit()

# Cierro la conexión
db.close()