def listarUsuarios(usuarios):
    print("\n Usuarios: \n")
    contador = 1
    for usu in usuarios:
        datos = "{0}. Id: {1} | Nombre: {2} | Apellido: {3} | Edad: {4} | Correo: {5}"
        print(datos.format(contador, usu[0], usu[1], usu[2], usu[3], usu[4]))
        contador = contador+1
    print(" \n")
#****************** FIN DE OPCION ENLISTAR *************************

def pedirDatosRegistro():
    nombre = input("Ingrese el Nombre del cliente: ")
    apellido = input("Ingrese el Apellido del cliente: ")

    edadCorrecta = False
    while (not edadCorrecta):
        edad = input("Ingrese la Edad del cliente: ")
        if edad.isnumeric():
            if (int(edad) > 0):
                edadCorrecta =  True
                edad = int(edad)
            else:
                print("Los creditos deben ser mayor a 0...")
        else:
            print("Edad incorrecta: Debe ser unicamente numero")
    correo = input("Ingrese el Correo del cliente: ")

    usuario = (nombre, apellido, edad, correo)
    return usuario

# ***************** FIN DE OPCION DE REGISTRAR ************************

def pedirDatosActualizacion(usuarios):
    listarUsuarios(usuarios)
    existeCodigo = False
    codigoEditar = int(input("Ingrese el ID del usuario a editar: "))
    for usua in usuarios:
        if usua[0] == codigoEditar:
            existeCodigo = True
            break
    if existeCodigo:
        nombre = input("Ingrese el Nombre del cliente a modificar: ")
        apellido = input("Ingrese el Apellido del cliente a modificar: ")

        edadCorrecta = False
        while (not edadCorrecta):
            edad = input("Ingrese la Edad del cliente a modificar: ")
            if edad.isnumeric():
                if (int(edad) > 0):
                    edadCorrecta =  True
                    edad = int(edad)
                else:
                    print("Los creditos deben ser mayor a 0...")
            else:
                print("Edad incorrecta: Debe ser unicamente numero")
        correo = input("Ingrese el Correo del cliente a modificar: ")

        usuario = (codigoEditar,nombre, apellido, edad, correo)
    else:
        usuario = None

    return usuario

#****************** FIN DE OPCION ACUALIZAR *************************

def pedirDatosEliminacion(usuarios):
    listarUsuarios(usuarios)
    existeCodigo = False
    codigoEliminar = int(input("Ingrese el ID del usuario a eliminar: "))
    for usua in usuarios:
        if usua[0] == codigoEliminar:
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar = ""
    
    return codigoEliminar

#****************** FIN DE OPCION ELIMINAR *************************