"""  
 List (Array)
 son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.

"""
print("\033c")


#Funciones más comunes en las listas
paises=["Mexico", "Canada", "EUA", "Mexico", "Brasil"]
numeros=[23,45,8,24]
varios=[33,3.1416,"hola",True]
vacio=[]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)
print(vacio)


#Recorrer la lista 
#1er forma 
for i in paises:
    print(i)


#2do forma 
for i in range(0,len(paises)):
    print(paises[i])


#ordenar elementos de una lista
print(paises)
paises.sort()
print(paises)

#dar la vuelta a una lista
paises.reverse()
print(paises)


paises=["Mexico", "Canada", "EUA", "Mexico", "Brasil"]
#Agregar, insertar, Añadir un elemento a una lista
#1er forma 
#paises.append("Honduras")
print(paises)

#2da forma
paises.insert(1,"Colombia")
print(paises)
paises.insert(8,"Polonia")
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
paises=["Mexico", "Canada", "EUA", "Mexica", "Brasil"]
print(paises)
#1er forma
paises.pop(3)
print(paises)

#2da forma 
paises.remove("EUA")
print(paises)

#Buscar un elemento dentro de la lista
encontro = "EUA" in paises 
print(encontro)

#Contar el numeros de veces que aparece un elemento dentro de una lista
paises=["Mexico", "Canada", "EUA", "Mexico", "Brasil"]
numeros=[23,45,8,24,23,100,23]

num_veces=numeros.count(23)
print(f"El valor 23 aparece: {num_veces} veces")

num_veces=paises.count("Mexico")
print(f"La palabra Mexico aparece: {num_veces} veces")

#Conocer la posicion o indice en el que se encuentra un elemento de la lista
paises=["Mexico", "Canada", "EUA", "Mexico", "Brasil",]
posicion = paises.index("Mexico")
print(f"Encontré el valor en la posición: {posicion}")


#Unir el contenido de una lista dentro de otra lista
numeros1 = [23,45,8,24,23,100,23]
numeros2 = [100,-100]
print(numeros1), print(numeros2)
numeros1.extend(numeros2)
print(numeros1)

#Crear a partir de las listas de numeros 1 y 2 un resultante y mostar el contenido ordenado descendentemente
numeros1.sort()
numeros1.reverse()
print(numeros1)




