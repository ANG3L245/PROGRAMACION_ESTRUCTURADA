
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funcion que no recibe parametros y no regresa valor
def funcion1():
      nombre=input("Nombre: ").upper().strip()
      apellidos=input("Apellidos: ").upper().strip()
      print(f"EL nombre del alumno es: {nombre} {apellidos}")
      

 #3.- Funcion que recibe parametros y no regresa valor 
def funcion3(nom,ape):
      nombre=nom
      apellidos=ape
      print(f"EL nombre del alumno es: {nombre} {apellidos}")

 #2.- Funcion que no recibe parametros y regresa valor
def funcion2():
      nombre=input("Nombre: ").upper().strip()
      apellidos=input("Apellidos: ").upper().strip()
      return nombre,apellidos
   
 #4.- Funcion que recibe parametros y regresa valor
def funcion4(nom,ape):
      nombre=nom
      apellidos=ape
      return nombre,apellidos

#Invocar las funciones
funcion1()

nombre=input("Nombre: ").upper().strip()
apellidos=input("Apellidos: ").upper().strip()
funcion3(nombre,apellidos)

nombre,apellidos=funcion2()
print(f"EL nombre del alumno es: {nombre} {apellidos}")

nom=input("Nombre: ").upper().strip()
ape=input("Apellidos: ").upper().strip()
nombre,apellidos=funcion4(nom,ape)
print(f"El nombre del alumno es: {nombre} {apellidos}")
