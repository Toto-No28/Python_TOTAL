# --- DIFERENCIA ENTRE COMPRESIÓN DE LISTAS Y ACUMULACIÓN ---

# Datos de origen
valores = [10, 20, 30, 40, 50]

print(f"Datos originales: {valores}")
print("-" * 50)

# 1. ACUMULACIÓN TRADICIONAL (Bucle for)
# El objetivo es obtener un ÚNICO valor final (un total).
total_acumulado = 0
for v in valores:
    total_acumulado += v  # Vamos sumando uno a uno a la variable externa

print(f"1. Total acumulado (con loop for): {total_acumulado}")
# NOTA: Usar for es mejor cuando el proceso es complejo o requiere varios pasos intermedios.


# 2. TRANSFORMACIÓN (Compresión de listas)
# El objetivo es obtener una NUEVA LISTA con cambios en cada elemento.
valores_con_iva = [v * 1.21 for v in valores]

print(f"2. Nueva lista con IVA (compresión): {valores_con_iva}")
# NOTA: Aquí no acumulamos nada en una variable externa, 
# simplemente "proyectamos" una nueva lista basada en la anterior.


# 3. EL "HÍBRIDO" (Compresión + Función de agregación)
# Si queremos un total (acumulación) pero escrito de forma compacta.
# Primero se genera la lista comprimida y luego sum() la reduce a un solo número.
total_compacto = sum([v for v in valores if v > 25])

print(f"3. Suma de valores > 25 (híbrido): {total_compacto}")
# NOTA: Esta es la forma "Pythonic" de hacer acumulaciones simples en una línea.


print("-" * 50)
# RESUMEN MENTAL:
# ¿Quieres UNA LISTA nueva? -> Usa Compresión.
# ¿Quieres UN SOLO VALOR total? -> Usa Bucle for (o Compresión + sum()).
# ¿Quieres hacer algo complejo (como imprimir o guardar en BD) mientras recorres? -> Usa Bucle for.
