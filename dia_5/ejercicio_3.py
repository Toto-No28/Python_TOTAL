'''Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False'''

def ceros_consecutivos(*args):
    # Usamos range(len(args) - 1) para detenernos en el penúltimo elemento.
    # En comparaciones siempre se usa N - 1 para evitar un IndexError al intentar acceder a args[i+1] en el último giro.
    for i in range(len(args) - 1):
        
        # Comparamos el número actual (i) con el siguiente (i+1)
        if args[i] == 0 and args[i+1] == 0:
            
            # Si encontramos el par buscado, terminamos la ejecución inmediatamente
            return True
            
    # Si el bucle termina de recorrer todo sin encontrar el par, devolvemos False
    return False

print(ceros_consecutivos(5,6,1,0,0,9,3,5))
print(ceros_consecutivos(6,0,5,1,0,3,0,1))