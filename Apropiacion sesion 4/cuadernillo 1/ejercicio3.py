# ejercicio 3

# Cree una aplicación que presente un menú con las siguientes opciones:
# Aplicaciones con Listas

# 1. Ingresar lista nueva
# 2. Ordenar lista
# 3. Promedio lista
# 4. Buscar elemento
# 5. Salir
# Ingresar lista solicita los elementos de una lista, terminando con el ingreso de un número negativo el cual no formará parte de la lista

# Ordenar lista Presenta los valores de la lista ordenados.

# Promedio lista Muestra el promedio de los valores de la lista

# Buscar elemento solicita un número a buscar en la lista e indica si se encuentra en ella y cuántas veces aparece.

# Salir Termina la ejecución del programa
opcion = []
while True:
    print(" ")
    print("Aplicaciones Con Listas\n")

    print("[1]. Ingresar Lista Nueva")

    print("[2]. Ordenar Lista")

    print("[3]. Promedio Lista")

    print("[4]. Buscar Elemento")

    print("[5]. Salir")
    print (" ")
     
    opcion = int(input("escoge la opcion que deseas realizar: "))
    if opcion >= 5:
        print ("!Haz Seleccionado Salir!")
        break
    elif opcion == 1:
       
        lista = []
        i = 0
        while True:
            num = int(input(f"ingrese el número {i + 1}:  "))
            if num == 0:
                break
            lista.append(num)
            i += 1
        print (f" su lista creada es : {lista}")
        
    elif opcion == 2:
        lista.sort()
        print (f"su lista ordenada es : ", lista )
    elif opcion == 3:
        print("El Promedio De Los Valores De La Lista Es: ", sum(lista)/len(lista), "\n")
    elif opcion == 4:
        buscar = int(input("Ingrese Un Número Que Quiera Buscar En La Lista: "))
        cantidad_veces = lista.count(buscar)
        if cantidad_veces > 0:
            print ("si está y está ", cantidad_veces ,"veces.")
        else:
            print("El Número No Está En La Lista\n")
      

        
            1
    
    