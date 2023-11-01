# En un sistema de automatización industrial, un motor puede estar encendido o apagado. Si la temperatura de la máquina supera los 80 grados, el motor debe apagarse automáticamente. Escribir un programa que controle el estado del motor y lo apague si la temperatura supera los 80 grados.

import random
temperatura = int(input("ingrese el numero "))


def obtener_temperatura():
    numero = 79 + random.random()
    return numero


def motor(temperatura):
    
    if temperatura >= 80:
        print("la temperatura es muy alta, el motor se apagara")
        encendido = False
    else:
        print("el motor tiene la temperatura adecuada el motor seguira ensendido")
        encendido =True
    return encendido
    
    
while True:
    numero = obtener_temperatura()
    encendido = motor(temperatura)
    
    break
    
   
