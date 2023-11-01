# ejercicio 4
# Recibir una frase por parte del usuario y devolver el número de palabras
#que se encuentran en la frase.


frase = input("Ingrese la frase:" )
print("La frase es:", frase)

resultado = len(frase.split())
print ("La cantidad de palabras de la frase es: ",resultado, "palabras")
