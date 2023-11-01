# Ejercicio 2
# Un programa de descarga de archivos multimedia tiene diferentes velocidades
# de descarga según la calidad de la conexión a internet del usuario. 
# Si la conexión es mayor a 20 Mbps, la velocidad de descarga será de 10 Mbps,
# si la conexión es menor a 20 Mbps pero mayor a 5 Mbps, 
# la velocidad será de 5 Mbps y si la conexión es menor a 5 Mbps, la velocidad de descarga será de 1 Mbps.
# Escribir un programa que calcule el tiempo de descarga de un archivo
# y el ancho de banda utilizado, según la velocidad de descarga.

def tiempo_de_descarga(tamaño_archivo, velocidad_conexion):
    if velocidad_conexion > 20:
        velocidad_descarga = 10
    elif velocidad_conexion > 5:
        velocidad_descarga = 5
    else:
        velocidad_descarga = 1
        
    tiempo_de_descarga = (tamaño_archivo * 8 * 1024 * 1024) / (velocidad_descarga * 1000000)
    banda_ancha = velocidad_descarga
    
    return tiempo_de_descarga, banda_ancha

tamaño_archivo = float(input("ingrese tamaño_archivo del archivo en MB: "))
velocidad_conexion = float(input("Ingrese la velocidad de internet en Mbps: "))

tiempo_de_descarga, banda_ancha = tiempo_de_descarga(tamaño_archivo,velocidad_conexion)

print ("El tiempo de descarga del archivo es: ", tiempo_de_descarga, "Segundos")
print ("Su ancho de banda utilizado es:", banda_ancha, "Mbps")
