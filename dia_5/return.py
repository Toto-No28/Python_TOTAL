# OPCIÓN 1: Retorno Directo
# Se usa para operaciones simples y directas. Es preferida en el campo laboral
# por seguir los principios de 'Clean Code' (código limpio y breve).
def multiplicar(num1, num2):
    return num1 * num2

resultado = multiplicar(5, 10)
print(f"Resultado Opción 1: {resultado}")

print('-' * 50)

# OPCIÓN 2: Con Variable Intermedia
# Se prefiere cuando:
# 1. Se necesita depurar (debugging) para ver el valor antes de retornar.
# 2. La lógica es compleja y una variable ayuda a darle nombre al resultado.
# Nota: He renombrado la función para que no haya duplicidad.
def multiplicar_con_total(num1, num2):
    total = num1 * num2
    return total

resultado_v2 = multiplicar_con_total(5, 10)
print(f"Resultado Opción 2 (con variable): {resultado_v2}")

"""
BUENAS PRÁCTICAS PARA FUNCIONES EN PYTHON:

1. Nombramiento: Usar snake_case y nombres descriptivos (ej: calcular_precio).
2. Responsabilidad Única: Una función debe hacer una sola tarea.
3. Docstrings: Usar comillas triples para documentar el propósito de la función.
4. Type Hints: (Avanzado) Indicar tipos esperados -> def suma(a: int) -> int:
5. Retorno vs Print: Una buena función devuelve el valor (return), no solo lo imprime.
"""
