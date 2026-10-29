# Operadores aritméticos. Vamos a mostrarlos en f-strings para seguir practicando su uso

x = 2811
y = 1110

print(f'{x} más {y} es igual a {x + y}')
print(f'{x} menos {y} es igual a {x - y}')
print(f'{x} por {y} es igual a {x * y}')
print(f'{x} entre {y} es igual a {x / y}')


print(f'{x} división al piso {y} es igual a {x // y}') # División entera: 2811 entre 1110 cabe 2 veces completas
print(f'{x} módulo de {y} es igual a {x % y}') # Residuo: sobran 591 después de la división entera
print(f'{x} potencia de {y} es igual a {x ** y}') # Potencia: 2811 elevado a la 1110, o sea 2811 se multiplicó por sí mismo 1110 veces

# Aquí presenté cómo hacer una raíz cuadrada anotando 0.5
print(f'La raíz cuadrada de {x} es {x ** 0.5}')
# Aquí tengo el ejemplo con 1/2 (importante anotarlo entre paréntesis)
print(f'La raíz cuadrada de {x} es {x ** (1/2)}')
# Y aquí el ejemplo con Raíz cúbica
print(f'La raíz cúbica de {x} es {x ** (1/3)}') # Raíz Cúbica: se eleva a la 1/3. IMPORTANTE usar paréntesis (1/3)

#aquí termino de experimentar con las raíces. Era necesario saber cómo hacerlo de manera más completa y no solo con la raíz cuadrada. Se consigue el conocimiento al mismo nivel de las "elevaciones" (potencias). 
print(f'La raíz cuarta de {x} es {x ** (1/4)}')
print(f'La raíz quinta de {x} es {x ** (1/5)}')



