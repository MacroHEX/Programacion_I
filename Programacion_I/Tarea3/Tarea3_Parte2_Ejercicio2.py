#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 3 Parte 2 Ejercicio 2
#inicializo la clase Persona
class Persona():
    #Creo el metodo para cargar los atributos
    def atributos(self):
        self.nombre = input("Introduzca su nombre: ")
        self.edad = int(input("Introduzca su edad: "))

    #Creo el metodo para imprimir los datos    
    def impresion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    #Creo el metodo para verificar si es mayor edad
    def es_mayor(self):
        print("Es mayor de edad.") if self.edad > 17 else print ("Es menor de edad.")

#asigno la variable a la clase Persona
persona = Persona()

#Paso la variable a inicializar los atributos
persona.atributos()


#Paso la variable para impresión
persona.impresion()


#Paso la variable para verificacion
persona.es_mayor()