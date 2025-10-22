from database import crear_conexion

def obtener_usuarios():
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre FROM usuarios")
            usuarios = cursor.fetchall()
            return usuarios
        except Exception as e:
            print(f"Error al obtener usuarios: {e}")
            return []
        finally:
            conexion.close()
    return []

def actualizar_usuario(id_usuario, nuevo_nombre):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE usuarios SET nombre = %s WHERE id = %s", (nuevo_nombre, id_usuario))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False
        finally:
            conexion.close()
    return False

def eliminar_usuario(id_usuario):
    conexion = crear_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False
        finally:
            conexion.close()
    return False