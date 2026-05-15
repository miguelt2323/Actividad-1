class Producto:
    def __init__(self, codigo, nombre, precio, cantidad, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def mostrar_info(self):
        return f"""
Codigo: {self.codigo}
Nombre: {self.nombre}
Precio: ${self.precio}
Cantidad: {self.cantidad}
Categoria: {self.categoria}
---------------------------
"""


class SistemaInventario:
    def __init__(self):
        self.productos = []

    # 1. Registrar producto
    def registrar_producto(self):

        codigo = input("Ingrese codigo del producto: ").strip()

        if codigo == "":
            print("Error: El codigo no puede estar vacio")
            return

        # Validar codigo repetido
        for prod in self.productos:
            if prod.codigo == codigo:
                print("Error: El codigo ya existe")
                return

        nombre = input("Ingrese nombre del producto: ").strip()

        if nombre == "":
            print("Error: El nombre no puede estar vacio")
            return

        # Validar precio
        while True:
            precio = float(input("Ingrese precio: "))

            if precio >= 0:
                break
            else:
                print("Error: El precio no puede ser negativo")

        # Validar cantidad
        while True:
            cantidad = int(input("Ingrese cantidad disponible: "))

            if cantidad >= 0:
                break
            else:
                print("Error: La cantidad no puede ser negativa")

        categoria = input("Ingrese categoria: ").strip()

        if categoria == "":
            print("Error: La categoria no puede estar vacia")
            return

        nuevo_producto = Producto(
            codigo,
            nombre,
            precio,
            cantidad,
            categoria
        )

        self.productos.append(nuevo_producto)

        print("Producto registrado correctamente")

    # 2. Mostrar productos
    def mostrar_productos(self):

        if len(self.productos) == 0:
            print("No hay productos registrados")
        else:
            print("\n===== LISTA DE PRODUCTOS =====")

            for prod in self.productos:
                print(prod.mostrar_info())

    # 3. Buscar producto
    def buscar_producto(self):

        print("""
1. Buscar por codigo
2. Buscar por nombre
""")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":

            codigo_buscar = input("Ingrese codigo: ")

            for prod in self.productos:
                if prod.codigo == codigo_buscar:
                    print("\nProducto encontrado")
                    print(prod.mostrar_info())
                    return

            print("Producto no encontrado")

        elif opcion == "2":

            nombre_buscar = input("Ingrese nombre: ").lower()

            for prod in self.productos:
                if prod.nombre.lower() == nombre_buscar:
                    print("\nProducto encontrado")
                    print(prod.mostrar_info())
                    return

            print("Producto no encontrado")

        else:
            print("Opcion invalida")

    # 4. Actualizar producto
    def actualizar_producto(self):

        codigo_buscar = input("Ingrese codigo del producto: ")

        for prod in self.productos:

            if prod.codigo == codigo_buscar:

                print("\nProducto encontrado")

                # Actualizar precio
                while True:
                    nuevo_precio = float(input("Nuevo precio: "))

                    if nuevo_precio >= 0:
                        prod.precio = nuevo_precio
                        break
                    else:
                        print("Precio invalido")

                # Actualizar cantidad
                while True:
                    nueva_cantidad = int(input("Nueva cantidad: "))

                    if nueva_cantidad >= 0:
                        prod.cantidad = nueva_cantidad
                        break
                    else:
                        print("Cantidad invalida")

                # Actualizar categoria
                nueva_categoria = input("Nueva categoria: ").strip()

                if nueva_categoria != "":
                    prod.categoria = nueva_categoria
                else:
                    print("Categoria vacia, no se actualizo")

                print("Producto actualizado correctamente")
                return

        print("Producto no encontrado")

    # 5. Eliminar producto
    def eliminar_producto(self):

        codigo_eliminar = input("Ingrese codigo del producto a eliminar: ")

        for prod in self.productos:

            if prod.codigo == codigo_eliminar:
                self.productos.remove(prod)

                print("Producto eliminado correctamente")
                return

        print("Producto no encontrado")

    # 6. Calcular total inventario
    def calcular_total_inventario(self):

        total = 0

        for prod in self.productos:
            total += prod.precio * prod.cantidad

        print(f"\nValor total del inventario: ${total}")

    # 7. Mostrar productos agotados
    def mostrar_agotados(self):

        agotados = False

        print("\n===== PRODUCTOS AGOTADOS =====")

        for prod in self.productos:

            if prod.cantidad == 0:
                print(prod.mostrar_info())
                agotados = True

        if agotados == False:
            print("No hay productos agotados")

    # 8. Guardar archivo txt
    def guardar_archivo(self):

        with open("inventario.txt", "w") as archivo:

            for prod in self.productos:
                archivo.write(prod.mostrar_info() + "\n")

        print("Archivo guardado correctamente")

    # Menu principal
    def menu(self):

        while True:

            print("""
========== MENU INVENTARIO ==========
1. Registrar producto
2. Mostrar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Calcular total inventario
7. Mostrar productos agotados
8. Guardar archivo
9. Salir
=====================================
""")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar_producto()

            elif opcion == "2":
                self.mostrar_productos()

            elif opcion == "3":
                self.buscar_producto()

            elif opcion == "4":
                self.actualizar_producto()

            elif opcion == "5":
                self.eliminar_producto()

            elif opcion == "6":
                self.calcular_total_inventario()

            elif opcion == "7":
                self.mostrar_agotados()

            elif opcion == "8":
                self.guardar_archivo()

            elif opcion == "9":
                print("Saliendo del sistema...")
                break

            else:
                print("Opcion invalida")


# Ejecutar sistema
sistema = SistemaInventario()
sistema.menu()