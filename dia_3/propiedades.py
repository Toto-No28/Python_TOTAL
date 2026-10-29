# Definimos un string de múltiples líneas usando triples comillas
poema = '''Mil pequeños peces blancos
como si hirviera
el color del agua'''

# El operador 'in' verifica si una subcadena existe dentro del string
# Devuelve True si la encuentra, False si no
print('agua' in poema)  # True, porque "agua" está en el poema
print('sol' in poema)   # False, porque "sol" no está en el poema

# El operador 'not in' verifica si una subcadena NO existe dentro del string
# Es la negación de 'in'
print('agua' not in poema) # False, porque "agua" SÍ está
print('sol' not in poema)  # True, porque "sol" NO está

# La función len() calcula la longitud total del string (número de caracteres, incluyendo espacios y saltos de línea)
print(len(poema))


print('Repetición' * 15)