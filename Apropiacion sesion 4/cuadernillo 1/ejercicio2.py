# 2 ejercicio 2
# Solicite al usuario dos frases y devuelva una lista con todas las letras que se repiten en la misma posición de ambas frases
# f1: hola mundo f2: como estas:

frase1 = input("ingresa la primera frase")
frase2 = input("ingresa la segunda frase")
lista = []

frase_completa = min(len(frase1), len(frase2))
for inicio in range (frase_completa):
    if frase1[inicio] == frase2[inicio]:
        lista.append(frase1[inicio])
        print (lista)