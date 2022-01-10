#Tarea 3 Ejercicio 9

#defino las variables de tipo float para facilitar las operaciones más adelante
inversion = float(input("Introduzca una cantidad para invertir: "))
interes_anual = float(input("Introduzca el interés anual: "))
anhos = int(input("Introduzca la cantidad de años: "))

#hago un bucle para calcular el valor final
for i in range(anhos):
    inversion *= 1 + interes_anual / 100    # *= para simplificar la operacion
    print ("Capital tras",anhos,"años es",round(inversion,2))