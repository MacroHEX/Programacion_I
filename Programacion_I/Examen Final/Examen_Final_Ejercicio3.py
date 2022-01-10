#Examen Final - Ejercicio 3

# Escribir un programa que realice las siguientes acciones. 
# 1) Crea una base de datos llamada “miagendaper.py” 
# 2) Cree una tabla llamada "agenda". Debe tener los siguientes campos: apellido (texto de 30), nombre (texto de 20), domicilio (texto de 30) y teléfono (texto de 11) 
# 3) Visualice las tablas existentes para verificar la creación de "agenda" (con el comando “select”). 
# 4) Ingrese los siguientes registros: “insert into agenda (apellido, nombre, domicilio, telefono) values ('Ramirez','Alberto','Manduvira 123','4334867')”; y “insert into agenda (apellido,nombre, domicilio, telefono) values ('Garcia','Juan',' Gonzales 435','4555567'); “ 
# 5) Seleccione todos los registros de la tabla: “ select * from agenda;"

# Primer punto
# Importo la libreria sqlite3
import sqlite3
# Creo la base de datos
conn = sqlite3.connect("miagendaper.py")
# Creo el cursor
c = conn.cursor()

# Segundo punto
# Creo la tabla y utilizo try: except: para que no salte el mensaje de tabla ya existente
try:
    # Creo la tabla con los campos solicitados
    c.execute("""CREATE TABLE agenda (
        apellido VARCHAR(30),
        nombre VARCHAR(20),
        domicilio VARCHAR(30),
        teléfono VARCHAR(11)
    )""")
except:
    pass

# Tercer Punto
# Visualizo las tablas existentes utilizando el comando SELECT
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

# Cuarto Punto
# Ingreso datos utilizando el comando INSERT
c.execute("INSERT INTO agenda (apellido, nombre, domicilio, teléfono) VALUES ('Ramirez', 'Alberto', 'Manduvira 123', '4334867')")
c.execute("INSERT INTO agenda (apellido, nombre, domicilio, teléfono) VALUES ('Garcia','Juan',' Gonzales 435','4555567')")

# Quinto Punto
# Selecciono los registros de la tabla con el comando select
c.execute("SELECT * FROM agenda")
print(c.fetchall())

# Guardo y cierro la conexión
conn.commit()
conn.close()