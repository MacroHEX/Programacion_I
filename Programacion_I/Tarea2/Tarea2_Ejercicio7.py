#Tarea 2 Ejercicio 7
peso = float(input("Introduzca su peso en kg: "))
altura = float(input("Introduzca su altura en metros: "))
imc = peso/altura**2
print("Tu índice de masa corporal es", round(imc,2))    #round (numero, digitos)