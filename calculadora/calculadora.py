o =True    
while o == True:
    print("¿Qué operación desea realizar?")
    print("[1] Sumar")
    print("[2] Restar")
    print("[3] Multiplicar")
    print("[4] Dividir")
    print("[5] Salir")
    
    operacion = int(input())
    
    if operacion == 5:
        print("¡Adiós!")
        break
    elif operacion > 5 or operacion < 1:
        print("esta operacion no es valida ")
        continue
    num1 = int(input("Escribe el primer número: "))
    num2 = int(input("Escribe el segundo número: "))
    
    if operacion == 4 and num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 + num2 if operacion == 1 else num1 - num2 if operacion == 2 else num1 * num2 if operacion == 3 else num1 / num2
        print(f"El resultado es: {resultado}")
        respuesta = input("¿Desea realizar otra operación? (y [si] / n [no]):").lower()
    if respuesta != "y":
        o = False



# from math import *
# o = True; 
# while o == True:
#     print("que operacion desea realizards")
#     print(" ")
#     print("[1] sumar")
#     print("[2] restar")
#     print("[3] multiplicar")
#     print("[4] division")
#     print("[5] Salir")
#     operacion = int(input())

#     if operacion == 1:
#         num1 = int(input("Escribe el primer numero: "))
#         num2 = int(input("Escribe el segundo numero: "))
#         print("El resultado de la suma es:", num1 + num2)
#     elif operacion == 2:
#             num1 = int(input("Escribe el primer numero: "))
#             num2 = int(input("Escribe el segundo numero: "))
#             print("El resultado de la resta es:", num1 - num2)
#     elif operacion == 3:
#             num1 = int(input("Escribe el primer numero: "))
#             num2 = int(input("Escribe el segundo numero: "))
#             print("El resultado de la multiplicacion:", num1 * num2)
#     elif operacion == 4:
#             num1 = int(input("Escribe el primer numero: "))
#             num2 = int(input("Escribe el segundo numero: "))
#             print("El resultado de la division", num1 / num2)
#     else: 
#         print("Saliste, care monda")
#         o = False

# while True:
#     print("¿Qué operación desea realizar?")
#     print("[1] Sumar")
#     print("[2] Restar")
#     print("[3] Multiplicar")
#     print("[4] Dividir")
#     print("[5] Salir")

#     operacion = input()

#     if operacion == '5':
#         print("¡Adiós!")
#         break

#     if operacion not in ('1', '2', '3', '4'):
#         print("Número de operación no válido.")
#         continue

#     num1 = float(input("Escribe el primer número: "))
#     num2 = float(input("Escribe el segundo número: "))

#     if operacion == '4' and num2 == 0:
#         print("Error: No se puede dividir por cero.")
#     else:
#         resultado = (num1 + num2, num1 - num2, num1 * num2, num1 / num2)[int(operacion) - 1]
#         print(f"El resultado es: {resultado}")
