# Una universidad ofrece un descuento a los estudiantes que depende del
#estrato y la edad. Si el estrato es 1 y su edad es menor a 18 el descuento
#será del 20% sobre el valor de la matrícula. Si el estrato es 1 y el alumno
#tiene 18 o mas años, el descuento será del 15%. Si el estrato es 2 y la edad
#es menor a 18 años, el descuento será del 10% y si el estrato es 2 y la edad
#es 18 años o mas, el descuento será del 5%.
# Escribir el precio que deberá pagar un estudiante por su matrícula y el
#valor del descuento.



edad = int(input("Ingrese su edad en números: "))
estrato = int(input("Ingrese su estrato: "))
precio = int(input("Ingrese el precio del semestre: "))
descuento = 0

if estrato == 1:
    if edad < 18:
        descuento = precio * 20 / 100
    else:
        descuento = precio * 15 / 100
elif estrato == 2:
    if edad < 18:
        descuento = precio * 10 / 100
    else:
        descuento = precio * 5 / 100

precio_final = precio - descuento

if descuento > 0:
    print("Su edad es", edad, "y su estrato es", estrato)
    print("Tiene un descuento de", descuento, "y deberá pagar", precio_final)
else:
    print("Lo sentimos, no califica para ningún descuento. Deberá pagar el precio completo de", precio)
