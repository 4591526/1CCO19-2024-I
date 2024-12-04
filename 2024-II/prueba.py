# Mi primer programa en Python en Visual Studio Code

# A diferencia de Google Colab, en Visual Studio Code no se puede ejecutar una celda de código
# por lo que se debe ejecutar todo el script a la vez 

# El output de la ejecución aparecerá en la terminal 

# Imprimir un mensaje
# print("Hola Mundo")

# Variables
x = 5
y = 10.5
z = "Luisa"
q = True

# Imprimir variables
#print(x)
#print(y)
#print(z)

# Operamos con los valores de las variables
#print("El valor de x es: ", x)
#print("El valor de y es: ", y)
#print("El valor de z es: ", z)
#print("El valor de q es: ", q)

print(x + y)
print(z * x)
print((x == y) != q)

# type(): nos dice el tipo de dato de una variable
print(type(x))
# help(): te ofrece información sobre un objeto
#help("int")

# Listas
lista = [1, 2, 3, 4, 5]
print(lista)

print(lista[0])
print(lista[1])

print(lista[-1])

print(lista[1:3])

lista.append(6)
print(lista)



# Diccionarios
diccionario = {'nombre': 'Cristina', 'edad': 25, 'ciudad': 'Santiago'}
print(diccionario)

print(diccionario['nombre'])
print(diccionario['edad'])

diccionario['edad'] = 26
print(diccionario)

# Convertir nuestro diccionario en un DataFrame
import pandas as pd
df_1 = pd.DataFrame(diccionario, index=[0])
#print(df_1)

# agregar una nueva fila
diccionario2 = {'nombre': 'Luisa', 'edad': 27, 'ciudad': 'Valparaíso'}
df_2 = df_1.append(diccionario2, ignore_index=True)
print(df_2)

# agregar latitud y longitud
df_2['latitud'] = [-33.45, -33.05]
df_2['longitud'] = [-70.65, -71.62]
print(df_2)

# pip install folium
# importamos la libreria folium
import folium

# Creamos un mapa centrado en Santiago
m = folium.Map(location=[-33.45, -70.65], zoom_start=10, tiles="OpenStreetMap")

# Agregamos un marcador
for _, row in df_2.iterrows():
    folium.Marker(
        location=[row["latitud"], row["longitud"]],
        popup=row["nombre"],
        tooltip=row["ciudad"]
    ).add_to(m)

# Procedemos a guardar y mostrar el mapa
m.save("mapa.html")
m

import pandas as pd
# abrir un archivo excel con pandas
juego = pd.read_excel('datos_juego.xlsx')
print(juego.head())

# eliminar columnas
juego = juego.drop(columns=['+', '+.1'])
print(juego.head())

# contar los valores de una columna
tipo_locacion = juego['Locación'].value_counts()
print(tipo_locacion)

# graficar un pie chart
# pip install matplotlib
import matplotlib.pyplot as plt

# help(plt.pie)

# tamaño de la figura
plt.figure(figsize=(10, 5))

# colores
colors = ['pink', 'skyblue', 'yellow']

plt.pie(tipo_locacion, labels=tipo_locacion.index, autopct='%1.1f%%', colors=colors)
plt.title('Locación de los juegos')

# guardar la imagen
#plt.savefig('pie_chart.png')

# plt.show()

# hacer un buscador con los datos
# deseo que el usuario el tamaño del negocio ("2x2" o "3x3") y la locación ("Hierba" o "Playa" o " Agua")
# y que el programa le entregue el nombre del negocio ("Comercio") y el precio ("Precio")

# input() nos permite ingresar datos por teclado
dimension = input("Ingrese el tamaño del negocio (2x2 o 3x3): ")
locacion = input("Ingrese la locación del negocio (Hierba, Playa o Agua): ")

# buscamos el negocio
for i, row in juego.iterrows():
    if row['T'] == dimension and row['Locación'] == locacion:
        print("El negocio es: ", row['Comercio'])
        print("El precio es: ", row['Precio'])
        break
    

    


