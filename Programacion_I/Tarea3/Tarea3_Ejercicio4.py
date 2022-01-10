#Tarea 3 Ejercicio 4

#defino las variables como int para facilitar la operacion
edad = int(input("Introduzca su edad: "))
ingresos = int(input("Introduzca sus ingresos (en guaranies): "))

#pregunto si las condiciones se cumplen
if edad > 17 and ingresos >= 7000000:
    print ("Debe tributar.")
else:
    print ("No debe tributar.")