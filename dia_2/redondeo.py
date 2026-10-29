# tenemos la oportunidad de poder redondear numeros con la funcion round()
numero = 10.6
print(round(numero)) # Redondea al numero entero mas cercano. En el caso de .5 redondea al numero par mas cercano
numero = 10.4
print(round(numero)) # Redondea al numero entero mas cercano

valor = 45689.456541321657896846513218432132189651
print(round(valor, 2)) # Redondea al numero con decimales especificados. La buena prráctica es usar un espacio después de la coma.

print(round(valor))
print(type(round(valor))) # Nos muestra el tipo de dato que es el resultado de la operacion. En este caso es un entero.

