"""
LISTAS
"""
# Que son las listas.


# Correcta estructura de una lista 
"""
Los objetos que esten dentro de la lista adoptan una posicion de [0], [1] 
esta es la forma que nos podemos mover usando los slides [::] 
"""
# Forma estructurada para muchos datos 
flores_veranales= [
    "Rosa",
    "Girasol",
    "Orquidia",
    "Mala madre",
    "Tulipanes",
    "lavanda",
    "Orquidias",
    "Ortalisas",
]

# Estructura de clave valor 

datos_estudiantes= [
{'Pezcado': 'pez goblo', "Mamifero": "mono", "Pajaro": 'Amarillo' },
('fish','mammal','bird'),
['Agua', 'Jungla', 'Sky']
]

# La lista se puede usar con un iterable como argumento 

list_vacia= list()
print(list_vacia)

# -Ejemplo 

lista_elemtos_tupla= list(("Parrot", "Bird", 334782))
print(lista_elemtos_tupla)


# funciones de las listas 
"""

las listas comparten las funciones de las cadenas 
lengt
map
reduce

"""

# Concaatenacion de listas  

lista_prueba2= [100,200,300,400]
lista_prueba3= [450,500,550,600]

listas= lista_prueba2  + lista_prueba3
print(listas)

# length 

lista_length= ["banana","apple","cherry"]
x= len(lista_length)

print(x)


# Data types 

list_1= ["apple","bananna","cherry"]
list_2= [1,5,7,9,3]
list_1= [True, False, False]

# se pueden integrar los diferentes tipos de datos en una sola lista 

lis_integrate= ["",34, True, 40, 'male',]

# Movimientos dentro de la lista 

list_ejmpl= ["apple","banna","Cherry"]
print(list_ejmpl[1])

# Slides en cadenas 

print(list_ejmpl[-1])

# slide con indices 

index_list= ['apple','banana','cherry','orange','kiwi','melon']
print(index_list[2:5])

# Comprobar si un elemento existe en una lista 

list_comprobacion= ["Platano",'fresa','Mango']
if "apple" in list_comprobacion:
    print("Yes i Do bro we on raigth")


# Cambiar valores dentro de una lista

lista_prueba4= ["basktball","futbol","Ciclismo","Natacion"]
lista_prueba4[3]= "Motociclismo"
print(lista_prueba4)

# Cambiar los valores de una lista usando un rango

range_list= ['Avion','Bus','Moto','Carro','Bicicleta','Barco']
range_list[1:3] = ["Esto","Cambie"]
print(range_list)


# Recorrido de una lista con obejetos repetidos

conteo_frutas= {}
ls_frutas= ["manzana", "pera", "manzana", "naranja", "pera", "manzana"]\

for fruta in ls_frutas:
    conteo_frutas[fruta]=conteo_frutas.get(fruta, 0) +1
    
print(conteo_frutas) # devuelve el diccionario con la (key: fruta) y los (values: cnt_in) 


#SETS 
"""
Un set es una colección desordenada y sin elementos duplicados. Se usa para operaciones matemáticas como uniones,
intersecciones y diferencias.

"""

# Crear un set
mi_set = {1, 2, 3, 4, 5}
otro_set = {4, 5, 6, 7}

# Agregar un elemento
mi_set.add(6)
print(mi_set)  # {1, 2, 3, 4, 5, 6}

# Eliminar un elemento (si no existe, da error)
mi_set.remove(3)
print(mi_set)  # {1, 2, 4, 5, 6}

# Eliminar sin error si el elemento no existe
mi_set.discard(10)  # No hace nada si 10 no está
print(mi_set)

# Eliminar y devolver un elemento aleatorio
elemento = mi_set.pop()
print(elemento, mi_set)

# Vaciar el set
mi_set.clear()
print(mi_set)  # set()

# Unión de sets
print(otro_set.union({8, 9}))  # {4, 5, 6, 7, 8, 9}

# Intersección (elementos comunes)
print(otro_set.intersection({5, 6, 10}))  # {5, 6}

# Diferencia (elementos solo en el primero)
print(otro_set.difference({5, 6, 10}))  # {4, 7}

# Diferencia simétrica (elementos únicos en ambos)
print(otro_set.symmetric_difference({5, 6, 10}))  # {4, 7, 10}


print('--'*50)


#Diccionarios
"""
Son colecciones clave-valor.
"""
# Crear un diccionario
mi_diccionario = {
    "nombre": "Ana",
    "edad": 30,
    "ciudad": "Bogotá"
}

# Obtener un valor sin error si la clave no existe
print(mi_diccionario.get("edad"))  # 30
print(mi_diccionario.get("altura", "No disponible"))  # No disponible

# Obtener solo las claves
print(mi_diccionario.keys())  # dict_keys(['nombre', 'edad', 'ciudad'])

# Obtener solo los valores
print(mi_diccionario.values())  # dict_values(['Ana', 30, 'Bogotá'])

# Obtener pares clave-valor
print(mi_diccionario.items())  # dict_items([('nombre', 'Ana'), ('edad', 30), ('ciudad', 'Bogotá')])

# Agregar o actualizar valores
mi_diccionario.update({"pais": "Colombia", "edad": 31})
print(mi_diccionario)

# Eliminar una clave y obtener su valor
edad = mi_diccionario.pop("edad")
print(edad)  # 31
print(mi_diccionario)

# Eliminar la última clave añadida
clave, valor = mi_diccionario.popitem()
print(clave, valor)  # Puede ser ('pais', 'Colombia')
print(mi_diccionario)

# Vaciar el diccionario
mi_diccionario.clear()
print(mi_diccionario)  # {}


print('--'*50)

#Tuplas 
'''
Las tuplas son inmutables y ordenadas.
'''
# Crear una tupla
mi_tupla = (10, 20, 30, 10, 40, 10)

# Contar cuántas veces aparece un elemento
print(mi_tupla.count(10))  # 3

# Obtener el índice de un elemento
print(mi_tupla.index(30))  # 2

#Extra 

def opciones_agenda():
    print('\n--- Agenda contactos ---')
    print("1. agregar un contacto")
    print("2. busqueda")
    print("3. actualizacion")
    print("4. Eliminar un contacto")


contactos = []

while True:
    opciones_agenda()
    opcion= int(input('Ingrese una opcion: '))
    match opcion:
        case 1:
            print('opcion 1')
        case 2:
            print('opcion 2')
        case 3:
            print('opcion 3')
        case 4:
            print('opcion 4')
        case 5:
            break                         