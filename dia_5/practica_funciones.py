import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Ejemplo de uso (opcional - puedes comentarlo o dejarlo para prueba)
# g1, g2 = lanzar_dados()
# print(evaluar_jugada(g1, g2))

print('-' * 50)

lista_numeros = [1, 2, 85, 43, 21, 85, 93, 2, 1]

def reducir_lista(lista):
    # Al convertir a set() eliminamos duplicados (los sets no los permiten), 
    # luego volvemos a list() para recuperar el formato de lista original.
    lista_sin_duplicados = list(set(lista))
    
    # 'if lista:' evalúa como True si tiene elementos y False si está vacía.
    # Lo usamos para asegurar que no falle al intentar buscar el max() de una lista vacía.
    if lista_sin_duplicados:
        lista_sin_duplicados.remove(max(lista_sin_duplicados))
        
    return lista_sin_duplicados

def promedio(lista):
    # 'if not lista' se activa si la lista está vacía.
    # Evitamos el error ZeroDivisionError (no se puede dividir por 0).
    if not lista:
        return 0
    # sum() suma todos los valores y len() cuenta cuántos hay.
    # Retornamos el resultado de la división (el promedio).
    return sum(lista) / len(lista)

print('-' * 50)# --- EJERCICIO: MONEDA Y LISTA --- #

# 1. VERSION CON ERRORES (Original del usuario)
# NOTA: Este bloque se comenta para que el script no falle al ejecutarse debido a los errores de sintaxis.

"""
def lanzar_moneda_error():
    # ERROR: Se debe pasar una colección (lista) a choice(), no argumentos separados.
    moneda = random.choice('Cara', 'Cruz')
    return moneda
    
def probar_suerte_error(moneda, lista):
    if moneda == 'Cara':
        print(f'La lista de autodestruirá')
        # ERROR: Devolvemos lista.clear(), lo cual retorna None (no devuelve una lista []).
        return lista.clear() 
    
    # ERROR DE SINTAXIS: El return de arriba cortó la conexión del if con el else.
    else:
        print(f'La lista fue salvada')
        return lista
"""

# 2. VERSION CORREGIDA Y PULIDA (Recomendada)

lista_moneda = [1, 2, 3, 4, 5]

def lanzar_moneda():
    # Usamos corchetes para pasar una lista a random.choice()
    # Retornamos el resultado directamente para que sea más limpio
    return random.choice(['Cara', 'Cruz'])
    
def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        # Seguimos la consigna exactamente: "se autodestruirá"
        print('La lista se autodestruirá')
        # Devolvemos una lista vacía literalmente para asegurar el resultado
        return []
    else:
        print('La lista fue salvada')
        # Devolvemos la lista intacta
        return lista

# Ejemplo de uso:
# resultado = probar_suerte(lanzar_moneda(), lista_moneda)
# print(resultado)

