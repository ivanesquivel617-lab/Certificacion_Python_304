#El mapa del tesoro
mapa=[
    [".",".",".","."],
    [".",".","x","."],
    [".",".",".","."],
    [".",".",".","."],
]
filas=len(mapa)
columnas=len(mapa)
#Recorrirendo la matriz con ciclos anidados 
#Ciclo externo para manejar filas (i)
for i in range(filas):
    #Ciclo externo para manejar columnas (j)
    for j in range(columnas):
        #Verificamos si encontramos el tesoro
        if mapa[i][j]=="x":
            print(f" Mapa encontrado en la posicion [{i}][{j}]")