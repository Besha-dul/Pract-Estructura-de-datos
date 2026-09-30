#PRACTICA DE LABORATORIO "REGISTRO Y EVALUACIÓN DE CALIFICACIONES"

#Mostrar encabeza de la escuela (sin parametros :D)
def mostrar_titulo ():
    print("UNIVERSIDAD TECNOLOGICA DE XICOTEPEC DE JUEAREZ")
    print("REPORTE DE CALIFICACIONES")
    print("")


#Obtener la nota minima para aprobar (sin parametros :D)
def obtener_nota_minima():
    return 6.0

#Evaluar el rendimiento del alumno (con 1 parametro)
def evaluar_rendimiento(nota_final): 
    if nota_final < 7.0:
        return "Reprobado"
    else nota_final <= 9.4:
        return "Aprobado"
    else: 
        return "Excelente"


#Calcular
def calcualar_promedio(nota_examenes, nota_tareas):
    promedio = (nota_examenes * 0.7 ) + (nota_tareas * 0.3)
    return round (promedio,  1) 

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    #Integrar funciones 
    nota_final = calcualar_promedio(nota_examenes,  nota_tareas)
    nota_minima = obtener_nota_minima()
    estado = evaluar_rendimiento(nota_final)

    print(f"Alumno: {nombre_alumno}")
    print(f"Nota Examenes (70%): {nota_examenes}")
    print(f"Nota Tareas (30%): {nota_tareas}")
    print(f"Nota final: {nota_final} ")
    print(f"Estado: {estado}")

    if nota_final < nota_minima:
        print(f"Debe presentar examen extraordinario. La nota minima es {nota_minima}")
    else: 
        print(f"No necesita hacer el examen extra, PASO!!!!")