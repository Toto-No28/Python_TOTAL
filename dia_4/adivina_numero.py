import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("Tienes 8 intentos para adivinar un número entre 1 y 100.")

while intentos <= 8:
    intentos += 1
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
        break

if adivina != numero_secreto:
    print(
        f"Lo siento, has agotado tus 8 intentos. El número secreto era {numero_secreto}"
    )
