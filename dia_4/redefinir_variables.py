# --- LA LÍNEA DE TIEMPO DE UNA VARIABLE ---

# T = 0 (Inicio)
mensaje = "Hola" 
print(f"Línea 4: {mensaje}") 

# T = 1 (Cambio de valor)
# ¡Ojo! No estamos creando una variable nueva.
# Estamos tomando la caja de 'mensaje', tirando lo viejo y poniendo lo nuevo.
mensaje = "Mundo" 
print(f"Línea 9: {mensaje}")

# T = 2 (Uso del valor anterior para crear uno nuevo)
mensaje = mensaje + " Python"
print(f"Línea 13: {mensaje}")

# Pregunta: ¿Cambió esto lo que imprimió la Línea 4?
# Respuesta: NO. Lo hecho, hecho está. La línea 4 ya ocurrió y se imprimió "Hola".
# El programa SIEMPRE avanza hacia abajo 👇. Nunca vuelve atrás.
