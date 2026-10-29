lista_frutas = ['manzana', 'banana', 'cereza']

for fruta in lista_frutas:
    print(fruta)

# --- DEMOSTRACIÓN DE PERSISTENCIA ---
# En Python, la variable del bucle ('fruta') NO muere cuando el bucle termina.
# Se queda con el valor de la última iteración.
print(f"\nFuera del loop, la variable 'fruta' sigue viva y contiene: {fruta}")

# --- BUENAS PRÁCTICAS ---
# Aunque técnicamente la variable sigue existiendo, la regla de oro es:
# "Finge que la variable de iteración NO existe fuera del bucle".
#
# ¿Por qué?
# 1. Legibilidad: El código es más limpio si las variables de iteración son efímeras.
# 2. Seguridad: Si la lista 'lista_frutas' estuviera vacía, el bucle nunca 
#    se ejecutaría y la variable 'fruta' nunca se crearía. Intentar usarla 
#    causaría un error (NameError).

print('-' * 50)

lista_nombres = ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro']
# Hago uso de la "variable temporal" para guardar el valor de cada elemento de la lista
# en cada iteración. En este caso, la variable temporal es 'nombre'.
for nombre in lista_nombres:
    print(f'Hola, {nombre}!')


abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letra in abecedario:
    numero_letra = abecedario.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')

print('\n' + '=' * 50 + '\n')

# -------------------------------------------------------------------------
# --- RESUMEN DE CONCEPTOS: ITERADORES, VARIABLES TEMPORALES Y ACUMULADORES
# -------------------------------------------------------------------------

# 1. ITERADOR (La variable del ciclo):
#    Es la variable que toma un valor diferente automáticamente en cada vuelta.
#    Es el INPUT de tu proceso (ej: 'precio' abajo).

# 2. VARIABLE TEMPORAL (La variable de proceso):
#    Se crea, se usa y muere (o se reinicia) DENTRO de cada vuelta.
#    No guarda historia de lo que pasó en la vuelta anterior (ej: 'precio_final').

# 3. ACUMULADOR EXTERNO (La alcancía):
#    Se crea FUERA del bucle y sobrevive a todas las vueltas.
#    Sirve para guardar totales, sumas o conteos globales (ej: 'ahorro_total').


# --- EJEMPLO PRÁCTICO: CALCULADORA DE DESCUENTOS Y AHORRO ---

precios_sin_descuento = [100, 250, 400, 15, 80]
ahorro_total = 0 # <--- ACUMULADOR (La alcancía empieza vacía FUERA del loop)

print("Iniciando cálculos...")

for precio in precios_sin_descuento: # <--- ITERADOR (precio actual)
    
    # VARIABLE TEMPORAL: Se calcula y muere en esta misma vuelta
    # Solo nos sirve para mostrar el dato en el print de abajo.
    precio_final = precio * 0.8 
    
    # ACUMULACIÓN: Metemos el ahorro a la alcancía externa.
    # Usamos el Operador de Asignación Aditiva (+=)
    # "ahorro_total += X" es una forma corta de decir "ahorro_total = ahorro_total + X"
    ahorro_total += precio * 0.2 
    
    print(f"El producto de ${precio} queda en ${precio_final}")

# Al terminar el bucle, imprimimos lo que quedó en la alcancía
print(f"\nEl ahorro total acumulado es de: ${ahorro_total}")

print('\n' + '-' * 50 + '\n')

lista_nombres2 = ['Ana', 'Luis', 'Carlos', 'Marta', 'Pedro', 'Salvador', 'Luisa', 'Miguel']

for nombre in lista_nombres2:
    if nombre.startswith('L'):
        print(nombre)

print('\n' + '-' * 50 + '\n')

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mi_acumulador = 0
# Éste ejemplo ya lo tengo demasiado claro jajajajaja
for numero in lista_numeros:
    mi_acumulador += numero

print(mi_acumulador)

print('\n' + '-' * 50 + '\n')

oracion = "Hola, ¿cómo estás?"
for letra in oracion:
    print(letra)

print('\n' + '-' * 50 + '\n')

# Vamos a ver  la función de dos variables temporales

lista_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lista in lista_listas:
    for numero in lista:
        print(numero)

for a, b, c in lista_listas:
    print(a, b, c)