def usuario(**kwargs):
    print(type(kwargs))

usuario(nombre="Salvador", edad=30, genero="Masculino")

print('-' * 50)

def usuario1(**kwargs):
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

usuario1(nombre="Salvador", edad=30, genero="Masculino")

print('-' * 50)

def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total

suma(a=1, b=2, c=3)

print('-' * 50)

print(suma(a=1, b=2, c=3))

print('-' * 50)

def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'El valor de arg es: {arg}')

    for clave, valor in kwargs.items():
        print(f'El valor de {clave} es {valor}')

prueba(1, 2, 3, 4, 5, nombre="Salvador", edad=30, genero="Masculino")


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")

