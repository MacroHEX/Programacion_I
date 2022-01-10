#Tarea 2 Ejercicio 9
PAYASOS_PESO = 112          #constante
MUNHECAS_PESO = 75
payasos = int(input("Introduce el número de payasos del envio: "))
munhecas = int(input("Introduce el número de muñecas del envio: "))
peso_total = PAYASOS_PESO * payasos + MUNHECAS_PESO * munhecas
print("El peso total del paquete es", peso_total)