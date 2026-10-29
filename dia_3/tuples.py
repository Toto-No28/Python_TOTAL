# --- Tuplas ---
# Son inmutables (no se pueden modificar).
# Son muy útiles para datos que no deben cambiar, como configuración o coordenadas.

mi_tuple = (1, 2, 3, 4, 5)
print(type(mi_tuple))

# Acceso a elementos
print(mi_tuple[0])
print(mi_tuple[-1])

# Podemos tener tuples dentro de otras (Tuplas Anidadas)
# Esto es útil para crear estructuras de datos complejas, como una matriz o una lista de coordenadas.
# Por ejemplo: coordenadas de un viaje = ((x1, y1), (x2, y2))
mi_tuple2 = (1, 2, (3, 4, 5))
print(mi_tuple2)
print(mi_tuple2[2][0]) # Accedemos al primer elemento de la tupla interna

# Desempaquetado de tuplas (Tuple Unpacking)
# Permite asignar los valores de una tupla a variables individuales en una sola línea.
# IMPORTANTE: El número de variables debe ser IGUAL al número de elementos en la tupla.
nombre, edad, ciudad = ("Juan", 25, "México")

# Esto es equivalente a hacer:
# nombre = "Juan"
# edad = 25
# ciudad = "Mexico"

print(nombre)
print(edad)
print(ciudad)

# --- BONUS: Desempaquetado en otras estructuras ---
# El desempaquetado NO es exclusivo de las tuplas.
# Funciona con cualquier estructura iterable (Listas, Diccionarios, etc.)
# IMPORTANTE: Aprendimos esto aquí, en el tema de Tuplas.

# 1. Desempaquetado de Listas
# Funciona EXACTAMENTE igual.
mi_lista = ["Manzana", "Banana", "Cereza"]
x, y, z = mi_lista  # x="Manzana", y="Banana", z="Cereza"

# 2. Desempaquetado de Diccionarios
# OJO: Por defecto, solo obtienes las CLAVES.
mi_dic = {"nombre": "Ana", "edad": 30}
a, b = mi_dic  # a="nombre", b="edad"

# Para obtener VALORES:
v1, v2 = mi_dic.values() # v1="Ana", v2=30

# Para obtener AMBOS (Tuplas):
i1, i2 = mi_dic.items() # i1=("nombre", "Ana"), i2=("edad", 30)

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(3))
print(type(mi_tupla.count(3)))

# --- Conversión de Tupla a Lista (Casting) --- 
# Las tuplas son inmutables, pero podemos convertirlas a listas para modificarlas.
tupla_original = (1, 2, 3)
lista_convertida = list(tupla_original) # Usamos la función list()

print(lista_convertida)
lista_convertida[0] = "Cambio" # Ahora sí podemos modificarla
print(lista_convertida)

# Podemos volver a convertirla a tupla
tupla_nueva = tuple(lista_convertida) 
print(tupla_nueva)