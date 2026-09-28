import datetime
def saludar():
    print("Hola. bienvenida!")
saludar()

#def mostrar_hora():
    #hora_actual=datetime.Now().strftime("%H","%M","%S")
    #print(f"La hora actual es:{hora_actual}")

#mostrar_hora()

#Now() consulta el reloj o la hora sel SO
#Strftime convierte la fecha y hora en texto, usando el formato establecido
#f-string la letra f indica a python que procese el texto e inserte las variables dentro de las llaves
#{hora_actual} se toma el valor almacenado en la variable de hora_actual y lo reemplaza ahi mismo  

#ejemplo 
def decir_hora():
    print("Son las 12:00 de la tarde.")

# Llamada a la función
decir_hora()


def mostrar_menu():
    print("===BIENVENIDO===")
    print("Menu opciones")
    print("1. Entrada")
    print("2. Plato principal")
    print("3. Postre")
mostrar_menu()