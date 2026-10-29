
# -------------------------------------------------------------------------
# --- FUNCIONES + INPUTS: EL DÚO DINÁMICO ---
# -------------------------------------------------------------------------
# Tienes toda la razón. Las funciones brillan cuando procesan datos QUE NO CONOCES
# de antemano (como lo que escribe un usuario).

def verificar_entrada_antro(nombre, edad):
    # Esta lógica se define UNA sola vez.
    # No importa si entra 1 persona o 1000, la regla es la misma.
    print(f"\nVerificando a {nombre}...")
    
    if edad >= 18:
        print(f"✅ ¡Adelante {nombre}! Bienvenido a la fiesta de Python.")
    else:
        anios_faltantes = 18 - edad
        print(f"⛔ Lo siento {nombre}, eres menor de edad.")
        print(f"   Vuelve en {anios_faltantes} años.")

# -------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------------------------------------------------

print("--- SISTEMA DE SEGURIDAD DEL CLUB PYTHON ---")

# 1. Pedimos datos al usuario (INPUT REAL)
nombre_usuario = input("Filtro de seguridad. ¿Cuál es tu nombre? ")
edad_texto = input("¿Qué edad tienes? ")

# 2. Convertimos el texto a número (porque input siempre devuelve texto)
edad_numero = int(edad_texto)

# 3. ¡La función hace la magia con los datos frescos!
verificar_entrada_antro(nombre_usuario, edad_numero)


# --- ¿POR QUÉ ES POTENTE ESTO? ---
# Imagina que tienes que verificar a 50 personas en una fila.
# En lugar de copiar y pegar el 'if/else' 50 veces, podrías hacer esto:
#
# while True:
#     nombre = input("Siguiente: ")
#     if nombre == "salir": break
#     edad = int(input("Edad: "))
#     verificar_entrada_antro(nombre, edad) <--- Reusas la misma lógica infinitamente
