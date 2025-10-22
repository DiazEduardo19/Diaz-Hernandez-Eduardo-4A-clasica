from database import crear_conexion

def validar_credenciales(usuario, contraseña):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE nombre = %s AND clave = %s", (usuario, contraseña))
            resultado = cursor.fetchone()
            return resultado is not None
        except Exception as e:
            print(f"Error al validar credenciales: {e}")
            return False
        finally:
            conexion.close()
    return False