# 1er utilizar los modulos 
import modulos

modulos.borrarPantalla()
modulos.funcion1()
                          
nom="Daniel"
ape="Carreon"
edad="18"

name,lastname,edad=modulos.funcion4(nom,ape,edad)
print(f"Nombre: {name}\nApellidos: {lastname}\nEdad: {edad}")  

#2da formar de utilizar modulos
from modulos import borrarPantalla,funcion1,funcion4
#* Sirve para importar todas las funciones que tiene modulos

borrarPantalla()
funcion1()

nom="Daniel"
ape="Carreon"
edad="18"

name,lastname,edad=modulos.funcion4(nom,ape,edad)
print(f"Nombre: {name}\nApellidos: {lastname} \nEdad: {edad}")  

