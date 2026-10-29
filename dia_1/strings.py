# Los string pueden tener "concatenaciones". Eso quiere decir que podemos unir strings con el operador "+"
print('Hola' + ' ' + 'Mundo')
print('-' * 30)
# El "\" (barra invertida) sirve para poder poner comillas dentro de un string
print("Me llamo \"Salvador\"")
# Éste es un ejemplo en inglés de como funciona el "\" (barra invertida)
print('I\'m Salvador')
print('-' * 30)
# El "\n" sirve para poder poner un salto de línea dentro de un string
print('Ésta es la primnera línea\nY ésta es la segunda línea')
print('-' * 30)
# El "\t" sirve para poder poner una tabulación dentro de un string 
print('Ésta es la primnera línea\tY ésta es la segunda línea')
print('-' * 30)
# El "\r" (retorno de carro) mueve el cursor al inicio de la línea, permitiendo sobrescribir el texto
print('Ésta es la primnera línea\rY ésta es la segunda línea')
print('-' * 30)
# El "\b" (retroceso) mueve el cursor una posición hacia atrás
print('Ésta es la primnera línea\bY ésta es la segunda línea')
print('-' * 30)
# Aquí pongo un ejemplo de como funciona el "\b" (retroceso) en mayor cantidad de carácteres
print('Ésta es la primnera línea' + '\b' * 10 + 'Y ésta es la segunda línea')
print('-' * 30)
# para anotar una barra invertida dentro de un string se debe poner "\\"
print('Éste símbolo \\ es una barra invertida')
print('-' * 30)

#EJERCICIOS
#1
print('Línea 1\nLínea 2\nLínea 3')
#2
print('A\tB\tC\nD\tE\tF\nG\tH\tI')
#3
print('Barra Normal: /')
print('Barra Invertida: \\')
#Versión 2
print('Barra Normal: /\nBarra Invertida: \\')