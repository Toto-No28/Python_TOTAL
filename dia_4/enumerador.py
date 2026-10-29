abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for indice, letra in enumerate(abecedario):
    print(indice, letra)


print('-' * 50)

lista_tuples = list(enumerate(abecedario))

print(lista_tuples)

print('-' * 50)

# Ejemplo de vida real
correos = [
    "carlos@gmail.com", 
    "ana@hotmail.com", 
    "pedro_sin_arroba.com", # <- Aquí hay un error
    "maria@yahoo.com"
]

# Usamos start=1 para que nuestras líneas empiecen a contar desde 1, como en un archivo real
for numero_linea, correo in enumerate(correos, start=1):
    if "@" not in correo:
        print(f"¡Alerta! Correo inválido encontrado en la línea {numero_linea}: {correo}")

print('-' * 50)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)
