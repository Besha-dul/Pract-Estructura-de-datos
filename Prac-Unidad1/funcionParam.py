def calcular_area_triangulo(base,altura):
    area=(base*altura)/2
    return area
resultado = calcular_area_triangulo(10,5)
print(f"El area del triangulo es: {resultado}")


def saludar_persona (nombre,edad):
   print(f"Hola { nombre}, tienes {edad} años. ")
saludar_persona("Elena",28)


#ejemplo
def sumar_numeros(a, b):
    resultado = a + b
    return resultado
total = sumar_numeros(5, 3)
print(f"El resultado de la suma es: {total}")

def dar_bienvenida(nombre):
    print(f"¡Bienvenido al sistema, {nombre}!")

# Llamada a la función cambiando el parámetro
dar_bienvenida("Carlos")
dar_bienvenida("Sofia")

