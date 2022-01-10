#TP Recuperatorio

# Importo la libreria tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *

# Importo la liberia sqlite3
import sqlite3

# Creo y conecto a la base de datos
conn = sqlite3.connect("datos.db")
# Creo un cursor a la base de datos
c = conn.cursor()

# Metodo para crear la tabla
def crear_tabla():
    conn = sqlite3.connect("datos.db")
    c = conn.cursor()

    # Utilizo try: except: para que no salte el error de "Tabla ya creada" y muestre una ventana de aviso
    try:
        # Guardo las entradas como cadenas para poder tener 0 al inicio
        c.execute("""CREATE TABLE datos (
            nombre TEXT,
            telf TEXT,
            ci TEXT
        )""")
    except:
        messagebox.showwarning("Base de Datos", "Esta tabla ya existe.")

    conn.commit()
    conn.close()

# Hay que establecer la conexión a la base de datos en cada metodo
# Metodo para añadir la entrada a la tabla
def submit():
    conn = sqlite3.connect("datos.db")
    c = conn.cursor()
    try:
        # Paso valores como diccionarios de python usando las cajas como entrada
        c.execute("INSERT INTO datos VALUES (:caja_nombre, :caja_telefono, :caja_cedula)",
            {
                'caja_nombre': caja_nombre.get(),
                'caja_telefono': caja_telefono.get(),
                'caja_cedula': caja_cedula.get()
            })
        conn.commit()
        conn.close()

        #Limpio las cajas de entrada
        caja_nombre.delete(0, END)
        caja_telefono.delete(0, END)
        caja_cedula.delete(0, END)
        messagebox.showinfo("Base de Datos", "Entrada Añadida con Éxito.")
    except:
        messagebox.showwarning("Base de Datos", "No existe una tabla.\nCreela en archivo.")

# Metodo para mostrar un cuadro acerca de....
def about():
    messagebox.showinfo("Acerca de....", "Código escrito por Martín Medina.")

# Metodo para imprimir los valores
def query():
    conn = sqlite3.connect("datos.db")
    c = conn.cursor()
    try:
        c.execute("SELECT *, oid FROM datos")
        records = c.fetchall()

        query_etiqueta = Label(tab4, text='')
        query_etiqueta.grid(row=2, column=0, columnspan=2)

        print_records = ''
        for record in records:
            print_records += str(record[3]) + "\t" + str(record[0]) + "\t\t" + str(record[1]) + "\t" + str(record[2]) + "\n"
        
        query_etiqueta = Label(tab4, text=print_records)
        query_etiqueta.grid(row=2, column=0, columnspan=2)
    except:
        messagebox.showwarning("Base de Datos", "No existe una tabla.\nCreela en archivo.")

    conn.commit()
    conn.close()

# Metodo para actualizar las entradas
def update():
    conn = sqlite3.connect("datos.db")
    c = conn.cursor()
    try:
        record_id = caja_id.get()
        c.execute("""UPDATE datos SET
            nombre = :nombre,
            telf = :telf,
            ci = :ci

            WHERE oid = :oid""",
            {
            'nombre': caja_nombre2.get(),
            'telf': caja_telefono2.get(),
            'ci': caja_cedula2.get(),
            'oid': record_id
            }) 
        conn.commit()
        conn.close()
        caja_nombre2.delete(0, END)
        caja_telefono2.delete(0, END)
        caja_cedula2.delete(0, END)
        messagebox.showinfo("Base de Datos", "Entrada Actualizada con Éxito.")
    except:
        messagebox.showwarning("Base de Datos", "No existe una tabla.\nCreela en archivo.")

# Metodo para imprimir los valores para edición
def valores():
    conn = sqlite3.connect("datos.db")
    c = conn.cursor()
    try:
        record_id = caja_id.get()
        caja_nombre2.delete(0, END)
        caja_telefono2.delete(0, END)
        caja_cedula2.delete(0, END)
        c.execute("SELECT * FROM datos WHERE oid = " + record_id)
        records = c.fetchall()
        for record in records:
            caja_nombre2.insert(0, record[0])
            caja_telefono2.insert(0, record[1])
            caja_cedula2.insert(0, record[2])
    except:
        messagebox.showwarning("Base de Datos", "No existe una tabla.\nCreela en archivo.")

# Metodo para imprimir los valores para eliminar
def valores2():
    conn = sqlite3.connect("datos.db")
    c = conn.cursor()
    try:
        record_id = caja_id2.get()
        caja_nombre3.delete(0, END)
        caja_telefono3.delete(0, END)
        caja_cedula3.delete(0, END)
        c.execute("SELECT * FROM datos WHERE oid = " + record_id)
        records = c.fetchall()
        for record in records:
            caja_nombre3.insert(0, record[0])
            caja_telefono3.insert(0, record[1])
            caja_cedula3.insert(0, record[2])
    except:
        messagebox.showwarning("Base de Datos", "No existe una tabla.\nCreela en archivo.")

# Metodo para eliminar una entrada de la tabla
def delete():
    conn = sqlite3.connect("datos.db")
    c = conn.cursor()
    try:
        c.execute("DELETE FROM datos WHERE oid = " + caja_id2.get())
        conn.commit()
        conn.close()
        caja_nombre3.delete(0, END)
        caja_telefono3.delete(0, END)
        caja_cedula3.delete(0, END)
        messagebox.showinfo("Base de Datos", "Entrada Eliminada con Éxito.")
    except:
        messagebox.showwarning("Base de Datos", "No existe una tabla.\nCreela en archivo.")

