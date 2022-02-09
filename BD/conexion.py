import mysql.connector
from mysql.connector.errors import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '12345678',
                db = 'crudbasicpyt'
            )

        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))

    def listarUsuarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM usuarios")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al Intentar la conexion: {0}".format(ex))

    # ***************** FIN OPCION DE ENLISTAR ***************************

    def registrarUsuario(self,usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO usuarios (nombre, apellido, edad, correo) VALUES ('{0}','{1}','{2}','{3}')"
                cursor.execute(sql.format(usuario[0],usuario[1],usuario[2],usuario[3]))
                self.conexion.commit()
                print("¡Usuario Registrado! \n")
            except Error as ex:
                print("Error al Intentar la conexion: {0}".format(ex))

    # ***************** FIN DE OPCION DE REGISTRAR ************************

    def actualizarUsuario(self, usuario):
         if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = """UPDATE usuarios SET nombre = '{0}', apellido = '{1}', edad= '{2}', correo= '{3}'
                         WHERE id = '{4}'"""
                cursor.execute(sql.format(usuario[1],usuario[2],usuario[3],usuario[4],usuario[0]))#Poner indices de acuerdo a como aprecen en la tabla en BD
                self.conexion.commit()
                print("¡Usuario Actualizado! \n")
            except Error as ex:
                print("Error al Intentar la conexion: {0}".format(ex))
                
    #****************** FIN DE OPCION ACUALIZAR *************************

    def eliminarUsuario(self, codigoUsuarioEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM usuarios WHERE id ='{0}'"
                cursor.execute(sql.format(codigoUsuarioEliminar))
                self.conexion.commit()
                print("¡Usuario Eliminado! \n")
            except Error as ex:
                print("Error al Intentar la conexion: {0}".format(ex))

    #****************** FIN DE OPCION ELIMINAR *************************