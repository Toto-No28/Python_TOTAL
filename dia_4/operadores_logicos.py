# El primer operador que trabajaremos es 'and', este operador nos permite combinar dos condiciones y nos devolverá True si ambas condiciones son verdaderas, de lo contrario nos devolverá False

mi_bool = (55 == 55) and ('perrito' == 'perrito')
print(mi_bool)

mi_bool = (55 == 55) and ('perrito' == 'gato')
print(mi_bool)

mi_bool = (55 == 550) and ('perrito' == 'perrito')
print(mi_bool)

mi_bool = (55 == 550) and ('perrito' == 'gato')
print(mi_bool)

# La única manera que 'and' sea True es que ambos comparadores sean True
print('-' * 50)
# El siguiente operador es 'or', este operador nos permite combinar dos condiciones y nos devolverá True si al menos una de las condiciones es verdadera, de lo contrario nos devolverá False

mi_bool = (55 == 55) or ('perrito' == 'perrito')
print(mi_bool)

mi_bool = (55 == 55) or ('perrito' == 'gato')
print(mi_bool)

mi_bool = (55 == 550) or ('perrito' == 'perrito')
print(mi_bool)

mi_bool = (55 == 550) or ('perrito' == 'gato')
print(mi_bool)

# La única manera que 'or' sea False es que ambos comparadores sean False
print('-' * 50)
# El siguiente operador es 'not', este operador nos permite negar una condición y nos devolverá True si la condición es False, de lo contrario nos devolverá False

mi_bool = not (55 == 55)
print(mi_bool)

mi_bool = not (55 == 550)
print(mi_bool)

# La única manera que 'not' sea True es que el comparador sea False