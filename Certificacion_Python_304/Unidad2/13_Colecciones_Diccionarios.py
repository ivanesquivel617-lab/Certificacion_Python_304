#Creando un diccionario
persona={
    "Nombre":"Ivan",
    "Edad":16,
    "Profesion":"Programador",
    "Estudiante":True
}
print(persona)
#Accediendo a un valor en especifico
print(persona["Nombre"])
#Se puede usarel metodo get()
#Es util porque no marca error si el valor no existe 
print(persona.get("Profesion"))
#Modificar un valor
persona["Estudiante"]=False
print(persona["Estudiante"])
#Agregar un par(clave:valor)
persona["Equipo"]="Nacaxa"
print(persona)
#Recorrer un diccionario con un bucle