# Creo la ventana principal
root = Tk()
root.title("Base de Datos - Martín Medina")
root.geometry("425x250")

# Creo un menú
menubar = Menu(root)
root.config(menu=menubar)

# Creo los valores del menú
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Crear Tabla", command=crear_tabla) # El menú llama al metodo para crear la tabla
filemenu.add_command(label="Guardar", command=conn.commit())
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.destroy)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Acerca de...", command=about)

# Creo los valores para el menú
menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Creo pestañas para facilitar la visualización
# tab1 añade datos | tab2 edita datos | tab3 elimina datos | tab4 muestra datos
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Añadir Entrada")
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Editar Entrada")
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="Eliminar Entrada")
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text="Mostrar Entradas")
tab_control.pack(expand=1, fill="both")

# Creo las etiquetas para la primera pestaña
etiqueta_nombre = Label(tab1, text="Nombre y Apellido:")
etiqueta_nombre.grid(row=0, column=0, padx=15 ,pady=5)
etiqueta_telefono = Label(tab1, text="Número de Teléfono:")
etiqueta_telefono.grid(row=1, column=0, padx=15 ,pady=5)
etiqueta_cedula = Label(tab1, text="Cédula de Identidad:")
etiqueta_cedula.grid(row=2, column=0, padx=15 ,pady=5)

# Creo las entradas para la primera pestaña
caja_nombre = Entry(tab1, width=40)
caja_nombre.grid(row=0, column=1)
caja_telefono = Entry(tab1, width=40)
caja_telefono.grid(row=1, column=1)
caja_cedula = Entry(tab1, width=40)
caja_cedula.grid(row=2, column=1)

# Creo un boton para guardar las entradas
submit_btn = Button(tab1, text="Añadir a la Tabla", command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=50)

# Creo una seleccion de ID
etiqueta_id = Label(tab2, text="Seleccione ID:")
etiqueta_id.grid(row=0, column=0, padx=15 ,pady=5)
caja_id = Entry(tab2, width=40)
caja_id.grid(row=0, column=1)
etiqueta_id2 = Label(tab3, text="Seleccione ID:")
etiqueta_id2.grid(row=0, column=0, padx=15 ,pady=5)
caja_id2 = Entry(tab3, width=40)
caja_id2.grid(row=0, column=1)

# Creo las etiquetas para la segunda pestaña
etiqueta_nombre2 = Label(tab2, text="Nombre y Apellido:")
etiqueta_nombre2.grid(row=1, column=0, padx=15 ,pady=5)
etiqueta_telefono2 = Label(tab2, text="Número de Teléfono:")
etiqueta_telefono2.grid(row=2, column=0, padx=15 ,pady=5)
etiqueta_cedula2 = Label(tab2, text="Cédula de Identidad:")
etiqueta_cedula2.grid(row=3, column=0, padx=15 ,pady=5)

# Creo las entradas para la segunda pestaña
caja_nombre2 = Entry(tab2, width=40)
caja_nombre2.grid(row=1, column=1)
caja_telefono2 = Entry(tab2, width=40)
caja_telefono2.grid(row=2, column=1)
caja_cedula2 = Entry(tab2, width=40)
caja_cedula2.grid(row=3, column=1)

# Creo las etiquetas para la tercera pestaña
etiqueta_nombre3 = Label(tab3, text="Nombre y Apellido:")
etiqueta_nombre3.grid(row=1, column=0, padx=15 ,pady=5)
etiqueta_telefono3 = Label(tab3, text="Número de Teléfono:")
etiqueta_telefono3.grid(row=2, column=0, padx=15 ,pady=5)
etiqueta_cedula3 = Label(tab3, text="Cédula de Identidad:")
etiqueta_cedula3.grid(row=3, column=0, padx=15 ,pady=5)

# Creo las entradas para la tercera pestaña
caja_nombre3 = Entry(tab3, width=40)
caja_nombre3.grid(row=1, column=1)
caja_telefono3 = Entry(tab3, width=40)
caja_telefono3.grid(row=2, column=1)
caja_cedula3 = Entry(tab3, width=40)
caja_cedula3.grid(row=3, column=1)

# Creo un boton para pedir los datos
query_btn = Button(tab4, text="Imprimir Datos", command=query)
query_btn.grid(row=0, column=0, columnspan=2, padx=125, pady=10, ipadx=50)
etiqueta_query = Label(tab4, text="           ID         Nombre y Apellido \t           Teléfono \t             Cédula")
etiqueta_query.grid(row=1, column=0, padx=0 ,pady=5)

# Creo un boton para guardar las entradas
query2_btn = Button(tab2, text="Pedir Valores", command=valores)
query2_btn.grid(row=5, column=0, columnspan=2, padx=(0,225), pady=10, ipadx=20)
submit2_btn = Button(tab2, text="Actualizar la Entrada", command=update)
submit2_btn.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=50)
query3_btn = Button(tab3, text="Pedir Valores", command=valores2)
query3_btn.grid(row=5, column=0, columnspan=2, padx=(0,225), pady=10, ipadx=20)
submit3_btn = Button(tab3, text="Eliminar la Entrada", command=delete)
submit3_btn.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=50)

# Guardo los cambios hechos a la base de datos
conn.commit()
# Cierro la conexión a la base de datos
conn.close()

# Loop de tkinter para visualizar la ventana
root.mainloop()