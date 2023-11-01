from math import *

class Calculadora:
    def main(self):
        while True:
            opt = self.getChoise()
            if opt == "0": break
            self.makeOperation(opt)

        return
    
    def getChoise(self):
        print("Elija la operacion que desea realizar.\n")
        print("1. Sumar.")
        print("2. Restar.") 
        print("3. Multiplicar.")
        print("4. Dividir.")
        print("5. Raiz.\n")
        print("0. Salir.")

        return input("Opción: ")
    
    def makeOperation(self, opt):
        n1 = n2 = 0
        n1 = input("Escriba el primer numero: ")
        if int(opt) <= 4: n2 = input("Escriba el segundo numero: ")
        

        operations = {
            "1": lambda n1, n2: "La suma es: " + str(int(n1) + int(n2)),
            "2": lambda n1, n2: "La resta es: " + str(int(n1) - int(n2)),
            "3": lambda n1, n2: "La multiplicación es: " + str(int(n1) * int(n2)),
            "4": lambda n1, n2: "La división es: " + str(int(n1) / int(n2)),
            "5": lambda n1, n2: "la raiz cuadrada es: " + str(sqrt(int(n1))),
            "default": lambda : "La opción seleccionada no existe",
        }

        return print(operations[opt](n1, n2) if opt in operations else operations["default"]())