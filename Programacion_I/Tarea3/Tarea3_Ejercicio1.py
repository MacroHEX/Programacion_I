#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 3 Ejercicio 1

# Almaceno la cadena "contraseña" en la variable pass
pas = "contraseña"

# Pido al usuario una entrada
pass_input = input("Introduzca su contraseña: ")

# Pregunto si la contraseña coincide con la almacenada en minusculas
if pas == pass_input.lower():
    print ("La contraseña coincide")
else:
    print ("La contraseña no coincide")