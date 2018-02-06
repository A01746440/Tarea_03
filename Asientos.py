#David Arnaiz Gaona
#Calcular el total en la compra de boletos

def calcularPago (asientosA, asientosB,asientosC):
    # Calcula el costo de cada asiento comprado dependiendo su clase y devuelve el total
    claseA = 870 * asientosA
    claseB = 650 * asientosB
    claseC = 235 * asientosC
    totalPago = claseA + claseB + claseC
    return totalPago


def main ():
    nBoletosA =int(input("Boletos a comprar en clase A: "))
    nBoletosB =int(input("Boletos  a comprar en clase B: "))
    nBoletosC =int(input("Boletos a comprar en clase C: "))
    totalPago = calcularPago(nBoletosA, nBoletosB, nBoletosC)
    print("El costo total a pagar es de: $%.2f "% totalPago)




main()