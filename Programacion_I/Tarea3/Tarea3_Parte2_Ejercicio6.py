#Tarea 3 Parte 2 Ejercicio 6
#creo la clase Banco
class Banco:
    #inicializo las variables
    def __init__(self):
        self.cliente1 = Cliente()
        self.cliente2 = Cliente()
        self.cliente3 = Cliente()
    
    #metodo para las operaciones
    def operar(self):
        self.cliente1.depositar()
        self.cliente2.depositar()
        self.cliente3.depositar()
        self.cliente1.extraer()
        self.cliente2.extraer()
        self.cliente3.extraer()

    #metodo para visualizar los depositos totales
    def deposito_total(self):
        total = self.cliente1.mostrar_total()+self.cliente2.mostrar_total()+self.cliente3.mostrar_total()
        print ("El total de dinero en el banco es:",total)

#creo la clase Cliente
class Cliente:
    #inicializamos
    def __init__(self):
        self.nombre = input("Introduzca el nombre del cliente: ")
        self.cantidad = int((input("Introduzca monto inicial: ")))

    #suma el valor en cantidad
    def depositar(self):
        print("Bienvenido",self.nombre)
        cantidad = float(input("Introduzca monto a depositar: "))
        self.cantidad+=cantidad

    #resta el valor en cantidad
    def extraer(self):        
        print("Bienvenido",self.nombre)
        cantidad = float(input("Introduzca monto a extraer: "))
        self.cantidad-=cantidad

    #pide el valor almacenado en cantidad
    def mostrar_total(self):
        return self.cantidad

banco = Banco()
banco.operar()
banco.deposito_total()