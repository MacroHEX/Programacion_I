# Importo las librerias tkinter y sqlite3
from tkinter import *
from tkinter import messagebox
import sqlite3

# Inicializo la interfaz grafica pasando datos para nombre de la ventana y dimension
root = Tk()
root.title('Base de Datos')
root.geometry('425x400')
root.resizable(height = False, width = False)

# Base de datos
# Crear la base de datos o conectar a una
conn = sqlite3.connect('datos.db')

# Crear un cursor
c = conn.cursor() 

# Crear la funcion para crear la tabla
def crear_tabla():
    # Conecto a la base de datos
    conn = sqlite3.connect('datos.db')

    # Crear un cursor
    c = conn.cursor() 

    # Utilizo try: except: para que no de el error de tabla ya creada e imprime una advertencia por tkinter   
    try:
       c.execute("""CREATE TABLE datos (
            nombre TEXT,
            telf INT,
            ci INT
            )""")
    except:
        messagebox.showwarning("Base de Datos", "Esta tabla ya existe")
    
    # Guarda cambios
    conn.commit()
    # Cerrar conexión
    conn.close()

# Crear la funcion para cargar a la base
def submit():
    # Conecto a la base de datos
    conn = sqlite3.connect('datos.db')

    # Crear un cursor
    c = conn.cursor() 

    # Insertar datos a la tabla
    c.execute("INSERT INTO datos VALUES (:box_name, :box_telf, :box_ci)",
       {
            'box_name': box_name.get(),
            'box_telf': box_telf.get(),
            'box_ci' : box_ci.get()
        })

    # Guarda cambios
    conn.commit()
    # Cerrar conexión
    conn.close()    

    # Limpiamos las cajas de texto
    box_name.delete(0, END)
    box_telf.delete(0, END)
    box_ci.delete(0, END)

# Crear una funcion para borrar una entrada
def delete():
    # Conecto a la base de datos
    conn = sqlite3.connect('datos.db')

    # Crear un cursor
    c = conn.cursor() 

    # Borrar una entrada
    c.execute("DELETE FROM datos WHERE oid = " + box_sel.get())

    # Guarda cambios
    conn.commit()
    # Cerrar conexión
    conn.close()    

# Crear una funcion para actualizar las entradas
def update():
    # Conecto a la base de datos
    conn = sqlite3.connect('datos.db')
    # Crear un cursor
    c = conn.cursor() 

    record_id = box_sel.get()
    # Actualizo los campos en la tabla datos utilizando un diccionario de python
    c.execute("""UPDATE datos SET
        nombre = :nombre,
        telf = :telf,
        ci = :ci

        WHERE oid = :oid""",
        {
        'nombre': box_name_editor.get(),
        'telf': box_telf_editor.get(),
        'ci': box_ci_editor.get(),
        'oid': record_id
        }) 
        
    # Guarda cambios
    conn.commit()
    # Cerrar conexión
    conn.close()
    # Cierro la ventana
    editor.destroy()

# Crear una funcion para editar las entradas
def edit():
    global editor
    editor = Tk()
    editor.title('Edición de Entrada')
    editor.geometry('430x200')
    editor.resizable(height = False, width = False)   

    # Conecto a la base de datos
    conn = sqlite3.connect('datos.db')

    # Crear un cursor
    c = conn.cursor() 

    # Crear variables globales para los nombres de las cajas
    global box_name_editor
    global box_telf_editor
    global box_ci_editor

    # Crear cajas de texto
    box_name_editor = Entry(editor, width=40)
    box_name_editor.grid(row=1, column=1, padx=20)
    box_telf_editor = Entry(editor, width=40)
    box_telf_editor.grid(row=2, column=1)
    box_ci_editor = Entry(editor, width=40)
    box_ci_editor.grid(row=3, column=1) 

    # Crear etiquetas de texto
    lbl_nombre = Label(editor, text="Nombre y Apellido")
    lbl_nombre.grid(row=1, column=0, padx=15)
    lbl_telf = Label(editor, text="Número de Teléfono")
    lbl_telf.grid(row=2, column=0, padx=15)
    lbl_ci = Label(editor, text="Cédula de Identidad")
    lbl_ci.grid(row=3, column=0, padx=15)

    record_id = box_sel.get()
    # Llamar a la base de datos
    c.execute("SELECT * FROM datos WHERE oid = " + record_id)
    records = c.fetchall()

    # Crear un boton para guardar lo actualizado
    edit_btn = Button(editor, text="Actualizar Entrada", command=update)
    edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

    # Loop en resultados
    for record in records:
        box_name_editor.insert(0, record[0])
        box_telf_editor.insert(0, record[1])
        box_ci_editor.insert(0, record[2])

    # Guarda cambios
    conn.commit()
    # Cerrar conexión
    conn.close()       

# Crear la funcion de llamada
def query():
    # Conecto a la base de datos
    conn = sqlite3.connect('datos.db')

    # Crear un cursor
    c = conn.cursor() 

    # Llamar a la base de datos
    c.execute("SELECT *, oid FROM datos")
    records = c.fetchall()
    # print(records) # Impresion para probar en consola

    # Impresion de la llamada
    print_records = ''
    for record in records:
        print_records += str(record[3]) + "\t" + str(record[0]) + "\t\t" + str(record[1]) + "\t\t" + str(record[2]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    # Guarda cambios
    conn.commit()
    # Cerrar conexión
    conn.close()

# Creo la función para el menú acerca de
def about():
    messagebox.showinfo("Acerca de...", "Código escrito por Martin Medina")

# Crear cajas de texto
box_name = Entry(root, width=40)
box_name.grid(row=1, column=1, padx=20)
box_telf = Entry(root, width=40)
box_telf.grid(row=2, column=1)
box_ci = Entry(root, width=40)
box_ci.grid(row=3, column=1) 
box_sel = Entry(root, width=40)
box_sel.grid(row=8, column=1, pady=5)

# Crear etiquetas de texto
lbl_nombre = Label(root, text="Nombre y Apellido")
lbl_nombre.grid(row=1, column=0, padx=15)
lbl_telf = Label(root, text="Número de Teléfono")
lbl_telf.grid(row=2, column=0, padx=15)
lbl_ci = Label(root, text="Cédula de Identidad")
lbl_ci.grid(row=3, column=0, padx=15)
lbl_sel = Label(root, text="Seleccionar ID")
lbl_sel.grid(row=8, column=0, pady=5)

# Crear un boton para crear la tabla
# table_btn = Button(root, text="Crear Tabla", command=crear_tabla)
# table_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=80)

# Crear un submit button
submit_btn = Button(root, text="Añadir una Entrada a la Base de Datos", command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=70)

# Crear un boton de llamada
query_btn = Button(root, text="Mostrar Entradas", command=query)
query_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Crear un boton para eliminar
del_btn = Button(root, text="Eliminar Entrada", command=delete)
del_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=126)

# Crear un boton para actualizar las entradas
edit_btn = Button(root, text="Editar Entrada", command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=133)

# Creo un menú
menubar = Menu(root)
root.config(menu=menubar)

# Asigno valor al menú Archivo
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Crear Tabla", command=crear_tabla)
filemenu.add_command(label="Guardar", command=conn.commit())
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Añadir Entrada", command=submit)
editmenu.add_command(label="Editar Entrada")
editmenu.add_command(label="Eliminar Entrada")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_command(label="Acerca de...", command=about)

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Guarda cambios
conn.commit()

# Cerrar conexión
conn.close()

# Loop infinito del GUI
root.mainloop()