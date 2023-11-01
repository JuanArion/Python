def tabla(numero):
    limite = 10
    contador = 1
    while contador <= limite:
        resultado =contador * numero
        print ("{} x {} = {}".format( numero, contador, resultado))
        contador = contador + 1

tabla(34)
