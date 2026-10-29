#Crea una función llamada devolver_distintos() que reciba 3
#integers como parámetros.

def devolver_distintos(a, b, c):
    suma = a + b + c
    
    #Si la suma de los 3 numeros es mayor a 15, va a devolver el
    #número mayor.
    if suma > 15:
        return max(a, b, c)
    
    #Si la suma de los 3 numeros es menor a 10, va a devolver el
    #número menor.
    elif suma < 10:
        return min(a, b, c)
    
    #Si la suma de los 3 números es un valor entre 10 y 15
    #(incluidos) va a devolver el número de valor intermedio.
    else:
        return sorted([a, b, c])[1]


