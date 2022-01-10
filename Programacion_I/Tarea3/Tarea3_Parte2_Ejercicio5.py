#Lenguaje de Programacion I -Python
#Prof. Lic. Miguel Dario Duarte Reyes
#Alumno: Martin Enrique Medina Aveiro
#Tarea 3 Parte 2 Ejercicio 5
class Agenda:
    #inicializo la clase
    def __init__(self):
        #creo una lista para almacenar la informacion
        self.contactos = []
    
    #inicio del menu
    def menu(self):
        print("Agenda Personal")
        print("1. Añadir Contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Cerrar agenda")

        #Pido una opcion para realizar el metodo seleccionado
        opcion = int(input("Introduca la opción deseada: "))
        if opcion == 1:
            self.anhadir()
        if opcion == 2:
            self.lista()
        if opcion == 3:
            self.buscar()
        if opcion == 4:
            self.editar()
        if opcion == 5:
            print("Saliendo de la agenda.")
            exit()
        
        #Vuelve a llamar al menú
        self.menu()

    #metodo para añadir contactos
    def anhadir(self):
        print("—————————————————————————")
        print("Añadir un nuevo contacto")
        print("—————————————————————————")
        name = input("Introduzca el nombre: ")
        telf = int(input("Introduzca el teléfono: "))
        email = input("Introduzca el Email: ")
        #anexa informacion a la lista
        self.contactos.append({'nombre': name, 'telf': telf, 'email': email})

    #metodo para ver lista de contactos
    def lista(self):
        print("———————————————————")
        print("Lista de contactos")
        print("———————————————————")
        if len(self.contactos) == 0:
            print ("No hay contactos en memoria.")
        else:
            for i in range(len(self.contactos)):
                #saco la información en nombre
                print (self.contactos[i]['nombre'])

    #metodo para buscar informacion del contacto
    def buscar(self):
        print("——————————————————————")
        print("Buscador de contactos")
        print("——————————————————————")
        nombre = input("Introduzca el nombre a buscar: ")
        for i in range(len(self.contactos)):
            if nombre == self.contactos[i]['nombre']:
                print("Datos del contacto")
                print("Nombre:", self.contactos[i]['nombre'])
                print("Teléfono:", self.contactos[i]['telf'])
                print("EMail:", self.contactos[i]['email'])
                #para que pare cuando encuentre
                return i
    
    #metodo para editar
    def editar(self):
        print("————————————————————")
        print("Editor de contactos")
        print("————————————————————")    

        contacto = self.buscar()
        print("¿Qué desea editar?")
        print("1. Editar nombre")
        print("2. Editar teléfono")
        print("3. Editar email")
        print("4. Volver")

        opcion = int(input())

        if opcion == 1:
            nombre = input("Introduzca el nuevo nombre: ")
            self.contactos[contacto]['nombre']=nombre
        if opcion == 2:
            telf = int(input("Introduzca el nuevo número: "))
            self.contactos[contacto]['telf']=telf
        if opcion == 3:
            email = input("Introduzca el nuevo email: ")
            self.contactos[contacto]['email']=email  
        if opcion == 4:
            return()

agenda = Agenda()
agenda.menu()