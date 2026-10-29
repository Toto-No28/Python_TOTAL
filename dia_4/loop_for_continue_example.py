
# -------------------------------------------------------------------------
# --- USO DE 'continue' ---
# -------------------------------------------------------------------------
# La instrucción 'continue' sirve para saltar el resto de código de la 
# iteración actual y pasar inmediatamente a la siguiente.

print('\n' + '=' * 50 + '\n')
print("Ejemplo de 'continue': Imprimir números pares del 0 al 9")

for numero in range(10):
    if numero % 2 != 0:
        continue # Si es impar, salta a la siguiente vuelta del bucle
    
    print(numero) # Solo se ejecuta si NO se hizo 'continue'
