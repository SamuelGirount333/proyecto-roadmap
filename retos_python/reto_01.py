# Tipos de operadores Arimeticos de python.
"""
En python hay  diferentes tipos de operadores Arimeticos 
entre ellos:

Relacionales
logicos 
De asignacio  
Especiales
"""

# Que es la division por el suelo (//)
'''
la divisio por el suelo es igual que la division normal salvo que el 
resultado siempre se redondea al numero mas pequeno 
'''


print('--'*50)
operadores_arimeticos= ["+ : suma, - : resta, * : multiplicacion, / : division, ** : potencia, // : Division al piso, % : modulo"]

print('Operadores Arimeticos')
print(operadores_arimeticos)
print('--'*50)

suma= 33 + 33 
resta= 100 - 6
multiplicacion= 333 * 300
division= 5 / 2
exponente= 3 ** 10
division_piso= 5 // 2 
modulo= 100 % 2  #Residuo 


# Que es una estructura de control en python
'''
contexto: 

las estructuras de control en pytho son bloques de codigo que permiten control el flujo del 
programa. Esto se ignifica que determinan como se ejecutan las instrucciones del codigo,
dependiendo de ciertas condiciones o meintras una condicion se mantenga. En python, las estructuras de control 
principales son las condicionales (if, elif, else) y las de bucle (for, while)

'''

print('--'*50)
print('Estos las estructuras de control condicionales en python')

# Condicionales
'''
Permiten ejecutar un bloque de codigo segun se cumplan ciertas condiciones 
'''
operadores_loicos= ['==','!=','<','<=','>','>=']
print('Operadores logicos')
print(operadores_loicos)
a='a'
b='b'

a == b  # a igual que b
a != b  # a no igual que b
a < b   # a es menor que b
a <= b  # a es menor o igual que b 
a > b   # a es mayor que b
a >= b  # a es mayor o igual que b

print('--'*50)
# if 

print('Condicional if')
numero = 10 
if numero > 5:
    print(f'{numero} es mayor que 5: ')

print('--'*50)
# elif 

'''
si las condiciones anteriores no fueron ciertas intenta con esta otra
'''
print('Condicional elif')
a= 33
b= 33

if b > a:
    print(f'{a} es mayor que {b}')
elif a == b:
    print(f'{a} es igual que {b}')

print('--'*50)
# else
'''
se utiliza en convinacion con if. el bloque de codigo despues de (else) se ejecutara si ninguna
de las condiciones anteriores se cumple.

'''
print('Condicional else')
numero1= 200
numero2= 33
if numero1 > numero2: 
    print(f'El numero {numero1} es mayor que {numero2}: ')
elif numero1 == numero2:
    print(f'{numero1} es igual a {numero2}: ')
else:
    print(f'El numero {numero1} es menor que {numero2}: ')

print('--'*50)

# Operadores ternerarios o Expresiones condicionales
print('Operadores Ternarios')
'''
se usa si solo se tiene una declaracion que ejecutar, una para SI y otra para NO
'''

a= 2
b= 330
print('a') if a > b else print('b')

    # Tambien se pueden tener maximo 3 condiciones en una linea 

a=330
b=330
print('a') if a > b else print('=') if a == b else print('b')

print('--'*50)

# Operador And
print('Operador AND')
a= 200
b= 33
c= 500

if a > b and c > a: 
    print('las dos condiciones son verdaderas: ')

print('--'*50)

#Opeador OR 
print('Operador OR')
a= 200
b= 33
c= 500
if a > b or a > c:
    print(f'Una de las condiciones es verdadera: {a} es mayor que {b}')
 
print('--'*50)

# Operadr Not 
print('Operador NOT')
a= 300
b= 500 
if not a > b:
    print(f'{a} no es mayor que {b}: ')

print('--'*50)

# if anidado 

'''
El operador if permite realizar condiciones anidadas
'''
print('if anidado')
x= 250

if x > 100:
    print(f'{x} Es mayor que 100')
    if x <= 350: 
        print(f'{x} Es mayor que 100 y menor o igual que 350 pero menor que 500')
        if not x > 500: 
            print(f'{x} Es menor que 500')
else:
    print(f'{x} Es mayor que 500')

print('--'*50)
print('Declaracion pass')
# Declaracion Pass 
'''
las condiciones if no pueden tener condiciones vacias pero, 
si por alguna razon tienes una declaracion sin contenido se puede
usar el Pass para ignorar la declaracion y evitar un output de error
'''

x= 450.0909
if x:
    pass


print('--'*50)
print('Estructuras de control Bucles de python:')

# Bucles en python
'''
Python cuenta con dos bucles primitivos 

while: Mientras que una condicion sea verdadera el bucle se ejecutara un numero de veces infinito 
 
for: Mientras que al menos una de las condiciones sea verdadera se ejecutara un numero finito de veces 
'''

print('--'*50)
print("Estructuras de control")
print('Bucles while')
# Bucle While
'''
Con el bucle while podemos ejecutar un conjunto de declaraciones siempre y cuando una condicion sea 
verdadera

Nota:
siempre aumentar el valor para que en cada iteracio del bucle se cuente como una nueva 
'''
print('Imprimir i siempre y cuando sea menor 6')
i = 1
while i < 6:
    print(i)
    i += 1  

''' 
El bucle while requiere que las variables importantes esten listas, en este ejemplo 
requerimos definir una variable (i) que le asignamos un valor inicial = (1)
'''

