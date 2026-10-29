# conversión implícita
num1 = 20
num2 = 30.5
print(type(num1)) # Es un integer
print(type(num2)) # Es un float
print(type(num1 + num2)) # Es un float porque python convierte el integer a float para realizar la operación. Se califica como "implícita" ya que no tenemos que interferir en la conversión.
print('-' * 30)

# conversión explícita
num3 = 5.8
print(num3)
print(type(num3))
# Si hago la conversión de float a integer, python elimina los decimales, sin redondear.
num4 = int(num3)
print(num4)
print(type(num4))
print('-' * 30)

#vamos a trabajar con el ejemplo de los datos ingresados por el usuario, en este caso con la edad.

edad = input('¿Dime qué edad tienes a la fecha del día de hoy? ')
print(type(edad))

# Como podemos ver, el dato ingresado por el usuario es de tipo string, por lo que debemos convertirlo a integer para poder realizar operaciones matemáticas con él.

edad = int(edad)
print(type(edad))

# Ahora si podemos realizar operaciones matemáticas con la variable edad.
print(edad + 5) # Suma
print(edad - 5) # Resta
print(edad * 5) # Multiplicación
print(edad / 5) # División (siempre devuelve float)
print(edad // 5) # División entera (sin decimales)
print(edad % 5) # Módulo o residuo (lo que sobra de la división)
print(edad ** 5) # Potenciación (elevado a la potencia)

print('-' * 30)

#Ejercicio
num1 = "7.5"
num2 = "10"
# para poder hacer las sumas dentro del print es necesario convertir los strings a float por separado.
print(float(num1) + float(num2))