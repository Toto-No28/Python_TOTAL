palabra = "python"

# --- MÉTODO TRADICIONAL ---
# Útil cuando la lógica interna es muy compleja o requiere múltiples pasos.
lista = []
for letra in palabra:
    lista.append(letra)

print(lista)

print('-' * 50)

# --- COMPRESIÓN DE LISTAS BÁSICA ---
# Sintaxis: [expresión for elemento in iterable]
# Ventaja: Más legible y eficiente en términos de rendimiento.
lista2 = [letra for letra in palabra]
print(lista2)

print('-' * 50)

# --- COMPRESIÓN CON FILTRADO (if al final) ---
# Sintaxis: [expresión for elemento in iterable if condición]
# El "if" al final actúa como un FILTRO (solo incluye si cumple).
# [ Resultado transformado | Origen | Condición ]
lista3 = [letra.upper() for letra in palabra if letra != 'o']
print(f"Filtrando la 'o' y pasando a Mayúsculas: {lista3}")

print('-' * 50)

# --- COMPRESIÓN CON OPERACIONES ---
# Podemos aplicar operaciones matemáticas directamente en el resultado.
lista4 = [numero for numero in range(0, 21, 2)]
print(f"Rango original (pares): {lista4}")

# Alteramos el valor multiplicado por 2
lista5 = [numero * 2 for numero in range(0, 21, 2)]
print(f"Valores multiplicados * 2: {lista5}")

print('-' * 50)

# --- COMPRESIÓN CON LÓGICA IF / ELSE (if al principio) ---
# OJO: Cuando hay un "else", la estructura cambia y el bloque condicional va ANTES del "for".
# Sintaxis: [valor_si_true if condición else valor_si_false for elemento in iterable]
lista6 = [numero if numero * 2 > 10 else "no cumple" for numero in range(0, 21, 2)]
print(f"Lista con validación if/else: {lista6}")


# --- BUENAS PRÁCTICAS ---
# 1. LEGIBILIDAD: Si la comprensión ocupa más de una línea o es muy difícil de leer, 
#    es mejor usar un bucle 'for' tradicional. El código se lee más veces de las que se escribe.
# 2. PROPÓSITO: Úsala para CREAR listas. No la uses para ejecutar funciones que cambien 
#    cosas fuera (efectos secundarios), para eso usa un bucle normal.
# 3. COMPLEJIDAD: Evita las "Compresiones anidadas" (una dentro de otra) a menos que 
#    sea estrictamente necesario, ya que se vuelven imposibles de depurar.

print('-' * 50)

# EJERCICIO: Crear una lista valores_cuadrado con los números de la lista valores elevados al cuadrado.
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [n**2 for n in valores]

print(f"Lista original: {valores}")
print(f"Lista al cuadrado: {valores_cuadrado}")

print('-' * 50)

# EJERCICIO: Crear una lista valores_pares con los números de 'valores' que sean pares.
valores_pares = [n for n in valores if n % 2 == 0]

print(f"Números pares: {valores_pares}")

print('-' * 50)

# EJERCICIO: Convertir temperaturas de Fahrenheit a Celsius
# Fórmula: (F - 32) * (5/9)
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n - 32) * (5 / 9) for n in temperatura_fahrenheit]

print(f"Fahrenheit: {temperatura_fahrenheit}")
print(f"Celsius: {grados_celsius}")




