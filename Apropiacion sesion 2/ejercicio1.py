# Ejercicio 1
# Realice un programa que calcule el índice de cosecha de un cultivo en función de la cantidad de frutos recolectados y la cantidad de frutos producidos en total.

# in_cosecha = (cantidadrc / cantidadpd) * 100%
cantidadrc = int(input("ingrese la cantidad de frutos recolectados = "))
cantidadpd = int(input("ingrese la cantidad de frutos Producidos = "))
indicecosecha = ((cantidadrc / cantidadpd) * 100)
print ("el Indice De La Cosecha es " , indicecosecha, "%")
