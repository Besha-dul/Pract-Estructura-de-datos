from collections import dequeimport time

cola_reproduccion=deque()

#El usuario agrega canciones
cola_reproduccion.apped("1. Californica")
cola_reproduccion.apped("2. Historia de amor")
cola_reproduccion.apped("3. Historia entre dedos")

#Mostrar las canciones en espera
print("canciones en espera: ")

for cancion in cola_reproduccion: 
    print (" _", cancion)
    print("iniciando reproduccion")

    #El ewproductor procesa la cola cancion por cancion 
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Sonando ahora{cancion_actual}")
    time.sleep(1) #simula la duracion del tema 
    print(f"Finalizo: "{cancion_actual})

    #Muestra cuantas canciones quedan en la cola 
    print(f"Quedan {len(cola_reproduccion)} canciones en la cola")
    print("la cola de reproduccion ha termiando")


