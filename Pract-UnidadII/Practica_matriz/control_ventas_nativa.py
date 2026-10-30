#Creacion d matriz 3x3

matrizA=[[10,15], [20,5],]
print("Mtraiz A: " ,matrizA)

matrizB=[[5,12],[15,8],]
print("Matriz B: ",matrizB)

#Suma de forma nativa 
total_nativo =[[0,0], [0,0]] #se crea una matriz vacia para guardar el resultado 
for i in range(2): #Recorre las filas osea las sucursales 
    for j in range(2): #recorre las dos columnas osea las productos 
        total_nativo[i][j] = matrizA[i][j] + matrizB[i][j] #recorre las 4 casillas (10 + 5) etc

print("--Total de productos vendidos (Sabado + Domingo)--")
print(total_nativo)

#Multiplicacion de matricez 
precio = 50
ingreso_total =[[0,0] ,[0,0]] #se crea una matriz vacia para guardar el resultado 
for i in range (2):
    for j in range(2):
        ingreso_total[i][j] = total_nativo[i][j]*precio 

print("--Ingreso toral en pesos (a 50 pesos por producto)--")
print(ingreso_total)