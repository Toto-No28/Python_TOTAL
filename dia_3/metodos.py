texto = 'Éste es el texto de Salvador'

resultado = texto.upper() # Hace el texto en mayúsculas. Los métodos son acompañados de paréntesis () y pueden recibir parámetros. En este caso no recibe ninguno, y aún así funcionará

print(resultado)
print('-' * 30)

resultado2 = texto.lower() # Convierte el texto a minúsculas

print(resultado2)
print('-' * 30)

resultado3 = texto.capitalize() # Convierte la primera letra a mayúscula

print(resultado3)
print('-' * 30)

resultado4 = texto.title() # Convierte la primera letra de cada palabra a mayúscula

print(resultado4)
print('-' * 30)

resultado5 = texto.count('a') # Cuenta cuántas veces aparece la letra 'a'

print(resultado5)
print('-' * 30)

resultado6 = texto.find('Salvador') # Busca la posición de la palabra 'Salvador'

print(resultado6)
print('-' * 30)

resultado7 = texto.replace('Salvador', 'Chava') # Reemplaza la palabra 'Salvador' por 'Chava'

print(resultado7)
print('-' * 30)

resultado8 = texto.split() # Divide el texto en una lista de palabras. Será importante a futuro, ya que nos permitirá separar el texto en partes de manera automática.

print(resultado8)
print('-' * 30)

resultado9 = texto.strip() # Elimina los espacios en blanco al inicio y al final

print(resultado9)
print('-' * 30)

resultado10 = texto.upper().replace('SALVADOR', 'CHAVA') # Combina dos métodos

print(resultado10)
print('-' * 30)

lista_palabras = ["La", "legibilidad", "cuenta"]
resultado11 = " ".join(lista_palabras) # .join() : Método que une una lista de cadenas en una sola, utilizando un separador definido (en este caso, un espacio).

print(resultado11)
print('-' * 30)