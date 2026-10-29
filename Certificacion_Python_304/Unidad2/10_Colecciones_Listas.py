carrito=[]
Num_productos=int(input("Ingresa el numero de productos:"))
for i in range(Num_productos):
    producto=input("Ingresa el producto a tu carrito:")
    carrito.append(producto)
print("Lista creada correctamente")
carrito[0]="barritas"
print(carrito[0])
print(carrito[1])
print(carrito)                                      