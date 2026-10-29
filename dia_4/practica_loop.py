# ---------------------------------------------------------
# EJERCICIO: CALCULADORA DE DESCUENTOS
# ---------------------------------------------------------
# Tienes una lista de precios de productos en una tienda.
# Hoy hay un descuento especial del 20% en toda la tienda.
#
# TU TAREA:
# 1. Crea un bucle 'for' que recorra la lista 'precios_sin_descuento'.
# 2. DENTRO del bucle, crea una variable temporal llamada 'precio_final'.
# 3. La variable 'precio_final' debe ser el precio original menos el 20%.
#    (Pista: multiplicar por 0.8 es una forma rápida de calcular el 80% restante).
# 4. Imprime el resultado con este formato: 
#    "El producto de $100 queda en $80.0"
# ---------------------------------------------------------

precios_sin_descuento = [100, 250, 400, 15, 80]

# Escribe tu código aquí abajo:
# (Recuerda cuidar la indentación)
ahorro = 0
for precio in precios_sin_descuento:
    # --- TU ESPACIO DE TRABAJO ---
    # Paso 1: Calcula el precio con descuento y guárdalo en una variable.
    precio_final = precio * 0.8
    ahorro = ahorro + precio * 0.2
    
    # Paso 2: Imprime el mensaje usando f-string.
    print(f"El producto de ${precio} queda en ${precio_final}")
print(f"El ahorro total es de ${ahorro}")

