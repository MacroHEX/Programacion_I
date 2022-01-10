#Tarea 4 Ejercicio 2

# Importo la libreria sqlite3
import sqlite3

# Me conecto a la base de datos
db = sqlite3.connect("teléfonos.db")
# Imprimo un mensaje para verificar que el codigo se ejecuto
print ("Conexión exitosa.")

# Creo un cursor
c = db.cursor()

# Creo una tabla llamada mistelefono con los campos nombre y teléfono uso try para que no salte el error si ya existe
try:
    c.execute("""CREATE TABLE mistelefono (
    nombre text,
    teléfono int
    )""")
    # Imprimo un mensaje para verificar que el codigo se ejecuto
    print ("Tabla creada con exito.")
except:
    print("La tabla ya existe")

# Guardo los cambios
db.commit()

# Cierro la conexión
db.close()