"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
print("\033c")

set1={"Hola", "123", "123", "Paises Bajos","Mexico",123,3.1416}
print(set1)

set1.add("Ganador")
print(set1)

set1.pop()
print(set1)
#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
lista_emails = []

for i in range(5):
    email = input("Ingrese un email: ")
    lista_emails.append(email)

set1 = set(lista_emails)

print("\nEmails sin duplicados (Set 1):")
print(set1)


# Solucion 2
set2 = set()

for i in range(5):
    email = input("Ingrese un email: ")
    set2.add(email)

print("\nEmails sin duplicados (Set 2):")
print(set2)