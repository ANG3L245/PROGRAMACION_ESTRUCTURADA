def insertar(usuario, tipo, categoria, monto, descripcion, fecha, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "insert into finanzas (usuario, tipo, categoria, monto, descripcion, fecha) values (%s,%s,%s,%s,%s,%s)",
                (usuario, tipo, categoria, monto, descripcion, fecha)
            )
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def consultarPorUsuario(usuario, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("select * from finanzas where usuario=%s", (usuario,))
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print(e)
        return []


def actualizar(id_movimiento, tipo, categoria, monto, descripcion, fecha, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "update finanzas set tipo=%s, categoria=%s, monto=%s, descripcion=%s, fecha=%s where id=%s",
                (tipo, categoria, monto, descripcion, fecha, id_movimiento)
            )
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def eliminar(id_movimiento, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute("delete from finanzas where id=%s", (id_movimiento,))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def obtenerMovimientosIndividuales(usuario, tipo, conexionBD):
    try:
        if conexionBD != None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "select categoria, monto, fecha from finanzas where usuario=%s and tipo=%s order by fecha asc",
                (usuario, tipo)
            )
            return cursor.fetchall()
        else:
            return []
    except Exception as e:
        print(f"Error en BD: {e}")
        return []