print('--'*50)
print('Declaracion de ruptura')
print('break')
# Break
'''
Con la declaracion de break podemos detener el bucle incluso si 
la condicion es cierta
'''
print('Salir del bucle cuando este sea = 3')
i= 1
while i < 6: 
    print(i)
    if i == 3:
        break
    i += 1

print('--'*50)
print('Declaracion de Continuar')
print('continue')
# continue 
'''
Con la declaracion continue podemos detener la itaracion y
cpntinuar con la siguiente
'''

i=0
while i < 6:
    i += 1
    if i == 3:
        continue 
    print(i) 

print('--'*50)
'''
Con esta condicional podemos detener la se cuencia de codigo en un punto exacto 
y continuar con la iteracion del codigo bucle, el bucle se pausara en la condicion y no 
mostrara el resultado de la declaracio definida en  el continue 
'''

# Bucle while con condicional else
'''
los bucles while tambien pueden contener condicionales como (else)
esto nos servira para ejecutar el bucle cuando la condicio ya no sea cierta 
'''

i= 1
while i < 6:
    print(i)
    i += 1
else:
    print("En esta vuelta i ya no es verdadera")

print('--'*50)
print('Estructuras de control')
print('Bucles for')

#Bucles for 
'''
los bucles for se utilizan para iterar sobre una secuencia 
que pueden ser bien sea (tuplas, una lista, un diccionario un array o una cadena)_

con el bucle for podemos ejecutar un conjunto de declaraciones, una vez para cada elemto en 
una lista, tupla o diccionario etc..

Al igual que el bucle while el for no necesita una variable de indexacion como valor inicial 

'''

cellphon_marca=['Nokia','Apple','Samsung']

for x in cellphon_marca:
    print(x)

# Iteracion en cadenas 
'''
incluso las cadenas son objetos iterables, ya que son una secuencia de caracteres
'''

for x in 'Motorola':
    print(x)

print('--'*50)
print('Break')
# Declaracio de ruptura 
#Break 
'''
Con la declaracion break podemos detener el bucle 
incluso antes de que haya iterado sobre todos los elementos
se dentendra en donde indiquemos la sentencia break y se 
saldra del bucle 
'''

cellphon_marca=['Nokia','Apple','Samsung']
for x in cellphon_marca:
    print(x)
    if x == 'Apple':
        break
    print(x)

print('--'*50)
print('continue')
# Declaracion de continucacion 
'''
con la declaracion de continuacion podemos detener la iteracion actual de bucle y continuar 
con la siguiente iteracion al igual que con con los bucles while

al declarar una sentencia para el continue exeptuamos la iteracion del valor que se le ah asiganado
'''
cellphon_marca=['Nokia','Apple','Samsung']

for x in cellphon_marca:
    if x == 'banana':
        continue
    print(x)


print('--'*50)
print('Funcion range()')
# Funcion de range()
'''
Para el bucle for podemos usar la funcion range() a la hora de 
declalar un rengo de numeros especificos 

la funcion de range() devuelve una secuencia de nuemeros, a partir de 0 
por defecto, y incremetos de (1 en 1) por defecto, y terminan en un numero
especifico 

el rango siempre devuelve hasta el numero antesesor del cual se difinio como
el final del rango de numeros entre (0 y x)
'''

for x in range(20):
    print(x)


print('--'*50)
print('Parametros predeterminados')
# valores predeterminados
'''
par la funcion de range podemos definir el inicio y el final de nuestro rango
esto quiere decir que no es explicitamente necesesario que el valor de los rangos 
empiece en 0 como valor inicial, pero sigue conservando su termino fianal antecesor 
al termino final
'''

for x in range(3, 10):
    print(x)


print('--'*50)
print('valor incremetable')
# Valor de incrementable 
'''
el range() es muy completo ya que se le puede pasar 3 parametros (inicial, incremento, final)
el range() toma por defecto un incrementable de 1, sin embargo es posible especificar el parametro 
'''
for x in range(0, 1, 30):
    print(x)


print('--'*50)
print('for (else)')
# else en bucle for 
'''
en el bucle for podemos hacer uso del condicional (else) cuando las condiciones 
del bucle no son verdaderas

lo que nos permite realizar una iteracion aun cuando la condicion del bucle ya no sea verdadera

'''

for x in range(6):
    print(x)
else:
    print('Finally finished!') # No se ejcutara si es detenido por una declaracion break


print('--'*50)
print('for anidado')
# Bucles anidados 
'''
un bucle anidado es un bucle el cual almacena uno o mas condiciones 
el bucle interior se ejecuta una vez por cada iteracion del bucle externo 
'''

colors_life=['red','green','yellow','blue']
cellphon_marca=['Nokia','Apple','Samsung']

for x in colors_life:
    for y in cellphon_marca:
        print(x, y)


print('--'*50)
print('Declaracion Pass')
# Declaracion de pass
'''
al igual que los condicionales los bucles for no pueden encontrarse vacias
pero si por alguna razon tenemos un bucle for vacio podemos hacer uso de la 
declaracion pass para evitar contraer un error 
'''

for x in [0, 1, 2]:
    pass


print('--'*50)
print('Puntuacion Extra')
#Puntuacion extra reto de programacion 

for number in range(10, 56):
    if number == 16:
        continue
    if number % 3:
        print(number)
    