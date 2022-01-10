#Tarea 3 Parte 2 Ejercicio 7
#Creo la clase Cuenta
class Cuenta:
    #Inicializo con el metodo __init__
    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    #Metodo para impresion de los datos
    def impresion(self):
        print("Titular", self.titular)
        print("Capital:", self.cantidad)

#Creo que la clase PlazoFijo heredada de Cuenta 
class PlazoFijo(Cuenta):
    #Inicializo con el metodo __init__
    def __init__(self, titular, cantidad, plazo, interes):
        #Llamo a los valores de la clase padre Cuenta
        super().__init__(titular, cantidad)
        self.plazo = plazo
        self.interes = interes

    #Metodo para calcular el interes
    def calculo_interes(self):
        ganancia=self.cantidad*self.interes/100
        print("El interes es:", ganancia)

    #Metodo para la impresión
    def impresion(self):
        print("Plazo Fijo")
        super().impresion()
        print("Plazo disponible:", self.plazo)
        print("Interés:", self.interes)
        self.calculo_interes()

# Creo la clase CajaAhorro heredada de Cuenta
class CajaAhorro(Cuenta):
    #Inicializo con el metodo __init__
    def __init__(self, titular, cantidad):
        super().__init__(titular, cantidad)

    #Metodo para la impresión
    def impresion(self):
        print("Caja Ahorro")
        super().impresion()


#Asigno un valor a la variable caja con la clase CajaAhorro
caja=CajaAhorro("Martin", 5000)
#Llamo al metodo de impresión
caja.impresion()


#Asigno un valor a la variable caja con la clase PlazoFijo
plazo=PlazoFijo("David", 8000, 365, 1.2)
#Llamo al metodo de impresión
plazo.impresion()