def suma(a, b):
    return a + b

print(suma(1, 2))

print('-' * 50)

def suma2(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(suma2(1, 2, 3, 4, 5))

print('-' * 50)

