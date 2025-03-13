#funciones de python 
'''
una funcion de python es un bloque de codigo que solo se ejecuta cuando se llama 

a las funciones se le pasan los datos, estos son los parametros de la fucion 

la misma devuelve estos datos procesados como un resultado 

en python se define una funcion usando la (def) palabra clave
'''

def my_fuction():
    print('Hola esta es mi funcion')

#llamado de una funcion 
'''
para llamar a una funcion, se debe utilizar el nombre de la funcion
seguida de los  parentesis()
'''

def my_dreams():
    print('Seras un gran Programador')

my_dreams()

#Argumentos 
'''
La informacion puede pasarse a las funciones como argumentos. 


los argumentos se especifican despues del nombre de la funcion dentro de los
parentesis. se puede anadir tantos argumentos como se desee, simplemente separarlos 
con una coma 

los argumentos a menudo se acortan a los arg en las documentaciones de python  

Argumentos o Parametros?
los terminos parametro y argumento se 
pueden diferir como lo mismo, Informacion que se le pasa 
a la funcion la cual devolvera dicha operacion como un resultado 
'''

# 1 Argumento 

def fuction_names(fname):
    print('Nombre:' + fname)

fuction_names('samuel')
fuction_names('brayan')
fuction_names('miguel')

# Numero de argumentos
'''
Por defecto una funcion debe ser llamada con el numero correcto de
argumentos. lo que se ignifica que si su funcion espera 2 argumentos, tienes que llamar 
a la funcion con 2 argumentos, no mas y no menos
'''

def fuction_person(fname, lname):
    print(fname + " " + lname)

fuction_person('camilo','sanchez')


# Argumentos arbitrarios, *args
'''
Si no se conoce cuantos argumentos seran pasados a la funcion, 
se puede hacer uso de los argumtos arbitrarios los cuales se representan con *,
se debe poner antes del nombre del parametro cuando se define la funcion.

de esta manera, la funcion recibira una tupla de argumentos, y puede acceder a los elementos 
consecuencia 
'''

def fuction_multiARG(*Person):
    print('Registro_persona:' + Person[2])

fuction_multiARG('Manuel', 'montes','manuelmont@test.com')


#Palabra clave arguemntos 
'''
Para las funciones tambien se le puede enviar argumetos de clave valor con la siguiente sintaxis 

(clave: valor) 


De esta manera el orden de los argumentos no importa.

'''

def fuction_sports(sport1, sport2, sport3):
    print("registro_sports:" + sport1 + sport2 + sport3)
 
fuction_sports(sport1= "Basketball", sport2= "football", sport3= "Baseball")
# Clave arbitraria  **kwargs 
'''
si por alguna razon usted no sabe cuantos argumentos definidos como keys van 
a ingresar a la funcion puede usar la clave arbitraria **

De esta manera la funcion recibira un diccionario de argumento para poder acceder
a los todos los items por medio de los index

los Parametros de las funciones se suelen acortar a una sola clave
en python
'''

def function_children(**kid):
    print("His last name is: " + kid["lname"])

function_children(fname= "Adres camilo", lname= 'sanchez')


# Clave arbitraria  **kwargs 
'''
si por alguna razon usted no sabe cuantos argumentos definidos como keys van 
a ingresar a la funcion puede usar la clave arbitraria **

De esta manera la funcion recibira un diccionario de argumento para poder acceder
a los todos los items por medio de los index

los Parametros de las funciones se suelen acortar a una sola clave
en python
'''

def function_children(**kid):
    print("His last name is: " + kid["lname"])

function_children(fname= "Adres camilo", lname= 'sanchez')


# Parametros preestablecidos en la funcion 
'''
cuando se define un parametro y se llama a la funcion sin argumento la funcion 
devuelve el valor predeterminado 
'''

def fuction_countrys(conutry= "Colombia"):
    print("He is from:" + conutry)

fuction_countrys("colombiano")
fuction_countrys("peruano")
fuction_countrys()
fuction_countrys("Marroqui")


# listas como argumentos 
'''
A las funciones se les pueden pasar todo tipo de datos como parametros (cadenas, numeros, listas, tuplas,
diccionarios etc), esto ara que la funcion interprete el mismo tipo de dato cuando igrese a la funcion 
'''

def function_almuerzo(igredientes):
    for  x in igredientes:
        print(x)

receta= ['zanahoria','cilantro','repollo','cebolla']

function_almuerzo(receta)

# Valores de retorno 
'''
las funciones pueden devolver un valor predeterminado sin ser especificamente un parametro
'''

def function_multiplicar(x):
    return 5 * x 

print(function_multiplicar(3))
print(function_multiplicar(7))
print(function_multiplicar(10))

# Declaracio pass
'''
la declaracion pass se usa para casos especiles donde no tenemos definido aun un contenido para
la fuincion, entonces evitamos contraer errores con esta declaracion
'''

def function_pass():
    pass


# Parametro de solo posicion
'''
Se puede especificar con los parametros los arguemntos que espera la funcion
existen dos tipos de argumentos posicionales y palabras clave.

se especifica que es un argumento posicional co (, /):
de esta manera solo se podra introducir en la funcio argumento posicionales
'''

def function_position(x, /):
    print(x)

function_position(34) 

'''
si no se usa el parametro de posicionamiento la funcion
esperara una palabra clave y un valor para esta 
'''

def function_notposition(x):
    print(x)

function_notposition(x= 3) # si se le pasa un arguemento de posicion habra un error

# Parametro de solo palabra clave
'''
Al igual que el parametro de posicionamiento 
las claves: valor tambien pueden ser un parametro unico dentro de la funcion
'''

def function_keywargs(*, x):
    print(x)

function_keywargs(x=100)

# Combinar la poscicion unica y la keywargs unica 
'''
Es evidente que al ser una propiedad inversamente proporcional podemos
realizar convinaciones de las mismas para crar un parametro donde se cumpla 
la posicion unica y la keywarg unica al mismo tiempo
'''

def bus_ocupation(personas, children, /, *, a, c):
    print('total personas:', personas,"total ninos:",children,"ninos y adultos:",a + c)

bus_ocupation(20, 5, a= 15, c= 5) 

# Recursion 
'''
El concepto general de la recursividad es una funcion que se llama a si misma 
en un bucle infinito o hasta que se rompa el ciclo 

las funciones con recursividad tienen gran similitud con los bucles pero cuentan con 
con una logica un poco mas compleja sin embargo es un recurso muy efectivo a la hora de 
llamarse a si misma 
'''

def countdown(number: int) -> int:
    if number >= 0:
        print(number)
        countdown(number -1)

countdown(100)

# Calcular el factorial de un numero 

def factorial(number: int) -> int:
    if number < 0:
        print("los numeros negativos no estan disponibles")
        return 0 
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)
    
factorial(10)


# Extra 

def puntos_extra(cadena1: str, cadena2: str) -> int:
    count= 0
    for number in range(1, 101):
        print(number) 
        if number % 3 == 0 and number % 5 == 0:
            print(cadena1 + cadena2)
        elif number % 5 == 0:
            print( cadena2)
        elif number % 3 == 0:
            print(cadena1)
    return count

print(puntos_extra('Multiplos_3','Multiplos_5'))

