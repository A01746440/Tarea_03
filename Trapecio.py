#David Arnaiz Gaona
#Calcular area y perimetro de un trapecio
import math     #llamar libreria math

def calcularArea (bMayor, bMenor,altura):
    #Calcula el Area del trapecio
    Area = ((bMayor + bMenor) /2) * altura
    return Area

def calcularPerimetro (bMayor, bMenor, altura):
    #Calcula la logitud de los lados oblicuos y despues calcula el perimetro
    diferenciaBases = (bMayor - bMenor)/2
    pitagoras = math.sqrt((diferenciaBases)**2 + (altura)**2)
    perimetro = bMayor + bMenor + (pitagoras * 2)
    return perimetro


def main ():
    bMayor = int(input("Escriba la longitud de la base mayor: "))
    bMenor = int(input("Escriba la longitud de la base menor: "))
    altura = int(input("Escriba la altura del trapecio: "))
    area = calcularArea (bMayor, bMenor, altura)
    perimetro = calcularPerimetro (bMayor, bMenor, altura)
    print("Area: %.2f"% area)
    print("Perimetro: %.2f"% perimetro)


main()