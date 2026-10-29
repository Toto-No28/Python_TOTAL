# Vamos a ver el día de hoy la funcion .index() que nos sirve para encontrar la posicion de un elemento en una lista. De momento, solo vamos a usar el index para encontrar elementos dentro de un solo string.

mi_texto = 'Ésta es una prueba'
resultado = mi_texto[0] # En Python las posiciones empiezan en 0, no en 1.
print(resultado)

#prueba 2 con números positivos
resultado = mi_texto[9] # En Python las posiciones empiezan en 0, no en 1.
print(resultado)

#prueba 3 con números negativos
resultado = mi_texto[-4] # En Python las posiciones empiezan en 0, no en 1.
print(resultado)
# como nota quiero agregar que aunque los número sean negativos, el cero se mantiene en la misma posicion.

#prueba 4 con .index() para encontrar la posicion de un elemento en un string. En este caso el '3'
resultado = mi_texto.index('a')
print(resultado)

# también podemos pedirle que el valor se busque en un rango de posiciones. Por ejemplo, que busque la 'a' a partir de la posicion 5.
resultado = mi_texto.index('a', 5)
print(resultado) # la primera 'a' se encuentra en la posicion 3, pero como le pedimos que busque a partir de la posicion 5, nos devuelve la posicion 10.

# el tercer parámetro nos sirve para indicarle que deje de buscar cuando llegue a esa posición. Por ejemplo, que busque la 'a' a partir de la posicion 5 y que deje de buscar cuando llegue a la posicion 10.
resultado = mi_texto.index('a', 5, 11)
print(resultado) # mencionar que aunque la 'a' se encuentra en la posición 10, si indicamos que el tercer es 10 nos lanza error. Ya que se le indica a python que deje de buscar cuando llegue a la posición 10, es decir, que no incluya la posición 10 en la búsqueda. Por lo que debemos indicar la posición 11 para que incluya la posición 10 en la búsqueda.

# rindex() funciona igual que index(), pero busca de derecha a izquierda.
resultado = mi_texto.rindex('a')
print(resultado)

# rindex() también acepta parámetros para buscar en un rango de posiciones. Aquí el resultado sigue siendo 10.
resultado = mi_texto.rindex('a', 5, 11)
print(resultado)


