dic = {
    'clave1': 'valor1',
    'clave2': 'valor2',
    'clave3': 'valor3',
}

item = dic.popitem()
print(item)
print(dic)


limpia = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

limpia =limpia.lstrip(',:_#%')
print(limpia)


frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

frutas.insert(3, "naranja")
print(frutas)


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

