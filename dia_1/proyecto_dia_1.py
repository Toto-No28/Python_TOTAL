print('Bienvenido a la creación de tu propia marca de cerveza!')
print(input('Me encantaría que primero me compartieras cuál es tu animal y tu color favoritos.\nPresiona Enter cuando estés listo!'))
#Primero tenemos que guardar datos en variables
animal = input('Cuál es tu animal favorito? ').capitalize()
color = input('Cuál es tu color favorito? ').capitalize() #.capitalize() sirve para que la primera letra sea mayuscula
print('Tu animal favorito es', animal, 'y tu color favorito es', color)
print(f'Tu cerveza se llama: "{animal} {color}"!') #f-string sirve para insertar variables dentro de una cadena de texto.
print('Gracias por tu tiempo!')