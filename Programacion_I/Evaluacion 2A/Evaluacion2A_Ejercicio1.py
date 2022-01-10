#Evaluación 2A  - Ejercicio 1
#Escribir una clase en python que convierta un número entero ingresado por teclado a número romano y que luego lo muestre por pantalla

class Conversion:
    # Defino el metodo __init__ y llamo al metodo de conversion
    def __init__(self):
        self.decimal = int(input("Introduzca un número: "))
        self.convertir()

    # Defino el metodo para la conversión de decimal a numeral romano
    def convertir(self):
        # Creo una lista con los valores de numeros decimales con sus homologos romanos
        constantes = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10) ,
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]
        # Creo la variable resultado con campo vacio
        r = ""

        # Creo un ciclo para convertir el decimal a romano
        for (romano, num) in constantes:
            (d, self.decimal) = divmod(self.decimal, num)
            r += romano * d
        
        #Imprimo el resultado
        print(r)
    
numero = Conversion()