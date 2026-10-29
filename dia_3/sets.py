# Sets (Conjuntos)
# Los sets son colecciones desordenadas de elementos únicos.
# Internamente usan una TABLA HASH.
# El orden depende del "hash" (un número único generado para cada elemento).

mi_set = {"Manzana", "Banana", "Cereza"}
print("Set original:", mi_set)

# ¿Por qué ese orden? Veamos los HASHES:
print("\n--- HASHES ---")
print(f"Hash de 'Manzana': {hash('Manzana')}")
print(f"Hash de 'Banana':  {hash('Banana')}")
print(f"Hash de 'Cereza':  {hash('Cereza')}")
# Python coloca los elementos en espacios de memoria basándose en estos números.
# Como los hashes de strings cambian en cada ejecución (por seguridad),
# el orden PUEDE CAMBIAR si reinicias el programa.

print("\n--- Números ---")
# Con números pequeños, el hash suele ser el mismo número, por eso a veces parecen ordenados.
nums = {1, 5, 2, 4, 3}
print(f"Set de números: {nums}")
for n in nums:
    print(f"Hash de {n}: {hash(n)}")

mi_set.add("Naranja")
print("\nDespues de agregar 'Naranja':", mi_set)

print('-' * 30)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set.union(set1, set2)
print(set3) 