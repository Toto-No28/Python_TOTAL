# Aquí tenemos el uso más básico de las variables
nombre = 'Salvador'
print(nombre)

# También podemos cambiar el contenido de la variable, y ésta se lee por Python de arriba a abajo
nombre = 'Guadalupe'
print(nombre)
print('-' * 30)

# Aquí presento variables con números
edad = 30
print(edad)

# De mismo modo podemos ejecutar operaciones matemáticas con la variables
edad = 30
edad2 = 15
print(edad + edad2)
print('-' * 30)

# También podemos usar funciones "input" para guardar los datos que usuario ingrese a una variable de manera directa
nombre = input('¿Cuál es tu nombre? ')
print(f'Enacntado de conocerte, {nombre}!')
print('-' * 30)

# También podemos hacer la "suma" de strings, esto se conoce como concatenación
nombre = 'Salvador'
apellido = 'Suárez Chacón'
print(nombre + ' ' + apellido)

# Pero prefiero el uso de las comas, ya que es más limpio y legible
print(nombre, apellido)
print('-' * 30)

# También podemos concatenar variables
nombre1 = 'Python'
nombre2 = 'TOTAL'
titulo = nombre1 + ' ' + nombre2
print(titulo)

