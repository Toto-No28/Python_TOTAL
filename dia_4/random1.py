# Buenas prácticas: Se prefiere "import random" sobre "from random import *" 
# para mantener el espacio de nombres limpio y saber de dónde vienen las funciones.
import random

# randint(a, b): Devuelve un entero aleatorio entre a y b (incluyendo ambos).
aleatorio = random.randint(1, 50)
print(aleatorio)

print('-' * 50)

# uniform(a, b): Devuelve un float aleatorio entre a y b.
aleatorio2 = random.uniform(1, 50)
print(aleatorio2)
# Tip: round(valor, decimales) ayuda a limpiar la salida de los floats.
print(round(aleatorio2, 2))

print('-' * 50)

# random(): Devuelve un float aleatorio entre 0.0 y 1.0. 
# Es la base de muchas otras funciones del módulo.
aleatorio3 = random.random()
print(aleatorio3)
print(round(aleatorio3, 2))

print('-' * 50)

colores = ['rojo', 'azul', 'verde', 'amarillo', 'negro', 'blanco']

# choice(): Selecciona UN solo elemento de una secuencia.
color_elegido = random.choice(colores)
print(color_elegido)

# choices(seq, k=n): Selecciona n elementos PERMITIENDO que se repitan.
colores_repetibles = random.choices(colores, k=3)
print(colores_repetibles)

print('-' * 50)

# sample(seq, k=n): Selecciona n elementos ÚNICOS de una secuencia (sin repetición).
# Importante: n no puede ser mayor al tamaño de la lista original.
colores_unicos = random.sample(colores, 3)
print(colores_unicos)

print('-' * 50)

# shuffle(): Mezcla/Baraja los elementos de una lista "in-place" (modifica la original).
# CASO ESPECIAL: shuffle() solo funciona con objetos MUTABLES (como listas).
# NO puedes usar shuffle() con un string directamente porque son inmutables.
random.shuffle(colores)
print(colores)

numero = list(range(5, 51, 5))
print(numero)

# Mezclando una lista generada por un range (convertida a lista antes)
random.shuffle(numero)
print(numero)

# Nota de seguridad: El módulo random NO debe usarse para fines criptográficos 
# (como contraseñas o tokens de seguridad). Para eso, usa el módulo 'secrets'.
