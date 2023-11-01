# ejercicio 2
# En una escuela se permite la inscripción de sus alumnos a las siguientes actividades deportivas: futbol (f), baloncesto (b). Realice un programa que permita ingresar el nombre de sus estudiantes e inscribir a cada uno en uno o los dos deportes.
# La aplicación debe mostrar los siguientes listados:

# Estudiantes inscritos en fulbol
# Estudiantes inscritos en baloncesto
# Estudiantes inscritos en ambos deportes
# Todos los estudiantes inscritos en algún deporte
# Estudiantes inscritos en solo un deporte.

# Creamos un diccionario vacío para almacenar los estudiantes y sus deportes
estudiantes = {}

# Pedimos al usuario que ingrese el número de estudiantes que desea inscribir
num_estudiantes = int(input("Ingrese el número de estudiantes que desea inscribir: "))

# Iteramos sobre el número de estudiantes y pedimos al usuario que ingrese su nombre y deportes
for i in range(num_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    deportes = input("Ingrese los deportes en los que desea inscribir al estudiante (f para fútbol, b para baloncesto): ")
    
    # Agregamos el estudiante y sus deportes al diccionario
    estudiantes[nombre] = deportes

# Generamos las listas solicitadas
futbol = []
baloncesto = []
ambos = []
alguno = []
uno_solo = []

for nombre, deportes in estudiantes.items():
    if "f" in deportes:
        futbol.append(nombre)
    if "b" in deportes:
        baloncesto.append(nombre)
    if "f" in deportes and "b" in deportes:
        ambos.append(nombre)
    if "f" in deportes or "b" in deportes:
        alguno.append(nombre)
    if len(deportes) == 1:
        uno_solo.append(nombre)

# Mostramos las listas generadas
print("Estudiantes inscritos en fútbol:", futbol)
print("Estudiantes inscritos en baloncesto:", baloncesto)
print("Estudiantes inscritos en ambos deportes:", ambos)
print("Todos los estudiantes inscritos en algún deporte:", alguno)
print("Estudiantes inscritos en solo un deporte:", uno_solo)












