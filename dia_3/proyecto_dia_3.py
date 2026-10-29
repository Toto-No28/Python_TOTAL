# Crear un programa que primero le pida al usuario que ingrese un texto.
print("Hola, bienvenido al programa de análisis de texto.")
texto_original = input("Ingrese su texto, por favor: ")

# 1. Convertimos todo a minúsculas
# Trabajamos sobre una copia ('texto') para no perder el formato original del usuario en 'texto_original'.
texto = texto_original.lower()

# 2. Reemplazamos manualmente las vocales con acento (la ñ no se toca)
texto = texto.replace("á", "a")
texto = texto.replace("é", "e")
texto = texto.replace("í", "i")
texto = texto.replace("ó", "o")
texto = texto.replace("ú", "u")
texto = texto.replace("ü", "u")

print('-' * 50)

# Luego, el programa le va a pedir al usuario que también ingrese tres letras a su elección.
print("Ahora, por favor, ingrese tres letras a su elección.")
letra1 = input("Ingrese la primera letra: ").lower()
letra2 = input("Ingrese la segunda letra: ").lower()
letra3 = input("Ingrese la tercera letra: ").lower()

print('-' * 50)

# Finalmente, el programa debe mostrar:
# 1- ¿Cuántas veces aparece cada una de las letras que eligió?
# Agregé .upper() para que la letra se muestre en mayúscula. (Elección personal)
print(f"La letra '{letra1.upper()}' aparece <{texto.count(letra1)}> veces.")
print(f"La letra '{letra2.upper()}' aparece <{texto.count(letra2)}> veces.")
print(f"La letra '{letra3.upper()}' aparece <{texto.count(letra3)}> veces.")

print('-' * 50)

# 2- Le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto.
# Usamos .split() para crear una lista con todas las palabras del texto (separadas por espacios).
# Luego usamos len() para contar cuántos elementos (palabras) hay en esa lista.
print(f"Hay <{len(texto.split())}> palabras en su texto.")

print('-' * 50)

# 3- Nos va a informar cuál es la primera letra del texto y cuál es la última.
# Usamos una lista de comprensión para obtener SOLO las letras, asegurando que el último elemento sea una letra y no un signo.
letras_solo = [c for c in texto if c.isalpha()]
print(f"La primera letra del texto es '{texto[0].upper()}' y la última es '{letras_solo[-1].upper()}'.")

print('-' * 50)

# 4- El sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
# Separamos el texto en palabras con split(), invertimos el orden con [::-1] y unimos todo de nuevo con join().
print(f"El texto invertido es: {' '.join(texto_original.split()[::-1])}")

print('-' * 50)

# 5- Nos va a decir si la palabra "python" aparece dentro del texto.
if "python" in texto:
    print("La palabra 'Python' sí aparece en el texto.")
else:
    print("La palabra 'Python' no aparece en el texto.")
