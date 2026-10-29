lista_numeros = [1, 2, 3]

print("--- OPCION A: Declarar DENTRO del bucle ---")
for numero in lista_numeros:
    # Si la declaras aquí, la variable "nace" de nuevo en cada vuelta
    cuenta_dentro = 0 
    cuenta_dentro = cuenta_dentro + numero
    print(f"Sumando {numero}... Total acumulado: {cuenta_dentro}")

# Al final, 'cuenta_dentro' solo recordará lo que pasó en la ÚLTIMA vuelta
print(f"RESULTADO FINAL (Opcion A): {cuenta_dentro}") 


print("\n" + "="*30 + "\n")


print("--- OPCION B: Declarar FUERA del bucle ---")
# Aquí la variable "nace" antes de empezar a girar
cuenta_fuera = 0 
for numero in lista_numeros:
    # Aquí solo la actualizamos, no la reiniciamos
    cuenta_fuera = cuenta_fuera + numero
    print(f"Sumando {numero}... Total acumulado: {cuenta_fuera}")

print(f"RESULTADO FINAL (Opcion B): {cuenta_fuera}")
