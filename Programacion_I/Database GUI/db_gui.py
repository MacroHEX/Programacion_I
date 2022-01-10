# Importo las librerias tkinter y sqlite3
from tkinter import *
import sqlite3

# Base de datos
# Crear la base de datos o conectar a una
conn = sqlite3.connect('datos.db')

# Crear un cursor
c = conn.cursor() 

# Metodos
# Metodo para crear menú ayuda
def ayuda():
    pass

# Metodo para crear menú acerca de...

# Inicializo la interfaz grafica pasando datos para nombre de la ventana y dimension
root = Tk()
root.title('Base de Datos - Martín Medina')
root.geometry('425x400')
root.resizable(height = False, width = False)

# Creo un menú
menubar = Menu(root)
root.config(menu=menubar)

# Asigno valor al menú Archivo
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Guardar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)

# Loop infinito del GUI
root.mainloop()