### Decoradores ###

"""
Los decoradores hacen parte de las funciones las cuales son ciudadanos 
de primera clase 

Los decoradores trabajan con al menos 3 funciones llamandose estas
- input
- funcion principal 
- output 

# formula 

a(b) -> c

"""

# Estructura  de un decorador de funciones sin argumentos

def function_a(function_b):

    def function_c():
        print('>>> Antes de la ejecucion')
        function_b()
        print('>>> Antes de la ejecucion')
    
    return function_c


# Decorar una funcion 
'''
Para hacer uso de un decorador usamo el @ para llamar la 
ejecucion de el decorador acompanado de la funcion que queremos decorar
'''

@function_a 
def saludar():
    print('Hola, desde una funcion! ')

saludar()

print("--"*50)

# Decoradores de funciones que reciben argumentos

def function_args(function_args_b):

    def function_args_c(*args, **kwargs):
        print('>>> Antes de la ejecucion')
        resultado = function_args_b(*args, **kwargs)
        print('>>> Antes de la ejecucion')
        
        return resultado
    
    return function_args_c

@function_args
def sum_values(value_a, value_b):
    return value_a + value_b

print(sum_values(100,50))



# Refactor de el decorador 
"""
Por concepto de descripcion  podemos implementar los decoradores 
con esta estructura de desarrollo.

Tener en cuenta que es por descripcion mas no por regla,
lo que se busca es dar mayor significado a la hora de poder leere el codigo
"""


def my_custom_decorator(function):

    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    
    return wrapper

print("--"*50)

# Calcular el tiempo que le toma a una  funcion terminar su ejecucion 

import time

def calcular_tiempo(function):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)

        print('Tiempo total: ', time.time() - start)

        return result 
    
    return wrapper

@calcular_tiempo
def multiply_values(value_a, value_b):
    time.sleep(3)
    return value_a * value_b

print(multiply_values(5,2))