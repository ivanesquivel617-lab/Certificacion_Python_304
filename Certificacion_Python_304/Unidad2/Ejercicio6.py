tabla = [

    ["Nombre", "Edad", "Calificacion"],
    ["Ivan", 16,9.0],
    ["Sofia", 16,7.0],
    ["Pedro", 17,6.5],
    ["Ivonne", 16,9.0],
    ["Litzy", 16,8.0],
    ["Diana", 16,7.0],
    ["Sherlyn", 16,9.0],
    ["Amanda", 16,9.5],
    ["Maria", 16,8.0],
    ["Jimena", 16,7.5]

]
nombre = input("Introduce el nombre")
filas= len(tabla)
columnas= len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla [i][j] ==nombre :
            print(f" Nombre encontrado en la posicion [{i}][{j}]")
            print(f" Edad {tabla[i][1]}")
            print(f" Calificacion {tabla[i][2]}")