monedas = 5

while monedas > 0:
    print(f'Tengo {monedas} monedas.')
    monedas = monedas - 1

print('-' * 50)

monedas = 10

while monedas > 0:
    print(f'Tengo {monedas} monedas.')
    monedas -= 1 # Esta es la escritura "Pythonica" de monedas = monedas - 1
else:
    print('Se acabaron las monedas')

print('-' * 50)

nombre = input('¿Cómo te llamas? ')

for letra in nombre:
    if letra == 'o':
        break
    print(letra)

print('-' * 50)

for letra in nombre:
    if letra == 'o':
        continue
    print(letra)