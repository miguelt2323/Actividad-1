class Estudiante:
    contadorAprobados = 0
    contadorNoAprobado = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota

        if self.nota >= 3:
            Estudiante.contadorAprobados += 1
        else:
            Estudiante.contadorNoAprobado += 1

    def mostrar_info(self):
        if self.nota >= 3:
            estado = "Aprueba"
        else:
            estado = "Reprueba"
        return f"Nombre: {self.nombre}, Nota: {self.nota}, Estado: {estado}"

estudent = []

for i in range(3):
    print(f"\nRegistro del estudiante{i+1}")
    nombre = input("nombre: ")

    while True:
        nota = float(input("Ingrese la nota (0 -5): "))
        if nota >= 0 and nota <=5:
            break
        else:
            print("Nota no valida")
        
   
    e = Estudiante(nombre, nota)
    estudent.append(e)

print("\nLista de estudiante")
for est in estudent:
    print(est.mostrar_info())

print("\n-----Resumen-----")
print("Aprobados: ", Estudiante.contadorAprobados)
print("Reprobados: ", Estudiante.contadorNoAprobado)