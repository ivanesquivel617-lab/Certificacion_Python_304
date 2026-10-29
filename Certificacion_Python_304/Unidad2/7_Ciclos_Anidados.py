#Ciclo externo para el numero de la base de la tabla 
for i in range(1,4):
    print(f"---Tabla del {i}---")
    #Ciclo interno mos multiplica la base(i) por el numero(j)
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print(f"Aqui termine la tabla del {i}")