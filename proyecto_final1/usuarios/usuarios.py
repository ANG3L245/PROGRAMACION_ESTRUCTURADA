import funciones
from usuarios import crud_usuarios
from usuarios import seguridad
import re 
import getpass

COLOR_BORDE = "\033[1;34m"
COLOR_TITULO = "\033[1;36m"
COLOR_TEXTO = "\033[1;30m"
COLOR_SALIR = "\033[1;31m"
COLOR_ALERTA = "\033[1;33m"
RESET = "\033[0m"

def menuUsuarios(conexionBD, usuario_activo):
    opc = ""
    while opc != "7":
        try:
            funciones.borrarPantalla()
            
            print(f"\n\t{COLOR_BORDE}╔═════════════════════════════════════════╗{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}       {COLOR_TITULO}::::: MENU USUARIOS :::::{RESET}         {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}╠═════════════════════════════════════════╣{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}                                         {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_TEXTO}1.- Registrar usuario{RESET}                  {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_TEXTO}2.- Iniciar sesion{RESET}                     {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_TEXTO}3.- Ver usuarios{RESET}                       {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_TEXTO}4.- Editar usuario{RESET}                     {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_TEXTO}5.- Eliminar usuario{RESET}                   {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_TEXTO}6.- Cambiar contrasena{RESET}                 {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}  {COLOR_SALIR}7.- Volver al menu principal{RESET}           {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}║{RESET}                                         {COLOR_BORDE}║{RESET}")
            print(f"\t{COLOR_BORDE}╚═════════════════════════════════════════╝{RESET}\n")

            opc = input(f"\t{COLOR_TEXTO}Escribe una opcion:{RESET} ").strip()

            match opc:
                case "1":
                    funciones.borrarPantalla()
                    registrarUsuario(conexionBD)
                case "2":
                    funciones.borrarPantalla()
                    resultado = iniciarSesion(conexionBD)
                    if resultado:
                        usuario_activo = resultado
                case "3":
                    funciones.borrarPantalla()
                    verUsuarios(conexionBD)
                case "4":
                    funciones.borrarPantalla()
                    editarUsuario(conexionBD)
                case "5":
                    funciones.borrarPantalla()
                    eliminarUsuario(conexionBD)
                case "6":
                    funciones.borrarPantalla()
                    cambiarContrasena(conexionBD)
                case "7":
                    pass
                case _:
                    funciones.opcionInvalida()
        
        except KeyboardInterrupt:
            print(f"\n\t{COLOR_ALERTA}...Operacion cancelada por el usuario (Ctrl+C)...{RESET}")
            funciones.esperarTecla()
        except Exception as e:
            print(f"\n\t{COLOR_ALERTA}...Ocurrio un error inesperado: {e}...{RESET}")
            funciones.esperarTecla()

    return usuario_activo


