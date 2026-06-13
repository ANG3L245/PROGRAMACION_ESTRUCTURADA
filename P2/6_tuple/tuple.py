"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")

paises1 = ("México", "Canadá", "EUA")
paises3= ["México", "Canadá", "EUA"]
varios= ("Hola", True,33,3.1416)

print(paises1)
print(varios)

for i in paises1:
  print(i)
  
for i in range(1, len(paises1)):
  print(paises1[i])  
  
i=1
while i <= len(paises1):
      print(paises1)
      i += 1
      
print(f"El país que inagurua la World Cup 2026 es: {paises1[0]}")

edades = (23,24,18,20,20,23,24,19,24)
contar = edades.count(24)
print(contar)

#programa
numero = int((input("Dame el número a buscar: ")).strip())
posiciones=[]
for i in range(0,len(edades)):
  if edades[i] == numero:
        posiciones.append(i)

if posiciones:
      print(f"El numero {numero} se encuentra en las posiciones: {posiciones}")
else:
      print(f"El número no se encuentra en la lista")