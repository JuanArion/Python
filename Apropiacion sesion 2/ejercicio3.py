# ejercicio 3

# Un alumno desea saber cuál será su calificación final en la materia
# de Matemáticas. Dicha calificación se compone de los siguientes
# porcentajes: 55% del promedio de sus tres calificaciones parciales
#(se debe leer cada calificación parcial). 30% de la calificación del
# examen final. 15% de la calificación de un trabajo final.

nota1 = float(input("digite la primera nota "))
nota2 =float(input("digite la segunda nota "))
nota3 = float (input("digite la tercera nota "))
examenf = float (input("digite la nota del examen final "))
tallerf = float (input("digite la nota del trabajo final "))
parcial = (nota1+nota2+nota3)/3
notafinal = parcial*0.55+examenf*0.30+tallerf*0.15
print("La nota final es ",notafinal)

