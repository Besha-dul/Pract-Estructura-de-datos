import numpy as np
#Creacion de matriz 2x2
A= np.array([[10,15],[20,5]])
B= np.array([[5,12],[15,8]])

#SUMA ELEMENTOS
suma=A+B
print("--Total de productos vendidos (Sabado + Domingo)--")
print(suma)

#MULTIPLICACION
multi=suma*50
print("--Ingreso toral en pesos (a 50 pesos por producto)--")
print(multi)