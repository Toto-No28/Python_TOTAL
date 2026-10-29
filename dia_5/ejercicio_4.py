'''Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.'''

def contar_primos(numero):
    primos = []
    for i in range(2, numero + 1):
        if i % 2 == 0:
            continue
        for j in range(3, i, 2):
            if i % j == 0:
                break
        else:
            primos.append(i)
    print(primos)
    return len(primos)

print(contar_primos(48))

print('-' * 50)

def contar_primos(numero):
    primos = [2]
    if numero < 2:
        return 0
    for i in range(3, numero + 1, 2):
        for j in range(3, i, 2):
            if i % j == 0:
                break
        else:
            primos.append(i)
    print(primos)
    return len(primos)

print(contar_primos(2))