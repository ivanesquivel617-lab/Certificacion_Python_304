#Realiza un programa que calcule 
#La compra tota, si la compra total 
#Es mayor a 2000 pesos me haga un descuento 
#Del 10%
#Datos de entrada 
precio1=float(input("Introduce el precio de produccto 1:"))
precio2=float(input("Introduce el precio de produccto 2:"))
precio3=float(input("Introduce el precio de produccto 3:"))
precio4=float(input("Introduce el precio de produccto 4:"))

total=precio1+precio2+precio3+precio4
if total>2000:
    total=(total-(total*.10))
    #Total=(3000-(3000*.10))
    print(total)
else:
    print("NO TIENES DESCUENTO")