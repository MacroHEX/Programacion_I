#Evaluación 2B  - Ejercicio 1

# Importo las librerias tkinter para la interfaz grafica y sqlite3 para la base de datos
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import sqlite3

# Realizo la conexión a la base de datos y creo el cursor
conn = sqlite3.connect("inventario.db")
c = conn.cursor()

# Creo la tabla y utilizo try: except: para que no salte el mensaje de tabla ya existente
try:
        # Creo la tabla con los campos de mes, ventas y gastos
        c.execute("""CREATE TABLE datos (
            mes TEXT,
            ventas INT,
            gastos INT
        )""")
except:
    pass

# Creo el metodo para añadir datos a la tabla
def add_datos():
    # Siempre realizo la conexión a la base de datos dentro de los metodos
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()

    # Paso valores como diccionarios de python usando las cajas como entrada
    c.execute("INSERT INTO datos VALUES (:mes, :ventas, :gastos)",
        {
            'mes': lista_desplegable.get(),
            'ventas': ventas_box.get(),
            'gastos': gastos_box.get()
        })
    
    # Guardo y cierro la conexión
    conn.commit()
    conn.close()

    # Limpio las cajas de entrada
    lista_desplegable.set("Seleccione Mes")
    ventas_box.delete(0, END)
    gastos_box.delete(0, END)
    # Muestro un mensaje de que se añadieron los datos con exito
    messagebox.showinfo("Base de Datos", "Entrada Añadida con Éxito.")

# Metodo para llamar datos
def inventario():
    # Siempre realizo la conexión a la base de datos dentro de los metodos
    conn = sqlite3.connect("inventario.db")
    c = conn.cursor()
    
    # Creo una nueva ventana para la visualización
    inv = Tk()
    inv.title("Inventario - MacroHEX")
    inv.geometry("350x250")
    inv.resizable(height = False, width = False)
    
    # Utilizo el cursor para seleccionar todos los datos de la tabla
    c.execute("SELECT *, oid FROM datos")
    records = c.fetchall()

    # Creo etiquetas para las categorias
    categorias_lbl = Label(inv, text="\tMes\t   Ventas\t\t Gastos", font=("Helvetica 10 bold"))
    categorias_lbl.grid(row=0, column=0, padx=10 ,pady=15)
    record_lbl = Label(inv, text='')
    record_lbl.grid(row=1, column=0, columnspan=2)

    # Creo una variable para almacenar lo impreso
    print_records = ''

    # Hago un ciclo para imprimir
    for record in records:
        print_records += "\t" + str(record[0]) + "\t\t" + str(record[1]) + "\t\t" + str(record[2]) + "\n"
    
    # Asigno la variable a una etiqueta
    record_lbl = Label(inv, text=print_records)
    record_lbl.grid(row=1, column=0, columnspan=2)

    # Guardo y cierro la conexión
    conn.commit()
    conn.close()

# Metodo para mostrar un cuadro acerca de....
def about():
    messagebox.showinfo("Acerca de....", "Código escrito por MacroHEX.\nEvaluación 2B - Ejercicio I")

# Creo mi ventana principal nombrandola root y bloqueo el redimensionamiento
root = Tk()
root.title("Inventario - MacroHEX")
root.geometry("200x250")
root.resizable(height = False, width = False)

# Creo un menú
menubar = Menu(root)
root.config(menu=menubar)

# Creo los valores del menú desplegable
# Menu Archivo
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Mostrar Inventario", command=inventario) 
filemenu.add_command(label="Guardar", command=conn.commit())
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.destroy)

# Menu Ayuda
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Acerca de...", command=about)

# Creo los valores para el menú superior
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Creo etiquetas para la ventana
mes_lbl = Label(root, text="Mes")
mes_lbl.grid(row=0, column=0, padx=10, pady=5)
ventas_lbl = Label(root, text="Ventas")
ventas_lbl.grid(row=2, column=0, padx=10, pady=5)
gastos_lbl = Label(root, text="Gastos")
gastos_lbl.grid(row=4, column=0, padx=10, pady=5)

# Creo las cajas para introducir información
ventas_box = Entry(root, width=20)
ventas_box.grid(row=3, column=0, padx=10, pady=5)
gastos_box = Entry(root, width=20)
gastos_box.grid(row=5, column=0, padx=10, pady=5)

# Creo los botones
subir_btn = Button(root, text="Añadir Dato del Mes", command=add_datos)
subir_btn.grid(row=6, column=0, columnspan=2, pady=10, ipadx=5)

# Creo una lista desplegable para los meses
lista_desplegable = ttk.Combobox(root, width=20, state="readonly")
lista_desplegable.grid(row=1, column=0, padx=20)
lista_desplegable.set("Seleccione Mes")

# Creo las opciones para la lista
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
lista_desplegable["values"]=meses

# Guardo y cierro la conexión a la base de datos
conn.commit()
conn.close()

# Loop de tkinter para visualizar la ventana
root.mainloop()