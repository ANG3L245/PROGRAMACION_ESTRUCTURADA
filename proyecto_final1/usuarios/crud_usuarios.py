def insertar(usuario, nombre, correo, contrasena, telefono, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "insert into usuarios (usuario, nombre, correo, contrasena, telefono) values (%s,%s,%s,%s,%s)",
                (usuario, nombre, correo, contrasena, telefono)
            )
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def buscarPorUsuario(usuario, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select * from usuarios where usuario=%s", (usuario,))
            return cursor.fetchone()
        else:
            return None
    except Exception as e:
        print(e)
        return None


def consultar(conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select * from usuarios")
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print(e)
        return []


def actualizar(usuario, nombre, correo, telefono, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "update usuarios set nombre=%s, correo=%s, telefono=%s where usuario=%s",
                (nombre, correo, telefono, usuario)
            )
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def eliminar(usuario, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from usuarios where usuario=%s", (usuario,))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def actualizarContrasena(usuario, hash_nuevo, conexionBD):
    try:
        cursor = conexionBD.cursor()
        # Asegúrate de que "contrasena" sea el nombre exacto de la columna en tu tabla de MySQL
        sql = "UPDATE usuarios SET contrasena = %s WHERE usuario = %s"
        valores = (hash_nuevo, usuario)
        
        cursor.execute(sql, valores)
        conexionBD.commit()
        
        return cursor.rowcount > 0
    except Exception as e:
        print(f"\n\t...Error al actualizar en BD: {e}...")
        return False
    finally:
        if cursor:
            cursor.close()