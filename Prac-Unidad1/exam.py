#examen 

defburbujs(lista):
    lista=lista.copy()
    n=len(lista) 
    for i in range(n):
        for j in range(n-1-i):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1] = lista[j+1],lista[j]
                return lista

def seleccion(lista):
    lista=lista.copy()
    n = len(lista)
    for i in range(n):
        menor = i
        for j in range (i+1,n):
            if lista[j] < lista[menor]:
                menor = j lista[i], lista[menor]=lista[menor], lista[i]
                return lista

 def insercion(lista): 
    lista=lista.copy()
    for i in range (1,len(lista)):
        actual = lista[i]
        j = i - 1
        while j>= 0 and lista[j] > actual: lista[j+1]=
