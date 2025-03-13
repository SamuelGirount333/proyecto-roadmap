contactos=[]

def opciones_agenda():

    print('\n--- Agenda contactos ---')
    print("1. agregar un contacto")
    print("2. busqueda")
    print("3. actualizacion")
    print("4. Eliminar un contacto")


def funciones_agenda(contactos):
    while True:
        opciones_agenda()
        opcion= int(input("seleccione una opcion"))

        if opcion == 1:
            print('Ingrese nombre,telefono')
            nombre= input("igrese nombre")
            telfono= int(input("ingrese el telefono"))
            if telfono == 10 and telfono.isdigit():
                contactos= {nombre: telfono} 
            else:
                print('ingrese un numero valido de 10 digitos')
        break