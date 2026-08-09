import mysql.connector


def borrarPantalla():
    print("\033c")


COLOR_BORDE = "\033[1;34m"
COLOR_TITULO = "\033[1;36m"
COLOR_TEXTO = "\033[1;30m"
COLOR_SALIR = "\033[1;31m"
COLOR_ALERTA = "\033[1;33m"
RESET = "\033[0m"

def esperarTecla():
    print(f"\n\t{COLOR_BORDE}────────────────────────────────────────────────────────{RESET}")
    input(f"\t{COLOR_TEXTO}Presiona Enter para continuar...{RESET}")

def opcionInvalida():
    print(f"\n\t{COLOR_ALERTA}⚠ Opcion invalida, por favor verifique e intente de nuevo.{RESET}")
    input(f"\t{COLOR_TEXTO}(Presiona Enter para continuar){RESET}")

def accionExitosa():
    print(f"\n\t{COLOR_TITULO}✔ ¡Accion realizada con exito!{RESET}")
    input(f"\t{COLOR_TEXTO}(Presiona Enter para continuar){RESET}")

def accionNoExitosa():
    print(f"\n\t{COLOR_ALERTA}✘ No fue posible realizar esta accion, intentalo mas tarde.{RESET}")
    input(f"\t{COLOR_TEXTO}(Presiona Enter para continuar){RESET}")

def terminarSistema():
    print(f"\n\n\t{COLOR_BORDE}╔═══════════════════════════════════════════════════════╗{RESET}")
    print(f"\t{COLOR_BORDE}║{RESET}{COLOR_TITULO}     GRACIAS POR UTILIZAR NUESTRO SISTEMA      {RESET}{COLOR_BORDE}║{RESET}")
    print(f"\t{COLOR_BORDE}╚═══════════════════════════════════════════════════════╝{RESET}\n")


def conectar():
    try:
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_finanzas"
        )
        return conexion
    except Exception as e:
        print(f"...Por el momento no es posible conectar con la Base de Datos: {e}...")
        return None