# Booleanos
# Los booleanos son tipos de datos que representan uno de dos valores: True o False.
# Se utilizan en operaciones lógicas y para tomar decisiones en el código.
# También es importante notar que se escriben con la primera letra en mayúscula.

var1 = True
var2 = False

print(type(var1))
print(var1)


print('-' * 30)

# Buenas prácticas: Estilo (PEP 8) y Legibilidad
# 1. Espaciado alrededor de operadores ( / , * , > )
# 2. Uso de paréntesis para agrupar operaciones y mejorar la lectura visual
# Original: resultado = 17834/34 > 87*56
resultado = (17834 / 34) > (87 * 56)
print(resultado)

print('-' * 30)

# Análisis de paréntesis: Necesidad vs Estilo vs Ruido
# 1. (1/2) -> NECESARIO: Sin ellos, la precedencia haría (25**1) / 2 = 12.5
# 2. (25 ** ...) -> ESTILO: Ayuda visualmente a separar la operación matemática de la comparación
# 3. (5) -> RUIDO: Innecesario para un valor literal simple
# Original: comparacion = (25 ** (1/2)) == (5)
comparacion = (25 ** (1/2)) == 5
print(comparacion)
