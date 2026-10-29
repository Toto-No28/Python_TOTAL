serie = "N-02-2026"

# Modo sin match

if serie == "N-01-2026":
    print("Serie 1")
elif serie == "N-02-2026":
    print("Serie 2")
elif serie == "N-03-2026":
    print("Serie 3")
else:
    print("Serie no encontrada")

# Modo con match

match serie:
    case "N-01-2026":
        print("Serie 1")
    case "N-02-2026":
        print("Serie 2")
    case "N-03-2026":
        print("Serie 3")
    case _:
        print("Serie no encontrada")

# --- PATTERN MATCHING AVANZADO (Destructuring) ---

# Imagina que recibimos datos de un cliente con diferentes formatos
# elemento = ["Nombre", Edad, "Puesto"]
elemento = ["Carlos", 28, "Programador"]

match elemento:
    case [nombre, edad, "Programador"]:
        # Aquí 'nombre' y 'edad' se crean automáticamente
        # extrayendo los valores de la lista
        print(f"Hola {nombre}, tienes {edad} años y eres colega.")

    case [nombre, edad, puesto]:
        # Aquí extrae los 3 valores independientemente de lo que diga 'puesto'
        print(f"Cliente: {nombre}, Puesto: {puesto}")

    case _:
        print("Estructura de datos no reconocida")

print("-" * 50)

protagonista = {"nombre": "Salvador", "edad": 30, "puesto": "Programador"}

pelicula = {
    "titulo": "The Matrix",
    "ficha_tecnica": {
        "protagonista": "Keanu Reeves",
        "director": "Lana y Lilly Wachowski",
    },
}