def registrarUsuario(conexionBD):
    try:
        titulo = "::::: REGISTRAR USUARIO :::::"
        print(f"\n\t{COLOR_BORDE}╔═══════════════════════════════════════════════════════╗{RESET}")
        print(f"\t{COLOR_BORDE}║{RESET}{COLOR_TITULO}{titulo:^55}{RESET}{COLOR_BORDE}║{RESET}")
        print(f"\t{COLOR_BORDE}╚═══════════════════════════════════════════════════════╝{RESET}\n")
        
        usuario = input(f"{COLOR_TEXTO}Nombre de usuario:{RESET} ").strip()

        existente = crud_usuarios.buscarPorUsuario(usuario, conexionBD)
        if existente:
            print(f"\n\t{COLOR_ALERTA}...Ese nombre de usuario ya esta ocupado, elige otro!...{RESET}")
            funciones.esperarTecla()
            return

        nombre = input(f"{COLOR_TEXTO}Nombre completo:{RESET} ").strip()

        correo = input(f"{COLOR_TEXTO}Correo:{RESET} ").strip()
        while not re.match(r"^[\w.-]+@[\w.-]+\.\w{2,}$", correo):
            print(f"\n\t{COLOR_ALERTA}...Correo invalido, verifique el formato (ejemplo@dominio.com)...{RESET}")
            correo = input(f"{COLOR_TEXTO}Correo:{RESET} ").strip()

        contrasena = getpass.getpass(f"{COLOR_TEXTO}Contrasena:{RESET} ").strip()

        telefono = input(f"{COLOR_TEXTO}Telefono:{RESET} ").strip()
        while not re.match(r"^\d{10}$", telefono):
            print(f"\n\t{COLOR_ALERTA}...Numero invalido, debe contener exactamente 10 digitos numericos...{RESET}")
            telefono = input(f"{COLOR_TEXTO}Telefono:{RESET} ").strip()

        hash_contrasena = seguridad.generarHash(contrasena)

        respuesta = crud_usuarios.insertar(usuario, nombre, correo, hash_contrasena, telefono, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
    
    except Exception as e:
        print(f"\n\t{COLOR_ALERTA}...Error en el registro: {e}...{RESET}")
        funciones.esperarTecla()


def iniciarSesion(conexionBD):
    try:
        titulo = "::::: INICIAR SESION :::::"
        print(f"\n\t{COLOR_BORDE}╔═══════════════════════════════════════════════════════╗{RESET}")
        print(f"\t{COLOR_BORDE}║{RESET}{COLOR_TITULO}{titulo:^55}{RESET}{COLOR_BORDE}║{RESET}")
        print(f"\t{COLOR_BORDE}╚═══════════════════════════════════════════════════════╝{RESET}\n")
        
        usuario = input(f"{COLOR_TEXTO}Nombre de usuario:{RESET} ").strip()
        contrasena = getpass.getpass(f"{COLOR_TEXTO}Contrasena:{RESET} ").strip()

        fila = crud_usuarios.buscarPorUsuario(usuario, conexionBD)

        if fila and seguridad.verificarHash(contrasena, fila[4]):
            print(f"\n\t{COLOR_TITULO}...Bienvenido {fila[2]}...{RESET}")
            funciones.esperarTecla()
            return fila[1]
        else:
            print(f"\n\t{COLOR_ALERTA}...Usuario o contrasena incorrectos...{RESET}")
            funciones.esperarTecla()
            return None
            
    except Exception as e:
        print(f"\n\t{COLOR_ALERTA}...Error al iniciar sesion: {e}...{RESET}")
        funciones.esperarTecla()
        return None


def verUsuarios(conexionBD):
    try:
        lista = crud_usuarios.consultar(conexionBD)

        if len(lista) == 0:
            print(f"\n\t{COLOR_ALERTA}...No hay usuarios registrados, verifique!...{RESET}")
            funciones.esperarTecla()
            return

        titulo = "::::: USUARIOS REGISTRADOS :::::"
        print(f"\n\t{COLOR_BORDE}╔═══════════════════════════════════════════════════════╗{RESET}")
        print(f"\t{COLOR_BORDE}║{RESET}{COLOR_TITULO}{titulo:^55}{RESET}{COLOR_BORDE}║{RESET}")
        print(f"\t{COLOR_BORDE}╚═══════════════════════════════════════════════════════╝{RESET}\n")
        
        print(f"\t{COLOR_TITULO}{'Usuario':<15}\t{'Nombre':<55}\t{'Correo':<35}\t{'Telefono':<12}{RESET}\n")
        for u in lista:
            print(f"\t{COLOR_TEXTO}{u[1]:<15}\t{u[2]:<55}\t{u[3]:<35}\t{u[5]:<12}{RESET}")
        print(f"\t{COLOR_BORDE}" + "-" * 115 + f"{RESET}")
        funciones.esperarTecla()
        
    except Exception as e:
        print(f"\n\t{COLOR_ALERTA}...Error al consultar usuarios: {e}...{RESET}")
        funciones.esperarTecla()


def editarUsuario(conexionBD):
    try:
        titulo = "::::: EDITAR USUARIO :::::"
        print(f"\n\t{COLOR_BORDE}╔═══════════════════════════════════════════════════════╗{RESET}")
        print(f"\t{COLOR_BORDE}║{RESET}{COLOR_TITULO}{titulo:^55}{RESET}{COLOR_BORDE}║{RESET}")
        print(f"\t{COLOR_BORDE}╚═══════════════════════════════════════════════════════╝{RESET}\n")
        
        usuario_sel = input(f"{COLOR_TEXTO}Escribe el nombre de usuario a editar:{RESET} ").strip()
        
        fila = crud_usuarios.buscarPorUsuario(usuario_sel, conexionBD)
        if not fila:
            print(f"\n\t{COLOR_ALERTA}...Ese usuario no existe!...{RESET}")
            funciones.esperarTecla()
            return

        contrasena = getpass.getpass(f"{COLOR_TEXTO}Ingresa la contrasena del usuario para autorizar la edicion:{RESET} ").strip()
        if not seguridad.verificarHash(contrasena, fila[4]):
            print(f"\n\t{COLOR_ALERTA}...Contrasena incorrecta. Autorizacion denegada!...{RESET}")
            funciones.esperarTecla()
            return

        nombre = input(f"{COLOR_TEXTO}Nuevo nombre completo:{RESET} ").strip()
        
        correo = input(f"{COLOR_TEXTO}Nuevo correo:{RESET} ").strip()
        while not re.match(r"^[\w.-]+@[\w.-]+\.\w{2,}$", correo):
            print(f"\n\t{COLOR_ALERTA}...Correo invalido, verifique el formato (ejemplo@dominio.com)...{RESET}")
            correo = input(f"{COLOR_TEXTO}Nuevo correo:{RESET} ").strip()

        telefono = input(f"{COLOR_TEXTO}Nuevo telefono:{RESET} ").strip()
        while not re.match(r"^\d{10}$", telefono):
            print(f"\n\t{COLOR_ALERTA}...Numero invalido, debe contener exactamente 10 digitos numericos...{RESET}")
            telefono = input(f"{COLOR_TEXTO}Nuevo telefono:{RESET} ").strip()

        respuesta = crud_usuarios.actualizar(usuario_sel, nombre, correo, telefono, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
            
    except Exception as e:
        print(f"\n\t{COLOR_ALERTA}...Error al editar usuario: {e}...{RESET}")
        funciones.esperarTecla()


def eliminarUsuario(conexionBD):
    try:
        titulo = "::::: ELIMINAR USUARIO :::::"
        print(f"\n\t{COLOR_BORDE}╔═══════════════════════════════════════════════════════╗{RESET}")
        print(f"\t{COLOR_BORDE}║{RESET}{COLOR_TITULO}{titulo:^55}{RESET}{COLOR_BORDE}║{RESET}")
        print(f"\t{COLOR_BORDE}╚═══════════════════════════════════════════════════════╝{RESET}\n")
        
        usuario_sel = input(f"{COLOR_TEXTO}Escribe el nombre de usuario a eliminar:{RESET} ").strip()
        
        fila = crud_usuarios.buscarPorUsuario(usuario_sel, conexionBD)
        if not fila:
            print(f"\n\t{COLOR_ALERTA}...Ese usuario no existe!...{RESET}")
            funciones.esperarTecla()
            return

        contrasena = getpass.getpass(f"{COLOR_TEXTO}Ingresa la contrasena del usuario para autorizar la eliminacion:{RESET} ").strip()
        if not seguridad.verificarHash(contrasena, fila[4]):
            print(f"\n\t{COLOR_ALERTA}...Contrasena incorrecta. Autorizacion denegada!...{RESET}")
            funciones.esperarTecla()
            return

        opc = input(f"\n{COLOR_TEXTO}¿Seguro que deseas eliminar al usuario {usuario_sel}? (si/no):{RESET} ").lower().strip()

        if opc == "si":
            respuesta = crud_usuarios.eliminar(usuario_sel, conexionBD)
            if respuesta:
                funciones.accionExitosa()
            else:
                funciones.accionNoExitosa()
        else:
            print(f"\n\t{COLOR_ALERTA}...Operacion cancelada...{RESET}")
            funciones.esperarTecla()
            
    except Exception as e:
        print(f"\n\t{COLOR_ALERTA}...Error al eliminar usuario: {e}...{RESET}")
        funciones.esperarTecla()


def cambiarContrasena(conexionBD):
    try:
        titulo = "::::: CAMBIAR CONTRASENA :::::"
        print(f"\n\t{COLOR_BORDE}╔═══════════════════════════════════════════════════════╗{RESET}")
        print(f"\t{COLOR_BORDE}║{RESET}{COLOR_TITULO}{titulo:^55}{RESET}{COLOR_BORDE}║{RESET}")
        print(f"\t{COLOR_BORDE}╚═══════════════════════════════════════════════════════╝{RESET}\n")
        
        usuario_sel = input(f"{COLOR_TEXTO}Escribe tu nombre de usuario:{RESET} ").strip()
        
        fila = crud_usuarios.buscarPorUsuario(usuario_sel, conexionBD)
        if not fila:
            print(f"\n\t{COLOR_ALERTA}...Ese usuario no existe!...{RESET}")
            funciones.esperarTecla()
            return

        sabe_contrasena = input(f"{COLOR_TEXTO}¿Conoces tu contrasena actual? (si/no):{RESET} ").lower().strip()

        if sabe_contrasena == "si":
            contrasena_actual = getpass.getpass(f"{COLOR_TEXTO}Ingresa tu contrasena actual:{RESET} ").strip()
            if not seguridad.verificarHash(contrasena_actual, fila[4]):
                print(f"\n\t{COLOR_ALERTA}...Contrasena incorrecta!...{RESET}")
                funciones.esperarTecla()
                return
        else:
            correo_actual = input(f"{COLOR_TEXTO}Ingresa tu correo electronico registrado:{RESET} ").strip()
            if correo_actual != fila[3]: 
                print(f"\n\t{COLOR_ALERTA}...El correo no coincide con el registrado en el sistema!...{RESET}")
                funciones.esperarTecla()
                return

        nueva_contrasena = getpass.getpass(f"{COLOR_TEXTO}Ingresa tu nueva contrasena:{RESET} ").strip()
        hash_nuevo = seguridad.generarHash(nueva_contrasena)

        respuesta = crud_usuarios.actualizarContrasena(usuario_sel, hash_nuevo, conexionBD)
        if respuesta:
            funciones.accionExitosa()
        else:
            funciones.accionNoExitosa()
            
    except Exception as e:
        print(f"\n\t{COLOR_ALERTA}...Error al cambiar contrasena: {e}...{RESET}")
        funciones.esperarTecla()