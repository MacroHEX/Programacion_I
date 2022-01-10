#Tarea 3 Parte 2 Ejercicio 1
#inicializamos la clase
class Alumno:                                           
    #defino atributos
    def inicializar(self):                
        self.nombre = input("Introduzca nombre: ")     
        self.nota = int(input ("Introduzca nota: "))
    #metodo para impresion
    def impresion(self):                  
        print("El alumno", self.nombre, "tiene una nota de", self.nota)
        self.aprueba()
    #metodo para verificar nota
    def aprueba(self):                            
        if self.nota > 1:
            print ("El alumno aprueba.")
        else:
            print ("El alumno no aprueba.")

#asigno la variable a la clase Alumno
alumno = Alumno()

#inicializo los atributos
alumno.inicializar()

#impresion y verificacion de resultados
alumno.impresion()