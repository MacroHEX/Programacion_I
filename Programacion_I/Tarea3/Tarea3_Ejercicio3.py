#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 3 Ejercicio 3

# Pide al usuario que introduzca un numero entero
num = int(input("Introduzca un número: "))

#un numero es par si su resto al dividir con 2 es igual a 0
print ("El número", num, "es par.") if num%2 == 0 else print ("El número", num, "es impar.")