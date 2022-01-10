#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#EXamen Final - Ejercicio 2

# Escribir un programa que realice las siguientes acciones. 
# 1) Crea una clase llamada Punto con sus dos coordenadas X e Y. 
# 2) Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será uno. 
# 3) Sobre escribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y) 
# 4) Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X Y si X == 0 e Y == 0 está sobre el origen. 
# 5) Añade un método llamado vector, que tome otro punto Y calcule el vector resultante entre los dos puntos.

# Primer Punto
# Creo una clase llamada Punto con las variables X e Y
class Punto:
    X = int
    Y = int

    # Segundo Punto
    # Creo un metodo constructor Y si el usuario no ingresa un dato asigna automaticamente el valor 1 a la variable
    def __init__(self):
        # Introduzco valor para X
        self.X = input("Introduzca valor para X: ")
        if self.X:
            pass
        else:
            self.X = 1
        # Introduzco valor para Y
        self.Y = input("Introduzca valor para Y: ")
        if self.Y:
            pass
        else:
            self.Y = 1
    
    # Tercer punto
    # Creo el metodo string para impresion
    def sting(self):
        print ("El punto tiene las coordenadas", "(" + str(self.X) + "." + str(self.Y) + ")")

    # Cuarto punto
    # Creo el metodo cuadrante
    def cuadrante(self):
        if int(self.X)== 0 and int(self.Y) != 0:
            print ("El punto se situa sobre el eje Y")
        elif int(self.X) != 0 and int(self.Y) == 0:
            print ("El punto se situa sobre el eje X")
        elif int(self.X) == 0 and int(self.Y) == 0:
            print ("El punto se situa en el origen")

    # Quinto punto
    # Creo el metodo vector
    def vector(self):
        # Creo un punto Y
        punto_Y = Punto()
        # Realizo el calculo del vector X con direccion a Y utilizando la formula (X-Y)
        vector_X = int(self.X) - int(punto_Y.X)
        vector_Y = int(self.Y) - int(punto_Y.Y)
        # Realizo la impresión del vector
        print ("El vector entre", "(" + str(self.X) + "." + str(self.Y) + ") y (" + str(punto_Y.X) + "." + str(punto_Y.Y) + ") es", "(" + str(vector_X) + "." + str(vector_Y) + ")")


#Codigo Principal
punto_X = Punto()
punto_X.sting()
punto_X.cuadrante()
punto_X.vector()