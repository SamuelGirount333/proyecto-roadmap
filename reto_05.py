""" Valor y referencia """

# Tipos de datos por valor 
"""
contexto: un tipo de dato por valor en python es aquel en el que, al 
asignarle a una nueva variable o pasarlo a una funcion, se crea  una copia 
independiente del valor original. Esto hace que cualquier modificacion que se haga sobre la variable
no afecta el valor original
"""
my_int_a = 10
my_int_b = my_int_a
my_int_b = 20
#my_int_a = 30
print(my_int_a)
print(my_int_b)

print('--'*50)
# Tipos de dato por referencia 
'''
contexto: las dos variables comparten la misma posicion de variables 
y al modificar una de ellas se vera reflejados los cambios en las dos 
variables ya que no se esta co piando la posicion de memoria, 
lo que se esta haciendo es una referencia de una variable con la otra 
'''
my_list_a = [10,20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

print('--'*50)
# Funciones con datos por valor 

def function_int_valor(my_int: int):
    my_int = 20 
    print(my_int)

my_int_c = 10 
function_int_valor(my_int_c)
print(my_int_c)


print('--'*50)
# Funcion con datos por referencia 

def function_ref_values(my_list: list):
    my_list.append(30)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_c = [10, 20]
function_ref_values(my_list_c)
print(my_list_c)

print('--'*50)
""" Extra """

# Funcion por valor  

def value_change(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    vlaue_b = temp
    return value_a, value_b

my_int_d = 10 
my_int_e = 20
my_int_f, my_int_g = value_change(my_int_d, my_int_e)

print(f'{my_int_d}, {my_int_e}')
print(f'{my_int_f}, {my_int_g}')