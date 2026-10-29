# En la propiedad "range" se toman todos los elementos desde el 0 hasta el 5 (el 5 no se toma en cuenta) El resultado de "range" es: 0, 1, 2, 3, 4

for numero in range(5):
    print(numero)

print('-' * 50)

# El primer parámetro se toma para indicar desde qué número se va a trabajar y el segundo hasta dónde. El resultado del print es : 1, 2, 3, 4
for numero in range(1, 5):
    print(numero)

print('-' * 50)

# El tercer parámetro se toma para indicar de cuánto en cuánto se va a trabajar. El resultado del print es : 0, 2, 4, 6, 8
for numero in range(0, 10, 2):
    print(numero)


# Range no recibe floats de ninguna manera, solo integers.

# También range se puede utilizar para llenar listas de manera automática

lista = list(range(1, 101))

# Para imprimir la lista completa:
print(lista)

# Para imprimir números saltados (ej. de dos en dos), usa slicing en el print:
# print(lista[::2])  # Imprime: 1, 3, 5, ..., 99
# print(lista[::3])  # Imprime: 1, 4, 7, ..., 100

print('-' * 50)
print(lista[::2])
print('-' * 50)
print(lista[::3])





