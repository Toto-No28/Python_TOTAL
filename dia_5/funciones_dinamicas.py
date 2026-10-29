def numero_3_cifras(numero):
    return numero in range(100, 1000)

resultado = numero_3_cifras(123)
print(resultado)

print('-' * 50)

def numero_4_cifras(lista_numeros):
    for numero in lista_numeros:
        if numero in range(1000, 10000):
            return True
        else:
            pass
    return False

