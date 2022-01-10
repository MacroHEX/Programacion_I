#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 3 Ejercicio 2

# Pido al usuario dos numeros enteros
n1 = int(input("Introduzca el dividendo: "))
n2 = int(input("Introduzca el divisor: "))

# Si el divisor es 0 manda un mensaje de error
if n2==0:
    print("Error, no se puede dividir por 0.")
else:
    print(n1/n2)