#1. debemos pedir el nombre del usuario

nombre = input('Por favor, ingrese su nombre: ')

#2. debemos solicitar el total de las ventas que hizo el usuario

venta = float(input('Por favor, Ingrese el toal de sus ventas: $'))

#3. debemos calcular el 13% de las ventas

comision = round(venta * 0.13, 2)

#4. debemos mostrar un f-string con el nombre del usuario y el total de las ventas

print(f'El usuario {nombre} obtuvo una comision de ${comision}')
