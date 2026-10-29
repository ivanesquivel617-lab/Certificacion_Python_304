cadena1='Hola'
cadena2='Mundo'
multilinea="""Esto es una cadena
de varias lineas"""
print(cadena1 + cadena2)#Print(f2{Cadena1})
#Cadenas y Repeticion
eco="ja"*6700
print(eco)
#Cambiar una cadena de miniscula a mayuscula 
tu_nombre='Ivan'
print(tu_nombre.upper())
#Cambiar una cadena de mayuscula a miniscula
print(tu_nombre.lower())
#Remplazar texto en una cadena
frase="Me gusta programacion"
print(frase.replace("programacion", "matematicas"))
#Formato de cadenas (F-String)
edad=16
Nombre='Ivan'
mensaje=f"Hola, me llamo\n{Nombre}\ny tengo\n{edad}\naños"
print(mensaje)
#Contar los caracteres de una cadena 
texto= " ¡Felicidades por continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprobar si un texto contiene una palabra
oracion="Aprender python es divertido"
if "java" in oracion:
    print("Encontrado")
else:
    print("No esta")
    #Validar contenido de una cadena
nlista="16"
print(nlista.isalpha())
print(nlista.isdigit())