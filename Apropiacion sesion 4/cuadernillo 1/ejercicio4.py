# ejercicio 4

# Leer una frase y almacenar en una tupla la frase leída pero sin espacios. Mostrar el contenido de la tupla.


frase = input("Por favor, ingresa una frase: ")
tupla = tuple(frase.replace(" ", ""))
print("tu frase ingresda es: ",frase)
print(tupla)
