#Ejemplo 1 sin manejo de excepciones 
try:
    numero1=float(input("Ingresa el primer numero:"))
    numero2=float(input("Imgresa el segundo numero:"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir un numero entre cero")
except ValueError:
    print("Error: no se puede intrioducir letras")