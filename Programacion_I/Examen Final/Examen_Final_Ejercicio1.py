#Examen Final - Ejercicio 1

# Escribir un programa que realice las siguientes acciones. 
# 1) Almacene una cadena de caracteres ingresada por teclado en una variable. 
# 2) Muestre por pantalla el contenido de la variable. 
# 3) Cuente cuantos caracteres tiene la cadena almacenada en la variable y muéstrelos por pantalla. 
# 4) Deletree el contenido de lo almacenado en la variable. 
# 5) Ingrese 5 valores por teclado en 5 variables distintas. 
# 6) Muestre por pantalla el contenido de cada una de las variables , y utilizando el comando correspondiente el tipo de dato que contiene cada una.

# Primer punto
# Creo una variable que almacene datos ingresados por teclado
cadena = input("Introduzca algo: ")

# Segundo punto
# Imprimo el contenido de la variable cadena
print ("La variable contiene esta información:", cadena)

# Tercer punto
# Cuento cuantos caracteres contiene la variable utilizando la funcion len y lo muestro en pantalla
print ('"' + cadena + '"', "contiene", len(cadena), "caracteres")

# Cuarto punto
# Utilizo un ciclo para imprimir la cadena deletreada
for letras in cadena:
    print(letras)

# Quinto punto
# Creo 5 variables que pidan entrada por teclado
a = input("Introduzca un dato: ")
b = input("Introduzca un dato: ")
c = input("Introduzca un dato: ")
d = input("Introduzca un dato: ")
e = input("Introduzca un dato: ")

# Sexto punto
# Imprimo las 5 variables junto a su tipo
print("La primera variable contiene el valor:", a)
print ("El tipo de dato de la primera variable es", type(a))

print("La segunda variable contiene el valor:", b)
print ("El tipo de dato de la segunda variable es", type(b))

print("La tercera variable contiene el valor:", c)
print ("El tipo de dato de la tercera variable es", type(c))

print("La cuarta variable contiene el valor:", d)
print ("El tipo de dato de la cuarta variable es", type(d))

print("La quinta variable contiene el valor:", e)
print ("El tipo de dato de la quinta variable es", type(e))