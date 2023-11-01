# Ejercicio 1
# Pregunte al usuario cuántos elementos desea ingresar en una lista, luego solicite cada uno de ellos y presente el contenido de la lista y su contenido invertido.

n = int(input("¿Cuántas frases desea ingresar en la lista? "))

mi_lista = []

for i in range(n):
    frase = input(f"Ingrese la frase {i + 1}: ")
    mi_lista.append(frase)
    
print("Lista original:")
for frase in mi_lista:
    print(frase)
    
print("Lista invertida:")
for frase in reversed(mi_lista):
    print(frase)
