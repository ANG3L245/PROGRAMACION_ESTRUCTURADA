import bcrypt


def generarHash(contrasena):
    return bcrypt.hashpw(contrasena.encode(), bcrypt.gensalt()).decode()


def verificarHash(contrasena, hash_guardado):
    return bcrypt.checkpw(contrasena.encode(), hash_guardado.encode())