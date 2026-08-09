import funciones
from usuarios import usuarios
from finanzas import finanzas

COLOR_BORDE = "\033[1;34m"
COLOR_TITULO = "\033[1;36m"
COLOR_TEXTO = "\033[1;30m"
COLOR_SALIR = "\033[1;31m"
COLOR_ALERTA = "\033[1;33m"
RESET = "\033[0m"

conexionBD = funciones.conectar()
usuario_activo = None

funciones.borrarPantalla()
print(f"\n\t{COLOR_TITULO}======================================================================={RESET}")
print(f"\t{COLOR_TITULO}Sistema de escritorio en consola para la gestion de finanzas personales{RESET}")
print(f"\t{COLOR_TITULO}======================================================================={RESET}")
print(f"\n\t{COLOR_TEXTO}Creado por:{RESET}")
print(f"\t{COLOR_TEXTO}  - Leonel Ivan Sifuentes Zaragoza{RESET}")
print(f"\t{COLOR_TEXTO}  - Angel Zavala Flores{RESET}\n")

input(f"\n\t{COLOR_ALERTA}Presiona ENTER para iniciar el programa...{RESET}")

opc = ""

while opc != "3":
    funciones.borrarPantalla()
    
    print(f"\n\t{COLOR_BORDE}╔═════════════════════════════════════════╗{RESET}")
    print(f"\t{COLOR_BORDE}║{RESET}       {COLOR_TITULO}::::: MENU PRINCIPAL :::::{RESET}        {COLOR_BORDE}║{RESET}")
    print(f"\t{COLOR_BORDE}╠═════════════════════════════════════════╣{RESET}")
    print(f"\t{COLOR_BORDE}║{RESET}                                         {COLOR_BORDE}║{RESET}")
    print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_TEXTO}1.- Trabajar con tabla Usuarios{RESET}        {COLOR_BORDE}║{RESET}")
    print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_TEXTO}2.- Trabajar con tabla Finanzas{RESET}        {COLOR_BORDE}║{RESET}")
    print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_SALIR}3.- Salir{RESET}                              {COLOR_BORDE}║{RESET}")
    print(f"\t{COLOR_BORDE}║{RESET}                                         {COLOR_BORDE}║{RESET}")
    print(f"\t{COLOR_BORDE}╚═════════════════════════════════════════╝{RESET}\n")
    
    opc = input(f"\t{COLOR_TEXTO}Escribe una opcion:{RESET} ").strip()

    match opc:
        case "1":
            funciones.borrarPantalla()
            usuario_activo = usuarios.menuUsuarios(conexionBD, usuario_activo)

        case "2":
            funciones.borrarPantalla()
            if usuario_activo is not None:
                finanzas.menuFinanzas(conexionBD, usuario_activo)
            else:
                input(f"\n\t{COLOR_ALERTA}...Primero debes iniciar sesion en la tabla Usuarios!...{RESET}")

        case "3":
            funciones.borrarPantalla()
            funciones.terminarSistema()

        case _:
            funciones.opcionInvalida()