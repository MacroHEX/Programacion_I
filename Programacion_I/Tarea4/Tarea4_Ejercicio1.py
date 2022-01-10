#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 4 Ejercicio 1

# Importo la libreria sqlite3
import sqlite3

# Creo la base de datos si no existe, si existe me conecto
base_datos = sqlite3.connect("teléfonos.db")

# Imprimo un mensaje para verificar que el codigo se ejecuto
print ("Base de datos creada.")