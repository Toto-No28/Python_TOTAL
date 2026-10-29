# --- LO QUE ESCRIBES ---
print("--- CÓDIGO CON BUCLE ---")
numeros = [1, 2, 3]
suma = 0

for n in numeros:
    suma = suma + n
    print(f"Sumando {n}... Total: {suma}")

print(f"Resultado final: {suma}")


print("\n" + "="*30 + "\n")


# --- LO QUE PYTHON EJECUTA (TU VISIÓN DE RAYOS X 🩻) ---
print("--- VISIÓN DE RAYOS X (LO QUE PASA REALMENTE) ---")
numeros = [1, 2, 3]
suma = 0

# Vuelta 1 (n vale 1)
n = 1
suma = suma + n
print(f"Sumando {n}... Total: {suma}")

# Vuelta 2 (n vale 2)
n = 2
suma = suma + n
print(f"Sumando {n}... Total: {suma}")

# Vuelta 3 (n vale 3)
n = 3
suma = suma + n
print(f"Sumando {n}... Total: {suma}")

print(f"Resultado final: {suma}")
