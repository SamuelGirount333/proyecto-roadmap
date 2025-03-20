"""
Recursividad
"""

# Conteo hacia atras 
def countdown(number: int) -> int:
    if number >= 0:
        print(number)
        countdown(number -1)

countdown(100)
print(countdown)


print('--'*10)

# calcular el factorial 

def function_factorial(number: int) -> int:
    if number < 0:
        print('los numeros negativos no tienen factorial ')
        return 0
    elif number == 0:
        return 1
    else:
      return number * function_factorial(number - 1)

print(function_factorial(10))

print('--'*10)

# Secuencia de fibonacci 

def function_fibonacci(number: int) -> int:
    if number == 0:
        print('La posicion tiene que ser mayor a 0')
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return function_fibonacci(number -1) + function_fibonacci(number -2)

print(function_fibonacci(8))