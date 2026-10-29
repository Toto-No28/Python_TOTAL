
print("--- Experimento con enteros y colisiones ---")
# El tamaño inicial de un set suele ser 8 (indices 0-7).
# hash(0) = 0 -> index 0
# hash(8) = 8 -> index 0 (colisión!)

s1 = {0, 8}
print(f"Set {{0, 8}}: {s1}") 
# Si el 0 entra primero, ocupa el slot 0. El 8 choca y busca otro slot.
# Al iterar, recorre la memoria en orden. Debería ver primero el 0.

s2 = {8, 0}
print(f"Set {{8, 0}}: {s2}")
# Si el 8 entra primero, ocupa el slot 0 (8 % 8 == 0). El 0 choca y busca otro.
# Al iterar, debería ver primero el 8.

print("\n--- Experimento con valores negativos ---")
# hash(-1) usualmente es -2 en Python (el valor -1 está reservado internamente para errores)
# hash(-2) es -2.
print(f"Hash de -1: {hash(-1)}")
print(f"Hash de -2: {hash(-2)}")
# Veamos cómo se ordenan
s3 = {-1, -2}
print(f"Set {{-1, -2}}: {s3}")

print("\n--- Strings y Randomización ---")
colores = {"Rojo", "Verde", "Azul"}
print(f"Set de colores: {colores}")
for c in colores:
    pass
for c in colores:
    h = hash(c)
    print(f"Item: {c}, Hash: {h}, Aprox Index (h & 7): {h & 7}")
