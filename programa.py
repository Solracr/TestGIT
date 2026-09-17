import pandas as pd 

datos = {
    "Clientes": ["C-129","C-3883","C-098"],
    "Transacciones": [22345.49,159.80,39.3]
}

df = pd.DataFrame(datos)

print(df)

promedio = df["Transacciones"].mean()
print("El promedio de la variable Transacciones es:")

print(promedio)