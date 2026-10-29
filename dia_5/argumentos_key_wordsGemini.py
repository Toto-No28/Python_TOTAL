"""
PRÁCTICA DE KEY WORD ARGUMENTS (**kwargs)
Conceptos aprendidos hoy: Empaquetado, Contenedores y Estructuras Complejas.
"""

# 1. Función básica para entender el empaquetado
def ejemplo_basico(**kwargs):
    # Python toma los argumentos nombre="valor" y los mete en un diccionario automáticamente.
    print("\n--- 1. EMPAQUETADO BÁSICO ---")
    print(f"Tipo de dato: {type(kwargs)}")
    print(f"Contenido: {kwargs}")

ejemplo_basico(nombre="Salvador", edad=30, genero="Masculino")


# 2. Una palabra clave con múltiples valores (La técnica de la "Bolsa")
# Recuerda: Una variable = Un objeto. Para pasar muchos valores, usamos una lista.
def ejemplo_lista(**kwargs):
    print("\n--- 2. UNA LLAVE CON MUCHOS VALORES (LISTA) ---")
    for clave, valor in kwargs.items():
        print(f"La clave '{clave}' contiene: {valor}")

ejemplo_lista(estudiante="Salvador", notas=[10, 9, 8, 10])


# 3. Estructuras Complejas: Lista de Diccionarios
# Las palabras clave (keys) se pueden repetir SIEMPRE que estén en diccionarios diferentes.
def ejemplo_complejo(**kwargs):
    print("\n--- 3. LISTA DE DICCIONARIOS ---")
    alumnos = kwargs["lista_alumnos"] # Extraemos la lista
    
    for registro in alumnos:
        # Aquí 'nombre' se repite en cada diccionario, pero son independientes.
        print(f"Registro encontrado -> Nombre: {registro['nombre']}, ID: {registro['id']}")

datos_alumnos = [
    {"nombre": "Salvador", "id": 1},
    {"nombre": "Ana", "id": 2},
    {"nombre": "Luis", "id": 3}
]

ejemplo_complejo(lista_alumnos=datos_alumnos)


"""
NOTAS DE BUENAS PRÁCTICAS:
--------------------------
1. Nombre por Convención: Usa siempre '**kwargs' a menos que tengas una razón muy 
   específica para cambiarlo. Ayuda a que otros programadores entiendan tu código rápido.

2. Unicidad de Llaves: En la llamada a la función, no puedes repetir la misma llave.
   MAL: funcion(puntos=10, puntos=20) -> Error.
   BIEN: funcion(puntos=[10, 20]) -> Correcto.

3. Orden de Argumentos: Si combinas tipos de argumentos, el orden debe ser:
   1. Argumentos normales (posicionales)
   2. *args
   3. **kwargs (Siempre al final)

4. Verificación: Siempre es bueno verificar si una llave existe antes de usarla para evitar errores:
   if 'nombre' in kwargs: 
       print(kwargs['nombre'])
"""
