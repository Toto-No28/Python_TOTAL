# Uso de min() y max() con argumentos individuales
menor = min(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
mayor = max(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(menor)
print(mayor)

print('-' * 50)

# Uso de min() y max() con una lista de números
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
menor = min(lista_numeros)
mayor = max(lista_numeros)

print(menor)
print(mayor)

print('-' * 50)

# También se pueden llamar directamente dentro de un f-string
print(f'El numero menor de la lista es {min(lista_numeros)} y el mayor es {max(lista_numeros)}')

print('-' * 50)

# Con strings, min() y max() buscan el orden alfabético
# Nota: Las mayúsculas tienen prioridad sobre las minúsculas en el código ASCII
nombres = ['Salvador', 'Juan', 'Maria', 'Pedro', 'Ana']
print(min(nombres)) # Imprime el primer nombre alfabéticamente
print(max(nombres)) # Imprime el último nombre alfabéticamente

print('-' * 50)

# Al usar min/max en un string, busca el carácter "menor" o "mayor" 
# basándose en su valor en la tabla ASCII
nombre = "Carlos"
print(min(nombre)) # La "C" mayúscula es menor que las minúsculas en ASCII
print(max(nombre)) # La "s" es la mayor alfabéticamente en minúsculas

# Al convertir a minúsculas, el resultado cambia porque se comparan puros iguales
nombre = "Carlos"
print(min(nombre.lower())) # Ahora "a" es la menor
print(max(nombre.lower())) # "s" sigue siendo la mayor

print('-' * 50)

# Al usar min/max con diccionarios:
diccionario = {'a': 1, 'b': 2, 'c': 3}

# Por defecto, busca entre las LLAVES (keys)
print(min(diccionario)) # Imprime la llave menor alfabéticamente
print(max(diccionario)) # Imprime la llave mayor alfabéticamente

# Si queremos los valores, necesitamos especificar .values()
print(min(diccionario.values())) # Imprime el valor numérico menor
print(max(diccionario.values())) # Imprime el valor numérico mayor