import random

if 10 > 5:
    print('Es correcto')

print('-' * 50)

mascota = input("¿Qué mascota tienes? ").lower()
if mascota == 'perro':
    print('Tu mascota es un cánido')
elif mascota == 'gato':
    print('Tu mascota es un felino')
else:
    print('No sé qué mascota tienes')

print('-' * 50)

# El Portero de la Discoteca (Básico)
edad = int(input('¿Cuántos años tienes? '))
if edad >= 18:
    print('¡Adelante, diviértete!')
else:
    print('Lo siento, no puedes pasar.')

print('-' * 50)

# Calificador de Notas
calificacion = int(input('¿Cuál es tu calificación? '))
if calificacion >= 90:
    print('Excelente (A)')
elif calificacion >= 80:
    print('Muy bien (B)')
elif calificacion >= 70:
    print('Bien (C)')
else:
    print('Necesitas mejorar (F)')      

print('-' * 50)

# Adivina el número
numero = random.randint(1, 10)
adivina = int(input('Adivina el número: '))
if adivina < numero:
    print('Demasiado bajo')
elif adivina > numero:
    print('Demasiado alto')
else:
    print('¡Correcto!')

print('-' * 50)

# Adivina el número (while)
numero_secreto = random.randint(1, 100)
adivina = None

while adivina != numero_secreto:
    adivina = int(input("Adivina el número (1-100): "))
    if adivina < numero_secreto:
        print("Demasiado bajo")
    elif adivina > numero_secreto:
        print("Demasiado alto")
    else:
        print(f"¡Correcto! El número secreto era {numero_secreto}")






