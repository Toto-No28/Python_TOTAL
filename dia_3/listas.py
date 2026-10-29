# Crear una lista con diferentes elementos
mi_lista = ['a', 'b', 'c', 'd', 'e']
# len() devuelve el número de elementos en la lista
resultado = len(mi_lista)
print(resultado)
print(type(mi_lista))

print('-' * 30)

# Acceder a un elemento específico usando su índice (empieza en 0)
resultado2 = mi_lista[3]  # El índice 3 corresponde al cuarto elemento ('d')
print(resultado2)
print(type(resultado2))

print('-' * 30)

# Slicing (rebanado): obtener una sub-lista desde el índice 0 hasta el 3 (sin incluir el 3)
resultado3 = mi_lista[0:3] 
print(resultado3)
print(type(resultado3))

print('-' * 30)

# Slicing con pasos: del 0 al 3, saltando de 2 en 2
resultado4 = mi_lista[0:3:2] 
print(resultado4)
print(type(resultado4))

print('-' * 30)

# Concatenación: unir dos listas con el operador +
mi_lista2 = ['f', 'g', 'h', 'i', 'j']
resultado5 = mi_lista + mi_lista2
print(resultado5)
print(type(resultado5))

print('-' * 30)

# Repetición: multiplicar una lista repite sus elementos
resultado6 = mi_lista * 3
print(resultado6)
print(type(resultado6))

print('-' * 30)

# Modificar elementos: las listas son mutables
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = 'alfa' # Cambiamos el primer elemento por 'alfa'
print(mi_lista3)
print(type(mi_lista3))

print('-' * 30)

# append(): agrega un elemento al final de la lista
mi_lista3.append('omega')
print(mi_lista3)
print(type(mi_lista3))

print('-' * 30)

# pop(): elimina y devuelve un elemento por su índice
mi_lista3.pop(4) # Eliminamos el elemento en el índice 4
eliminado = mi_lista3.pop(4) # Eliminamos el NUEVO elemento en el índice 4 (la lista ya cambió)
print(mi_lista3)
print(type(mi_lista3))
print(eliminado)

print('-' * 30)

lista_desordenada = ['z', 'c', 'h', 'a', 'm']
# .sort() ordena la lista en su lugar (modifica la original)
lista_desordenada.sort()
print(lista_desordenada)
print(type(lista_desordenada))

print('-' * 30)

# .sort() por defecto ordena de menor a mayor (ascendente)
# Si le pasamos el argumento reverse=True, lo ordena al revés (descendente)
# Es decir, de la Z a la A, o del número más grande al más pequeño
lista_desordenada.sort(reverse=True)
print(lista_desordenada)

print('-' * 30)

lista_desordenada.sort(reverse=False)
print(lista_desordenada) # Orden ascendente de nuevo (el mismo que .sort() por defecto)

print('-' * 30)

lista_desordenada.reverse()
print(lista_desordenada) # Orden descendente (el mismo que .sort(reverse=True))


print('-' * 30)

# --- Desempaquetado de Listas ---
# APRENDIDO EN: tuples.py
# Funciona igual que en las tuplas: asigna elementos a variables en orden.
datos_lista = ["Juan", "Perez", 30]
lnombre, lapellido, ledad = datos_lista
print(lnombre)
print(lapellido)
print(ledad)
