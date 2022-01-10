#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 3 Ejercicio 6

# \n inserta salto de pagina \t inserta una tabulacion
# imprimo un menú para mejor visualización
print("Seleccione su tipo de pizza\n\t 1- Vegetariana\n\t 2- No Vegetariana")

# pido al usuario su seleccion en formato cadena
seleccion = input("Introduzca su selección: ")

# verifica condiciones para saber si es vegetariana o no
if seleccion == "1":
    print("Ingredientes disponibles.\n\t 1- Locote \n\t 2- Albaca")
    ingredientes = input("Seleccione su ingrediente: ")
    if ingredientes == "1":
        print("Pizza vegetariana con mozzarella, tomate y locote.")
    else:
        print("Pizza vegetariana con mozzarella, tomate y albaca.")
else:
    print("Ingredientes disponibles.\n\t 1- Pepperoni \n\t 2- Jamón \n\t 3- Salmón")
    ingredientes = input("Seleccione su ingrediente: ")
    if ingredientes == "1":
        print("Pizza no vegetariana con mozzarella, tomate y pepperoni.")
    elif ingredientes == "2":
        print("Pizza no vegetariana con mozzarella, tomate y jamón.")
    else:
        print("Pizza no vegetariana con mozzarella, tomate y salmón.")