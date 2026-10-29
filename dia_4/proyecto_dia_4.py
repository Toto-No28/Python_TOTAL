# ---------- ADIVINA EL NÚMERO----------
import random

nombre = input(
    "Bienvenido al juego ADIVINA EL NÚMERO!!!\nPor favor ingresa tu nombre: "
)

print(f"Hola {nombre}, ahora vamos a jugar")

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

print("Tienes 8 intentos para adivinar un número entre 1 y 100.")

# El bucle se repite mientras los intentos sean menores a 8.
# Usamos < 8 para evitar un 9no intento (ya que el contador empieza en 0).
while intentos < 8:
    intentos += 1
    # "adivina" captura la entrada, la convierte a entero y la guarda para comparar.
    adivina = int(input(f"Intento {intentos}: Adivina el número: "))

    if adivina < 1 or adivina > 100:
        print("Has elegido un número que no está permitido")
    elif adivina < numero_secreto:
        print("Demasiado bajo")
    elif adivina > numero_secreto:
        print("Demasiado alto")
    else:
        print(
            f"¡Correcto! El número secreto era {numero_secreto}. Te tomó {intentos} intentos."
        )
        # "break" detiene el bucle inmediatamente al ganar para no seguir pidiendo números.
        break

# Verificamos si el jugador perdió (si salió del bucle sin adivinar).
if adivina != numero_secreto:
    print(
        f"Lo siento, has agotado tus 8 intentos. El número secreto era {numero_secreto}"
    )
