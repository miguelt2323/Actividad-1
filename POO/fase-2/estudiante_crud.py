class Estudiante:
    def __init__(self, codigo, nombre, nota):
        self.codigo = codigo
        self.nombre = nombre
        self.nota = nota

    def estado(self):
        if self.nota >= 3:
            return "Aprueba"
        else:
            return "Reprueba"
        
    def mostrar_info(self):
        return f"Codigo: {self.codigo} Nombre: {self.nombre} Nota: {self.nota} Estado: {self.estado()}"
    
class SistemaEstudiantes:
    def __init__(self):
        self.estudiantes =[]

    def registrar_estudiante(self):
        codigo = input("Codigo del estudiante: ")

        for est in self.estudiantes:
            if est.codigo == codigo:
                print("Error: El codigo ya existe")
                return
        nombre = input("Nombre: ")

        while True:
            nota = float(input("Nota(0 - 5): "))

            if 0 <= nota <= 5:
                break
            else:
                print("Nota invalida")
        nuevo_estudiante = Estudiante(codigo, nombre, nota)
        self.estudiantes.append(nuevo_estudiante)
        print("Estudiante registrado correctamente")

    def mostrar_estudiantes(self):

        if len(self.estudiantes)== 0:
            print("No hay estudiantes registrados")
        else:
            print("\n LISTA DE ESTUDIANTES")
            
            for est in self.estudiantes:
                print(est.mostrar_info())

    def buscar_estudiante(self):
        codigo_buscar = input("Ingrese el codigo a buscar: ")

        for est in self.estudiantes:
            if est.codigo == codigo_buscar:
                print("\nEstudiante encontrado")
                print(est.mostrar_info())
                return
            
        print("Estudiante no encontrado")

    def menu(self):
        while True:
            print("""
                  ======= MENU ======
                  1. Registrar estudiante
                  2. Mostrar estudiante
                  3. Buscar estudiante
                  4. Eliminar estudiante
                  5. Actualizar nota
                  6. Calcular promedio
                  7. Guardar archivo
                  8. Estadisticas
                  9. Salir""")
            opcion = input("Seleccione una opcionn: ")
            if opcion == "1":
                self.registrar_estudiante()
            elif opcion == "2":
                self.mostrar_estudiantes()
            elif opcion == "3":
                self.buscar_estudiante()
            elif opcion == "4":
                self.eliminar_estudiante()
            elif opcion == "5":
                self.actualizar_nota()
            elif opcion ==  "6":
                self.calcular_promedio()
            elif opcion == "7":
                self.guardar_archivo()
            elif opcion == "8":
                self.estadisticas()
            elif opcion == "9":
                print("Saliendo del sistema")
                break

    def eliminar_estudiante(self):
        codigo_eliminar = input("Ingrese el codigo a eliminar: ")

        for est in self.estudiantes:
             if est.codigo == codigo_eliminar:
                 self.estudiantes.remove(est)
                 print("Estudiante eliminado correctamente")
                 return
             
        print("Estudiante no encontrado")
    
    def actualizar_nota(self):
        codigo_buscar = input("Ingrese el codigo del estudiante: ")

        for est in self.estudiantes:
            if est.codigo == codigo_buscar:

                while True:
                    nueva_nota = float(input("Ingrese nueva nota: "))

                    if 0 <= nueva_nota <= 5:
                        est.nota = nueva_nota
                        print("Nota actualizada correctamente")
                        return
                    else:
                        print("Nota invalida")
        print("Estudiante no encontrado")

    def calcular_promedio(self):
        
        if len(self.estudiantes)== 0:
            print("No hay estudiantes registrados: ")
            return
        
        suma = 0
        for est in self.estudiantes:
            suma += est.nota
        promedio = suma / len(self.estudiantes)
        print(f"\nPromedio general: {promedio: .2f}")

    def guardar_archivo(self):
        with open("estudiantes.txt", "w") as archivo:
            for est in self.estudiantes:
                archivo.write(est.mostrar_info()+"\n")
        print("Archivo guardado correctamente")

    def estadisticas(self):

        aprobados = 0
        reprobados = 0

        for est in self.estudiantes:
            if est.nota >= 3:
                aprobados += 1
            else:
                reprobados += 1

        print("\n -- ESTADISTICAS --")
        print("Aprobados: ", aprobados)
        print("Reprobados: ", reprobados)

sistema = SistemaEstudiantes()
sistema.menu()

