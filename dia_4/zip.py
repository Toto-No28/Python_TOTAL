nombre = ["Ana", "Luis", "Carlos", "Marta", "Pedro", "Juan", "Maria", "Sofia", "Fernando", "Lucia"]
edad = [22, 34, 29, 42, 25, 31, 28, 33, 26, 30]
ciudades = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Malaga", "Zaragoza", "Palma", "Murcia", "Las Palmas"]


combinados = list(zip(nombre, edad, ciudades))

print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")


espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

# Creamos el zip y lo convertimos en una lista
numeros = list(zip(espaniol, portugues, ingles))

print(numeros)
