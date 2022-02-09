from BD.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("==== MENÚ PRINCIPAL ====")
            print("1.- Listar Usuarios")
            print("2.- Registrar Usuarios")
            print("3.- Actualizar Usuarios")
            print("4.- Eliminar Usuarios")
            print("5.- Salir")
            print("========================")
            opcion = int(input("Selecciona una opcion: "))

            if opcion <1 or opcion >5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este Sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

#****************** FIN DE OPCION MENU *************************

def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion ==1:
        try:
            usuarios = dao.listarUsuarios()
            if len(usuarios) > 0:
                funciones.listarUsuarios(usuarios)
            else:
                print("No se encontraron registros...")
        except:
            print("Ha ocurrido un error...")

    # ***************** FIN OPCION DE ENLISTAR ***************************

    elif opcion == 2:
        usuario = funciones.pedirDatosRegistro()
        try:
            dao.registrarUsuario(usuario)
        except:
            print("Ha ocurrido un error...")

    # ***************** FIN DE OPCION DE REGISTRAR ************************

    elif opcion == 3:
        try:
            usuarios = dao.listarUsuarios()
            if len(usuarios) > 0:
                usuario = funciones.pedirDatosActualizacion(usuarios)
                if usuario:
                    dao.actualizarUsuario(usuario)
                else:
                    print("ID de Usuario a actualizar no encontrado \n")
            else:
                print("No se encontraron usuarios...\n")
        except:
            print("Ha ocurrido un error...")

    #****************** FIN DE OPCION ACUALIZAR *************************

    elif opcion == 4:
        try:
            usuarios = dao.listarUsuarios()
            if len(usuarios) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(usuarios)
                if not (codigoEliminar == ""):
                    dao.eliminarUsuario(codigoEliminar)
                else:
                    print("ID de Usuario no encontrado...\n")
            else:
                print("No se encontraron usuarios...\n")
        except:
            print("Ha ocurrido un error...")

    #****************** FIN DE OPCION ELIMINAR *************************
    
    else:
        print("Opción no válida")

menuPrincipal()