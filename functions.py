#lista de calificaciones de un estudiante
calificaciones = [85, 92, 78, 90, 88]
#calificaciones = []  # Puedes modificar esta lista con las calificaciones del estudiante
#calificaciones = [0, 0, 0]

def promedio_estudiante(calificaciones):
    if len(calificaciones) == 0:
        promedio = float(0)
        return promedio
    promedio = float(sum(calificaciones) / len(calificaciones))
    return promedio

print("El promedio del estudiante es:", promedio_estudiante(calificaciones))