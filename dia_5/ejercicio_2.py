'''Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido", debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']'''

import unicodedata

def letras_unicas(palabra):
    # 1. Normalización NFD: Descompone caracteres (ej: 'é' se convierte en 'e' + '´')
    palabra = unicodedata.normalize('NFD', palabra)
    
    # 2. Filtrado y Reconstrucción: 
    # Recorre cada carácter (c) y lo mantiene solo si NO es de categoría 'Mn' (acentos)
    # El ''.join() vuelve a unir los caracteres sobrevivientes en un solo string
    palabra = ''.join(c for c in palabra if unicodedata.category(c) != 'Mn')
    
    # 3. Normalización a minúsculas (para que 'A' y 'a' se cuenten como la misma letra)
    palabra = palabra.lower()
    
    # 4. Eliminar duplicados con set() y ordenar alfabéticamente con sorted()
    letras = set(palabra)
    return sorted(letras)

print(letras_unicas("murciélago"))
    
    