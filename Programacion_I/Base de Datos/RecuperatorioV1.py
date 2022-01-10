from tkinter import *
import sqlite3
# Me conecto a la base de datos y creo un cursor
conexion = sqlite3.connect("basededatos.db")
cursor = conexion.cursor()

# Añadir datos, editar datos, eliminar datos, consultar datos, crear tabla

# Usamos metodo try: except: para que no salte el error de la tabla ya existe
try:
    cursor.execute("""CREATE TABLE informacion (
                    nombre TEXT,
                    telf TEXT,
                    ci INT
                )""")
except:
    pass

def añadir_datos():
    # Me conecto a la base de datos
    conexion = sqlite3.connect("basededatos.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO informacion VALUES (:nombre, :telefono, :ci)",
        {
            'nombre': nombre_caja.get(),
            'telefono': telefono_caja.get(),
            'ci': ci_caja.get()
        })
    # Guardo y cierro la conexión a la base de datos
    conexion.commit()
    conexion.close()

    # Limpiar los cuadros de texto
    nombre_caja.delete(0, END)
    telefono_caja.delete(0, END)
    ci_caja.delete(0, END)

def editar_venta():

    global editar_ventana
    global nombre_caja_editar
    global telefono_caja_editar
    global ci_caja_editar
    global id_caja_editar

    # Creo la ventana usando el modulo tkinter
    editar_ventana = Tk()
    editar_ventana.title("Edición de Datos")

    # Creo las etiquetar
    nombre_etq_editar = Label(editar_ventana, text = "Nombre y Apellido")
    nombre_etq_editar.grid(row=0, column=0, padx=10, pady=10)
    telefono_etq_editar = Label(editar_ventana, text = "Teléfono")
    telefono_etq_editar.grid(row=1, column=0, padx=10, pady=10)
    ci_etq_editar = Label(editar_ventana, text = "Cédula de Identidad")
    ci_etq_editar.grid(row=2, column=0, padx=10, pady=10)
    id_etq_editar = Label(editar_ventana, text = "ID de Fila")
    id_etq_editar.grid(row=3, column=0, padx=10, pady=10)
   
    # Creo las cajas
    nombre_caja_editar = Entry(editar_ventana, width=30)
    nombre_caja_editar.grid(row=0, column=1, padx=10, pady=10)
    telefono_caja_editar = Entry(editar_ventana, width=30)
    telefono_caja_editar.grid(row=1, column=1, padx=10, pady=10)
    ci_caja_editar = Entry(editar_ventana, width=30)
    ci_caja_editar.grid(row=2, column=1, padx=10, pady=10)
    id_caja_editar = Entry(editar_ventana, width=30)
    id_caja_editar.grid(row=3, column=1, padx=10, pady=10)

    # Creo los botones
    editar_btn = Button(editar_ventana, text = "Editar", command=editar_datos)
    editar_btn.grid(row=4, column=0, columnspan=2, padx=(0,200), pady=10)
    eliminar_btn = Button(editar_ventana, text = "Eliminar", command=eliminar_datos)
    eliminar_btn.grid(row=4, column=2, columnspan=2, padx=(0,100))

def editar_datos():
    # Me conecto a la base de datos y creo un cursor
    conexion = sqlite3.connect("basededatos.db")
    cursor = conexion.cursor()

    rowid = id_caja_editar.get()

    cursor.execute('UPDATE informacion SET nombre = :nombre, telf = :telf, ci = :ci WHERE rowid=:rowid',
        {
            'nombre': nombre_caja_editar.get(),
            'telf': telefono_caja_editar.get(),
            'ci': ci_caja_editar.get(),
            'rowid': rowid
        })

    # Guardo y cierro la conexión a la base de datos
    conexion.commit()
    conexion.close()
    editar_ventana.destroy()

def consultar_datos():
    # Me conecto a la base de datos
    conexion = sqlite3.connect("basededatos.db")
    cursor = conexion.cursor()
    # Creo la ventana usando el modulo tkinter
    mostrar_ventana = Tk()
    mostrar_ventana.title("Datos")

    # usamos un cursor para almacenar la informacion en la variable datos
    cursor.execute("SELECT *, oid FROM informacion")
    datos = cursor.fetchall()
    
    # creamos las etiquetas para la impresion
    datos_etq = Label(mostrar_ventana, text="")
    datos_etq.grid(row=0, column=0, padx=10, pady=10)

    # creamos una variable tipo texto vacia
    impresion_datos = ""
    
    # Hacemos un ciclo for para imprimir las filas de la base de datos
    for dato in datos:
        impresion_datos += str(dato[0]) + " " + str(dato[1]) + " " + str(dato[2]) + "\n"

    # creamos las etiquetas para la impresion con la variable con la informacion
    datos_etq = Label(mostrar_ventana, text=impresion_datos)
    datos_etq.grid(row=0, column=0, padx=10, pady=10)    

    # Guardo y cierro la conexión a la base de datos
    conexion.commit()
    conexion.close()

def eliminar_datos():
    # Me conecto a la base de datos
    conexion = sqlite3.connect("basededatos.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM informacion WHERE oid = " + id_caja_editar.get())

    # Guardo y cierro la conexión a la base de datos
    conexion.commit()
    conexion.close()
    editar_ventana.destroy()

# Creo la ventana usando el modulo tkinter
ventana = Tk()
ventana.title("Base de Datos - Mi Nombre")
#ventana.geometry("400x300")

# Creo el menu
barramenu = Menu(ventana)
ventana.config(menu=barramenu)

# Crear lo que hay dentro de los menus
menu_archivo = Menu(barramenu, tearoff=0)
menu_archivo.add_command(label="Consulta", command=consultar_datos)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.destroy)

# Creamos los valores del menú
barramenu.add_cascade(label="Archivo", menu=menu_archivo)
barramenu.add_command(label="Editar", command=editar_venta)

# Creo las etiquetas
nombre_etq = Label(ventana, text = "Nombre y Apellido")
nombre_etq.grid(row=0, column=0, padx=10, pady=10)
telefono_etq = Label(ventana, text = "Teléfono")
telefono_etq.grid(row=1, column=0, padx=10, pady=10)
ci_etq = Label(ventana, text = "Cédula de Identidad")
ci_etq.grid(row=2, column=0, padx=10, pady=10)

# Creo las cajas
nombre_caja = Entry(ventana, width=30)
nombre_caja.grid(row=0, column=1, padx=10, pady=10)
telefono_caja = Entry(ventana, width=30)
telefono_caja.grid(row=1, column=1, padx=10, pady=10)
ci_caja = Entry(ventana, width=30)
ci_caja.grid(row=2, column=1, padx=10, pady=10)

# Creo botones
añadir_btn = Button(ventana, text = "Añadir Dato", command=añadir_datos)
añadir_btn.grid(row=3, column=0, columnspan=3)



# Guardo y cierro la conexión a la base de datos
conexion.commit()
conexion.close()

# Para que la ventana se vea
ventana.mainloop()