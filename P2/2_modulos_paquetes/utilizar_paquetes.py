from paquete1 import modulos,modulo_paquete

modulos.borrarPantalla()
modulos.funcion1()

nom="Daniel"
ape="Carreon"

name,lastname=modulos.funcion4(nom,ape)
edad=modulo_paquete.solicitarEdad()
print(f"Name: {name} \n Lastname: {lastname}")