import pandas as pd 

datos = {
    "Cod": ["C-129","C-3883","C-098"],
    "Value": [22345.49,159.80,39.3]
}

df = pd.DataFrame(datos)

print(df)

mediana = df["Value"].median()
print("La mediana es:")

print(mediana)