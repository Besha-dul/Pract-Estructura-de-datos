# PRACTICA DE LABORATORIO "REGISTRO Y EVALUACIÓN DE CALIFICACIONES"

# Mostrar encabezado de la escuela (sin parámetros :D)
def mostrar_titulo():
    print("UNIVERSIDAD TECNOLÓGICA DE XICOTEPEC DE JUÁREZ")
    print("REPORTE DE CALIFICACIONES")
    print("")

# Obtener la nota mínima para aprobar (sin parámetros :D)
def obtener_nota_minima():
    return 6.0

# Evaluar el rendimiento del alumno (con 1 parámetro)
def evaluar_rendimiento(nota_final):
    if nota_final < 6.0:          
        return "Reprobado"
    elif nota_final <= 9.4:
        return "Aprobado"
    else:
        return "Excelente"

# Calcular promedio
def calcular_promedio(nota_examenes, nota_tareas): 
    promedio = (nota_examenes * 0.7) + (nota_tareas * 0.3)
    return round(promedio, 1)

def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    # Integrar funciones
    mostrar_titulo()              
    nota_final = calcular_promedio(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima()
    estado = evaluar_rendimiento(nota_final)
    
    print(f"Alumno: {nombre_alumno}")
    print(f"Nota Exámenes (70%): {nota_examenes}")
    print(f"Nota Tareas (30%): {nota_tareas}")
    print(f"Nota final: {nota_final}")
    print(f"Estado: {estado}")
    
    if nota_final < nota_minima:
        print(f"Debe presentar examen extraordinario. La nota mínima es {nota_minima}")
    else:
        print(f"No necesita hacer el examen extra, ¡¡¡¡PASÓ!!!!")


# 1. Llamamos a la función para generar la boleta con datos de prueba
generar_boleta("Juan Pérez", 8.5, 9.0)


