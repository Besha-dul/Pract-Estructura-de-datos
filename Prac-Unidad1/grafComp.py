import matplotlib.pyplot as plt 
datos=[42,12,88,23,7,65,34,50]

#Algoritmo de INSERCION 
def insercion(arr):
    a = arr.copy()
    comp=0
    for i in range(1,len(a)):
        clave,j=a[i],i-1
        while j>=0 and a[j]>clave: 
            comp+=1
            a[j+1]=a[j]
            j-=1
        if j>0: comp+=1
        a[j+1]=clave
    return a, comp

#Algoritmo de SELECCION 
def seleccion(arr):
    a = arr.copy()                  # CORREGIDO: Uso de '=' en lugar de ':'
    comp = 0
    n = len(a)                      # CORREGIDO: Uso de '=' en lugar de ':'
    for i in range(n - 1):          # CORREGIDO: Estructura del bucle externo
        min_idx = i
        for j in range(i + 1, n):   # CORREGIDO: Bucle interno necesario para comparar
            comp += 1
            if a[j] < a[min_idx]:
                min_idx = j 
        a[i], a[min_idx] = a[min_idx], a[i] # CORREGIDO: Intercambio fuera del bucle interno
    return a, comp 


#EJECUTAMOS AMBOS ALGORITMOS 
lista_ordenada, comp_ins=insercion(datos)
_, comp_Sel=seleccion(datos)

#GRAFICAMOS
fig,(ax1,ax2,ax3)=plt.subplots(1,3, figsize=(12,3.5))

#GRAFICO 1 INICAL-LISTA DESORDENADA     
ax1.bar(range(len(datos)),datos,color='salmon')
ax1.set_title('1.- Lista Desordenada')
ax1.set_ylabel('valor')

#GRAFCO 2 LISTA ORDENADA 
ax2.bar(range(len(lista_ordenada)),lista_ordenada,color='green')
ax2.set_title('2.- LISTA ORDENADA')

#GRAFICO 3 COMPARACIONES REALIZADAS 
ax3.bar(['insercion', 'seleccion'],[comp_ins,comp_Sel],color=["#2397EA", "#ac8059"])
ax3.set_title('3.- COMPARACIONES')
ax3.set_ylabel('cantidad')

plt.tight_layout()
plt.show()