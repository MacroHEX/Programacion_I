#Tarea 3 Parte 2 Ejercicio 4
#Creo la clase Calculadora
class Calculadora:
    #iniciamos las variables con el metodo de __init__
    def __init__(self):
        self.x = int(input("Introduzca un primer valor: "))
        self.y = int(input("Introduzca un segundo valor: "))

    #metodo para la suma
    def suma (self):
        suma = self.x + self.y
        print("La suma de", self.x, "y", self.y, "es", suma)

    #metodo para la resta    
    def resta (self):
        resta = self.x - self.y
        print("La resta de", self.x, "y", self.y, "es", resta)

    #metodo para el producto    
    def producto (self):
        pro = self.x * self.y
        print("El producto de", self.x, "y", self.y, "es", pro)

    #metodo para la division    
    def division (self):
        div = self.x / self.y
        print("La división de", self.x, "y", self.y, "es", div)

#Asigno la variable a la clase
operacion = Calculadora()

#Realizo los metodos creados
operacion.suma()
operacion.resta()
operacion.producto()
operacion.division()