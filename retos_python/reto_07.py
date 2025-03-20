''' Ejercicio '''

""" Pila/Stack (LIFO) -> last int first Out """

stack = []

stack.append('Manzanas')
stack.append('Sandias')
stack.append('Peras')
stack.append('Aguacates')
print(stack)

# Lifo manual
stack_item = stack[len(stack) -1]
del stack[len(stack) -1]
print(stack_item)
print(stack)

print('--'*50)

# Lifo python 
print(stack.pop)
print(stack)


print('--'*50)
""" Cola/Queue (FIFO) -> First int First Out """

queue = []

queue.append('Cliente 1')
queue.append('Cliente 2')
queue.append('Cliente 3')
queue.append('Cliente 4')
print(queue)


# FIFO Manual 
queue_item = queue[0]
del queue[0]

print(queue_item)
print(queue)

print('--'*50)

# FIFO python
print(queue.pop(0))
print(queue)


print('--'*50)

""" Extra """

def web_navigation():

    stack_web = []
    
    while True:

        action = input('ingrese una URL o Interactua con palbras Adelante/Atras/Salir: ')

        if action == 'salir':
            print('Saliendo del navegador web')
            break
        elif action == 'adelante':
            pass
        elif action == 'atras':
            if len(stack_web) > 0:
                stack_web.pop()
        else:
            stack_web.append(action)
        
        if len(stack_web) > 0:
            print(f'Has navegado a la web: {stack_web[len(stack_web)- 1]}.')
        else:
            print('Estas en la pagina de inicio')

#web_navigation()

print('--'*50)

def comunity_printer():
    pedido = []
    
    while True:
        
        order = input('Agrege un documento a la cola o use Imprimir/Salir.  ')

        if order == 'salir':
            print('Apagando la impresora')
            break        
        
        elif order == 'imprimir':
            if len(order) > 0:
                print(f'El documento {pedido[0]} se imprimio con exito. ')
                pedido.pop(0)
        
        elif len(pedido) > 0:
            pedido.append(order)
            print(f'La cola de impresion es: {pedido}')
        
        else:
            print(f'la cola de impresion {pedido} esta vacia')
            return 'ingrese un documento. '

comunity_printer()