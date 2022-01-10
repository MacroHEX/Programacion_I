#Tarea 3 Parte 2 Ejercicio 3
#Creo la clase Triangulo
class Triangulo():
    #Creo el metodo para inicializar los datos
    def inicializar(self):
        self.a = input("Introduzca el primer lado del triangulo: ")
        self.b = input("Introduzca el segundo lado del triangulo: ")
        self.c = input("Introduzca el tercer lado del triangulo: ")

    #Creo el metodo para definir el lado mayor
    def mayor(self):
        if self.a > self.b and self.a > self.c:
            print("El primer lado es el mayor.")
        elif self.b > self.a and self.b > self.c:
            print("El segundo lado es el mayor.")
        elif self.c > self.a and self.c > self.b:
            print("El tercer lado es el mayor.")
        else:
            print("Todos los lados son iguales.")

    #Creo el metodo para definir el tipo de triangulo basado en sus lados
    def tipo(self):
        if self.a == self.b and self.b == self.c:
            print("El triangulo es equilatero")
        elif self.a != self.b and self.a != self.c:
            print("El triangulo es escaleno")
        else:
            print("El triangulo es isosceles.")

#Asigno la variable a la clase
triangulo = Triangulo()

#Inicializo la variable
triangulo.inicializar()

#Verifico el/los lado(s) mayor(es)
triangulo.mayor()

#Verifico el tipo de triangulo del que se trata
triangulo.tipo()