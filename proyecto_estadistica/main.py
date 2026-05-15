from src.estadistica import calcular_promedio, contar_aprobados, promedio_diccionario,clasificar_notas


datos = [25,150,200,300,350]

resultado = calcular_promedio(datos)

print("El promedio de la lista es: ",resultado)

notas = {
    "Sara": 5.0,
    "Sofia": 4.5,
    "Pau": 5.5,
    "Vanessa": 6.0
}

promedio_notas = promedio_diccionario(notas)
print("El promedio del diccionario es: ",promedio_notas)

aprobados = contar_aprobados(notas,3.5)
print("El numero de estudiantes aprobados es: ",aprobados)

clasificar_notas = clasificar_notas(notas)
print("Clasificación de notas: ",clasificar_notas)


