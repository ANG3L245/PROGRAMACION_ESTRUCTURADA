print("\033c")

#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros = [23,33,45,8,24,0,100]
print(numeros)

lista = ""
for i in numeros:
    lista = lista + str(i) + ", "
    lista += f"{i}, "
print(f"[{lista}]")

lista = ""
for i in range(0,len(numeros)):
    lista += f"{numeros[i]}, "
print(f"[{lista}]")

lista = ""
i = 0
while i < len(numeros):
    lista += f"{numeros[i]}, "
    i += 1
print(f"[{lista}]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#1ER FORMA
palabras = ["UTD","tercer","cuatrimestre","TI"]
palabra = input("Dame la palabra a buscar: ").strip()

if palabra in palabras:
    print(f"Encontré la palabra: {palabra} en la lista")
else:
    print(f"No encontré la palabra: {palabra} en la lista")

#2DA FORMA
palabras = ["UTD","tercer","cuatrimestre","TI"]
palabra = input("Dame la palabra a buscar: ").strip() 

encontro = False
for i in palabras:
    if i == palabra:
        encontro = True
if encontro:
    print(f"Encontré la palabra: {palabra} en la lista")
else:
    print(f"No encontré la palabra: {palabra} en la lista")

#3ER FORMA len
palabras = ["UTD","tercer","cuatrimestre","TI"]
palabra = input("Dame la palabra a buscar: ").strip() 

encontro = False
for i in range(0,len(palabras)):
    if i == palabra:
        encontro = True
if encontro:
    print(f"Encontré la palabra: {palabra} en la lista")
else:
    print(f"No encontré la palabra: {palabra} en la lista")

#4TA FORMA While
palabras = ["UTD","tercer","cuatrimestre","TI"]
palabra = input("Dame la palabra a buscar: ").strip() 

encontro = False
while i<len(palabras):
    if palabras[i] == palabra:
        encontro = True
if encontro:
    print(f"Encontré la palabra: {palabra} en la lista")
else:
    print(f"No encontré la palabra: {palabra} en la lista")

#Ejemplo 3 Añadir elementos a la lista
lista = []

#Opción 1:
true=True
while true:
    valor = input("Dame un valor: ").strip
    lista.append(valor)
    true = input("Ingresa True/False para continuar: ").strip()
    if true == "False":
        true = False

print(lista)

#Opción 2:
continuar = "SI"
while continuar == "SI":
    valor = input("Dame un valor: ").strip
    lista.append(valor)
    continuar = input("Ingresa SI/NO para continuar: ").strip().upper()

print(lista)

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda = [
    ["Carlos","6181234567"],
    ["Adrian","6182332456"],
    ["Luis","6182223444"]
]

print(agenda)

for i in agenda:
    print(i)

lista = ""
for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])

lista = ""
for r in range(0,3):
    for c in range(0,2):
            lista += f"{agenda[r][c]}, "
    lista += "\n"

print(lista)