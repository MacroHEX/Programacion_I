#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 3 Ejercicio 5

#defino a la variable como integer para facilitar la verificacion
cliente = int(input("Introduzca su edad: "))

#compruebo las condiciones para la entrada
if cliente < 4:
    print("Puede entrar gratuitamente.")
elif cliente <= 18:
    print("La entrada tiene un costo de 5.000gs")
else:
    print("La entrada tiene un costo de 10.000gs")