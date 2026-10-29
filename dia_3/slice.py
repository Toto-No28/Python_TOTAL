# Como siempre extraemos los elementos de las listas sin problemas.

texto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
fragmento = texto[2]
print(fragmento) # resultado: C

# Pero si queremos extraer un fragmento de texto, necesitamos usar slicing.
fragmento = texto[2:5] # Empieza en el índice 2 y termina en el índice 5 (sin incluirlo)
print(fragmento) # resultado: CDE

# Si dejamos el segundo parámetro en blanco, extraerá hasta el final.
fragmento = texto[2:] # Empieza en el índice 2 y termina en el final
print(fragmento) # resultado: CDEFGHIJKLMNOPQRSTUVWXYZ

# Si dejamos el primer parámetro en blanco, extraerá desde el principio.
fragmento = texto[:5] # Empieza en el principio y termina en el índice 5 (sin incluirlo)
print(fragmento) # resultado: ABCDE

fragmento = texto[2:10:2] # Empieza en el índice 2, termina en el índice 10 (sin incluirlo) y avanza de 2 en 2
print(fragmento) # resultado: CEGI

fragmento = texto[::3] # Nos da todo el texto pero de 3 en 3
print(fragmento) # resultado: ADGJMORUX

fragmento = texto[::-1] # Nos da todo el texto pero al revés.
print(fragmento) # resultado: ZYXWVUTSRQPOÑNMLKJIHGFEDCBA

fragmento = texto[::-2] # Nos da todo el texto pero al revés y de 2 en 2
print(fragmento) # resultado: ZXVTRPÑMKIGECA