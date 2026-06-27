class Usuario:
    def __init__(self, documento, nombre, correo, rol, estado):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo
        self.rol = rol
        self.estado = estado

    def mostrar_info(self):
        return f"""
Documento: {self.documento}
Nombre: {self.nombre}
Correo: {self.correo}
Rol: {self.rol}
Estado: {self.estado}
-----------------------------
"""


class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    # 1. Registrar usuario
    def registrar_usuario(self):

        documento = input("Ingrese documento: ").strip()

        if documento == "":
            print("Error: Documento vacio")
            return

        # Validar documento unico
        for user in self.usuarios:
            if user.documento == documento:
                print("Error: El documento ya existe")
                return

        nombre = input("Ingrese nombre: ").strip()

        if nombre == "":
            print("Error: Nombre vacio")
            return

        correo = input("Ingrese correo: ").strip()

        # Validar correo
        if "@" not in correo or "." not in correo:
            print("Error: Correo invalido")
            return

        # Validar correo repetido
        for user in self.usuarios:
            if user.correo == correo:
                print("Error: El correo ya existe")
                return

        roles_validos = ["Administrador", "Aprendiz", "Instructor"]

        print("\nRoles disponibles:")
        for rol in roles_validos:
            print("-", rol)

        rol = input("Ingrese rol: ").strip()

        if rol not in roles_validos:
            print("Error: Rol invalido")
            return

        estados_validos = ["Activo", "Inactivo"]

        estado = input("Ingrese estado (Activo/Inactivo): ").strip()

        if estado not in estados_validos:
            print("Error: Estado invalido")
            return

        nuevo_usuario = Usuario(
            documento,
            nombre,
            correo,
            rol,
            estado
        )

        self.usuarios.append(nuevo_usuario)

        print("Usuario registrado correctamente")

    # 2. Mostrar usuarios
    def mostrar_usuarios(self):

        if len(self.usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            print("\n===== LISTA DE USUARIOS =====")

            for user in self.usuarios:
                print(user.mostrar_info())

    # 3. Buscar usuario
    def buscar_usuario(self):

        print("""
1. Buscar por documento
2. Buscar por correo
""")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            documento_buscar = input("Ingrese documento: ")

            for user in self.usuarios:
                if user.documento == documento_buscar:
                    print("\nUsuario encontrado")
                    print(user.mostrar_info())
                    return

            print("Usuario no encontrado")

        elif opcion == "2":

            correo_buscar = input("Ingrese correo: ")

            for user in self.usuarios:
                if user.correo == correo_buscar:
                    print("\nUsuario encontrado")
                    print(user.mostrar_info())
                    return

            print("Usuario no encontrado")

        else:
            print("Opcion invalida")

    # 4. Actualizar usuario
    def actualizar_usuario(self):

        documento_buscar = input("Ingrese documento del usuario: ")

        for user in self.usuarios:

            if user.documento == documento_buscar:

                print("\nUsuario encontrado")

                nuevo_nombre = input("Nuevo nombre: ").strip()

                if nuevo_nombre != "":
                    user.nombre = nuevo_nombre

                nuevo_correo = input("Nuevo correo: ").strip()

                if "@" in nuevo_correo and "." in nuevo_correo:
                    user.correo = nuevo_correo
                else:
                    print("Correo invalido, no se actualizo")

                roles_validos = ["Administrador", "Aprendiz", "Instructor"]

                nuevo_rol = input("Nuevo rol: ").strip()

                if nuevo_rol in roles_validos:
                    user.rol = nuevo_rol
                else:
                    print("Rol invalido, no se actualizo")

                estados_validos = ["Activo", "Inactivo"]

                nuevo_estado = input("Nuevo estado: ").strip()

                if nuevo_estado in estados_validos:
                    user.estado = nuevo_estado
                else:
                    print("Estado invalido, no se actualizo")

                print("Usuario actualizado correctamente")
                return

        print("Usuario no encontrado")

    # 5. Eliminar usuario
    def eliminar_usuario(self):

        documento_eliminar = input("Ingrese documento del usuario a eliminar: ")

        for user in self.usuarios:

            if user.documento == documento_eliminar:
                self.usuarios.remove(user)

                print("Usuario eliminado correctamente")
                return

        print("Usuario no encontrado")

    # 6. Mostrar usuarios activos
    def mostrar_activos(self):

        activos = False

        print("\n===== USUARIOS ACTIVOS =====")

        for user in self.usuarios:

            if user.estado == "Activo":
                print(user.mostrar_info())
                activos = True

        if activos == False:
            print("No hay usuarios activos")

    # 7. Contar usuarios por rol
    def contar_roles(self):

        administradores = 0
        aprendices = 0
        instructores = 0

        for user in self.usuarios:

            if user.rol == "Administrador":
                administradores += 1

            elif user.rol == "Aprendiz":
                aprendices += 1

            elif user.rol == "Instructor":
                instructores += 1

        print("\n===== USUARIOS POR ROL =====")
        print("Administradores:", administradores)
        print("Aprendices:", aprendices)
        print("Instructores:", instructores)

    # 8. Guardar archivo txt
    def guardar_archivo(self):

        with open("usuarios.txt", "w") as archivo:

            for user in self.usuarios:
                archivo.write(user.mostrar_info() + "\n")

        print("Archivo guardado correctamente")

    # Menu principal
    def menu(self):

        while True:

            print("""
========== MENU USUARIOS ==========
1. Registrar usuario
2. Mostrar usuarios
3. Buscar usuario
4. Actualizar usuario
5. Eliminar usuario
6. Mostrar usuarios activos
7. Contar usuarios por rol
8. Guardar archivo
9. Salir
===================================
""")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar_usuario()

            elif opcion == "2":
                self.mostrar_usuarios()

            elif opcion == "3":
                self.buscar_usuario()

            elif opcion == "4":
                self.actualizar_usuario()

            elif opcion == "5":
                self.eliminar_usuario()

            elif opcion == "6":
                self.mostrar_activos()

            elif opcion == "7":
                self.contar_roles()

            elif opcion == "8":
                self.guardar_archivo()

            elif opcion == "9":
                print("Saliendo del sistema...")
                break

            else:
                print("Opcion invalida")


# Ejecutar sistema
sistema = SistemaUsuarios()
sistema.menu()