# Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina
#si una persona tiene anemia o no, lo cual depende de su nivel de hemoglobina en la sangre, de su edad y de su sexo.

# Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina
#su resultado como positivo y en caso contrario como negativo.

# La tabla en la que el medico se basa para obtener el resultado es la siguiente:
# EDADES                          NIVEL HOMOGLOBINA 
# 3 -1                            13 - 26g%
# >1 Y <=6 meses                  10 -18g%
# > 6 Y <= 12 meses               11 -15g%
# >1 y <= 5 años  10 -            11.5 -15g%
# >5 años y <= 10 años            12.6 -15.5g%
# >10 y <= 15 años                13 -15.5g%
# Mujeres > 15 años               12 -16g%
# Hombres > 15 Años               14 -18g%


def verificar_anemia(hemo, rango_min, rango_max):
    if hemo >= rango_min and hemo <= rango_max:
        return "El paciente está saludable con un valor negativo"
    else:
        return "El paciente no está saludable"

edad = int(input("Ingrese su edad: "))
val = input("¿La edad en meses? (s/n)").lower()
sexo = input("Ingrese su sexo (m/f): ").lower()

if val == "s":
    if edad >= 0 and edad < 1:
        hemo = int(input("Ingrese el valor numérico para hemoglobina en gr %: "))
        resultado = verificar_anemia(hemo, 13, 26)
    else:
        print("La edad máxima es 12 meses para la opción elegida")
else:
    if edad >= 1:
        hemo = int(input("Ingrese el valor numérico para hemoglobina en gr %: "))
        if sexo == "m":
            if edad > 15:
                resultado = verificar_anemia(hemo, 14, 18)
            else:
                resultado = verificar_anemia(hemo, 12, 16)
        elif sexo == "f":
            resultado = verificar_anemia(hemo, 12, 16)
        else:
            resultado = "Sexo no válido"
    else:
        resultado = "Edad no válida"

print(resultado)
