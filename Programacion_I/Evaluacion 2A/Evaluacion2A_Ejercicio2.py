#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Evaluación 2A  - Ejercicio 2
#Escribir una clase en python que revierta una cadena de palabras

# Creo la clase Revirtir
class Revertir:
    # Defino el constructor __init__ y asigno el valor a la variable
    def __init__(self, cadena):
        self.cadena = cadena
    
    # Defino un proceso para separar la cadena en una lista usando el espacio como separador y regreso el valor
    def separacion(self):
        return " ".join(self.cadena.split(" "))
    
    # Invierto el orden de la lista y regreso el valor
    def revertir(self):
        return " ".join(self.cadena.split(" ")[::-1])

# Asigno la clase Revertir a la variable palabra con la cadena
palabra = Revertir("Universidad Nihon")

# Imprimo llamando a los metodos
print("Entrada:", palabra.separacion())
print("Salida:",palabra.revertir())