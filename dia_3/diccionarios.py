# --- Estructura Básica ---
# Los diccionarios guardan pares de CLAVE: VALOR.
# Nota importante: Las claves (keys) son ÚNICAS, pero los valores pueden repetirse.
diccionario = {'c1': 'valor1', 'c2': 'valor1'} 
print(diccionario)

# --- Acceder a Valores ---
# Para obtener un valor, usamos su clave entre corchetes []
resultado = diccionario['c1']
print(resultado)

# --- Ejemplo Realista ---
# Un diccionario puede guardar diferentes tipos de datos (strings, números, etc.)
cliente = {
    'nombre': 'Juan', 
    'apellido': 'Fuentes', 
    'peso': 88, 
    'talla': 1.76
}
# La estructura anterior es correcta porque Python permite saltos de linea dentro de {}.
# Esto hace que sea mucho mas legible, similar a CSS o JSON.
consulta = (cliente['apellido'])
print(consulta)

# --- Claves Repetidas ---
# ¿Qué pasa si intento repetir una clave?
# Python NO da error, pero solo guarda el ÚLTIMO valor asignado a esa clave.
dic_repetido = {'a': 1, 'a': 2}
print(dic_repetido) # Imprimirá solo {'a': 2}, el 1 se perdió.


# --- Listas dentro de Diccionarios ---
dic = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
# Podemos acceder encadenando: [clave] -> [indice de lista] -> metodo()
print(dic['c2'][1].upper())

# --- Diccionario con Claves Numéricas ---
dic = {1: 'a', 2: 'b'}
print(dic)

# --- Agregar nuevos elementos ---
# Si la clave no existe, se crea nueva.
dic[3] = 'c'
print(dic)

# --- Modificar elementos existentes ---
# Si la clave YA existe, se reemplaza su valor (son mutables).
dic[2] = 'B'
print(dic)

# --- Métodos útiles ---
# .keys(): Devuelve una vista de todas las claves.
# .values(): Devuelve una vista de todos los valores.
# .items(): Devuelve una vista de tuplas (clave, valor).
print(dic.keys())
print(dic.values())
print(dic.items())

print('-' * 30)

# --- Desempaquetado de Diccionarios ---
# APRENDIDO EN: tuples.py
# Por defecto desempaqueta las CLAVES.
mi_dicc = {'a': 1, 'b': 2}
k1, k2 = mi_dicc
print(k1)
print(k2)

# Para valores usamos .values()
v1, v2 = mi_dicc.values()
print(v1)
print(v2)

# Para items (tuplas clave-valor) usamos .items()
i1, i2 = mi_dicc.items()
print(i1)
print(i2)