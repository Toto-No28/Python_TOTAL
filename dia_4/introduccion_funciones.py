# -------------------------------------------------------------------------
# --- INTRODUCCIÓN A LAS FUNCIONES (def) ---
# -------------------------------------------------------------------------
# 'def' es la palabra clave en Python para DEFINIR una FUNCIÓN.
#
# ¿Qué es una función?
# Imagina que es como una "receta" o una "miniatura de programa" que guardas
# para usar después. En lugar de escribir el mismo código una y otra vez,
# le pones un nombre y lo "llamas" cuando lo necesites.

# 1. EJEMPLO BÁSICO: Una función simple que solo imprime algo
# ---------------------------------------------------------
def saludar():
    # Todo lo que esté identado (con sangría) pertenece a la función
    print("¡Hola! Bienvenido al mundo de las funciones.")
    print("Esta es una función sin parámetros se ejecuta solo cuando la llamas.")


print("--- 1. Llamando a la función saludar() ---")
# Aquí "llamamos" o "invocamos" a la función para que se ejecute
saludar()


# 2. PARÁMETROS: Pasándole información a la función
# ---------------------------------------------------------
# A veces la receta necesita ingredientes. Esos son los "parámetros".
# Aquí 'nombre' es una variable que solo existe dentro de esta función.
def saludar_personalizado(nombre):
    print(f"Hola, {nombre}. ¡Qué gusto verte!")


print("\n--- 2. Llamando a saludar_personalizado() ---")
saludar_personalizado("Chava")
saludar_personalizado("Maria")


# 3. RETURN: Devolviendo un resultado
# ---------------------------------------------------------
# A veces no quieres que la función solo imprima, sino que CALCULE algo
# y te devuelva el resultado para usarlo después.
def sumar(a, b):
    resultado = a + b
    return resultado  # 'return' entrega el valor final hacia fuera


print("\n--- 3. Usando return ---")
mi_suma = sumar(10, 5)  # Guardamos el resultado de la función en una variable
print(f"El resultado de la suma es: {mi_suma}")

# Podemos usar el resultado directamente en una operación
total = sumar(50, 50) + 20
print(f"Suma de (50 + 50) + 20 = {total}")
