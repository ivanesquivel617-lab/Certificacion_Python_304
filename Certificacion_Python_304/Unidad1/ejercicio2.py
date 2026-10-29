try:
    alumnos=["Pedro", "Ivone", "Litzi", "Diana", "Maria"]
    califiaciones=["6.7", "8.0", "0.67", "9.1", "9.0"]
    print(alumnos[0],califiaciones[0])
    print(alumnos[2],califiaciones[2])
    print(alumnos[4],califiaciones[4])
except IndexError:
    print("No se encuentra el alumno, menos la calificacion")
