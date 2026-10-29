#Declarando una lista 
try:
    materias=["Programacion", "Filosofia", "Matematicas", "Ingles"]
    print(materias[0])
    materias.append("Lengua y comunicacion ")
    print(materias)
    materias[1]="Biologia"
    print(materias)
    materias.remove("Ingles")
    print(materias)
except IndexError:
    print("Indice incorrecto")