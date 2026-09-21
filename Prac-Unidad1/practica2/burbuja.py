lista = [2,3,6,8,10,7,8,9,4,5,10,3,4,8]
n = len(lista)
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if lista[i]>lista[i+1]:
            lista[i],lista[i+1]=lista[i+1],lista[i]
            swapped = True
print("Lista Ordenada: ", lista)

#cambiando el signo < se realiza la lista de forma descendente :D