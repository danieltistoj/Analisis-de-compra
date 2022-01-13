import pandas as pd
from datetime import datetime


df = pd.read_csv("csv/compras2.csv")
#muestra los primeras cinco filas

#df.head()
#mustra los ultimos cinco filas
#df.tail()
#ponemos decubrir los datos, calculando estadisticos descriptivos
#mean = media
#min = minimo
#std = desviacion estandar
#df.describe()

#Limpieza de datos
#con fillna decimos que valor queremos que tengan aquellos espacios vacios o NA
df_filtrado = df.fillna({"Descripcion":"","Cantidad":0})
#Eliminamos el signo de quetzales del sub total
df_filtrado["Sub TOTAL"] = df_filtrado["Sub TOTAL"].str.replace('Q','')
#Convertimos el string en flotante
df_filtrado["Sub TOTAL"] = df_filtrado["Sub TOTAL"].astype(float)
#df_filtrado['Fecha'] = pd.date_range(df_filtrado['Fecha'],format="%dd/%mm/%Y")
#print(df_filtrado['Fecha'])
#print(df_filtrado["Sub TOTAL"])

df_filtrado = df_filtrado.groupby("Fecha").agg({
    "Sub TOTAL":'sum',
    "Cantidad":'sum'
})


print(df_filtrado)
