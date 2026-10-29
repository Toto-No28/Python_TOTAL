# Primero veremos el uso de los enteros
mi_numero = 1
print(mi_numero)

print(type(mi_numero)) #El uso de type siempre nos va a servir para saber que tipo de dato es el que estamos utilizando
print('-' * 30)

# Aqui también presento el uso de los decimales
mi_numero = 5.89
suma_numero = mi_numero + mi_numero # tambien podemos usar el operador + para sumar el valor de la variable por si mismo
multiplicacion_numero = mi_numero * 2 # tambien podemos usar el operador * para multiplicar el valor de la variable por si mismo
print(suma_numero)
print(multiplicacion_numero)
print(type(suma_numero))
print(type(multiplicacion_numero))
print('-' * 30)

#Tenemos que dejar claro que cualquier dato ingresado por el usuario siempre será considerado como un string, por lo tanto, si queremos realizar operaciones matemáticas con él, debemos convertirlo a un entero o a un decimal
numero = input('Ingresa un numero: ')
print(type(numero))
numero = int(numero)
print(type(numero))
numero = float(numero)
print(type(numero))
print('-' * 30)

num1 = 7.5
num2 = 2.5
print(num1 + num2)
print(type(num1 + num2)) #La única manera de que el resultado sea un integer es que ambos numeros sean integers, o que transformemos el resultado a un integer de manera manual como a continuación se muestra
print(int(num1 + num2))
print(type(int(num1 + num2)))
