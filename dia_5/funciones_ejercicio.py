# Definimos la función llamada 'todos_positivos' que espera recibir una lista
def todos_positivos(lista):
    # Usamos un bucle 'for' para revisar cada número dentro de la lista uno por uno
    for num in lista:
        # Evaluamos: ¿Es el número actual menor que cero (negativo)?
        if num < 0:
            # En el momento que encontramos un SOLO negativo, la función se detiene
            # y devuelve False. No necesita seguir revisando el resto de la lista.
            return False
    
    # Si el bucle termina y NUNCA se encontró un número menor que cero,
    # significa que todos eran positivos (o cero). Entonces devolvemos True.
    return True

# --- SECCIÓN DE PRUEBAS ---

# 1. Prueba con una lista que tiene números negativos mezclados
lista_numeros = [10, -5, 3.14, -12.5, 0, 42, -7.8, 100, -200, 15.5, -3, 8, -0.5, 22, -11, 7.7, -99, 1, -4.2, 50]

# Llamamos a la función y guardamos el resultado (será False por los negativos)
resultado = todos_positivos(lista_numeros)
print(f"¿Son todos los números positivos en lista_numeros? {resultado}")

# 2. Prueba con una lista que SÓLO tiene números positivos
lista_positiva = [1, 5, 10, 25, 100]

# Llamamos a la función con la nueva lista (el resultado será True)
resultado_positivo = todos_positivos(lista_positiva)
print(f"¿Es positiva la lista {lista_positiva}? {resultado_positivo}")


print('-' * 50)

'''Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.'''

def suma_menores(lista):
    suma = 0
    for numero in lista:
        if numero in range(1, 1000):
            suma += numero
    return suma
            
            
            
lista_numeros = [10, -5, 3.14, -12.5, 0, 42, -7.8, 100, -200, 15.5, -3, 8, -0.5, 22, -11, 7.7, -99, 1, -4.2, 50]

resultado = suma_menores(lista_numeros)
print(f"La suma de los números menores a 1000 es: {resultado}")

print('-' * 50)

#Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.

def cantidad_pares(lista):
    pares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
    return pares
    
lista_numeros = [10, -5, 3.14, -12.5, 0, 42, -7.8, 100, -200, 15.5, -3, 8, -0.5, 22, -11, 7.7, -99, 1, -4.2, 50]

resultado = cantidad_pares(lista_numeros)
print(resultado)

print('-' * 50)

