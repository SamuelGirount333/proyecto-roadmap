
def mis_contactos():
    contactos = {}
    is_on = True
    
    def insert_contact():
        name = input('ingrese el nombre del contacto. ')
        phone = input('ingrese el numero del contacto. ')
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 10:
            contactos[name] = phone

    while is_on:
        print('')    
        print('\n--- Agenda contactos ---')
        print("1. agregar un contacto")
        print("2. busqueda")
        print("3. actualizacion")
        print("4. Eliminar un contacto")
        print('5. salir')

        option = input('\nseleccione una opcion: ')

        match option:
            case 1:
                name = input("ingrese nombre del contacto. ")
                phone = input('ingrese el numero del contacto. ')
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 10:
                    contactos[name] = phone
                print('el contacto se agrego correctamente')
            case 2:
                name = input('ingrese el nombre del contacto a buscar')
                name in contactos
                print(f'El numero de telefono de {name} es {contactos[name]}. ')
            case 3:
                name =  input('ingrese el nombre del contacto a actualizar. ')
                if name in contactos:
                    phone_new = input('ingrese el numero de telefono nuevo. ')
                    if phone.isdigit() and len(phone_new) > 0 and  len(phone_new) <= 10:
                        contactos[name] = phone_new
                else:
                    print('ingrese un numero de telefono valido') 
            case 4:
                name = input('ingrese el nombre del contacto que desea eliminar. ')
                if name in contactos:
                    del contactos[name]
                    print('El contacto se elimino correctamente. ')
            case 5:
                print('saliendo del programa')
                is_on = False
            case _:
                print('Opcion no valida, Elije una opcion valida')
mis_contactos()