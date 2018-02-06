#David Arnaiz Gaona
#Calcula el rendimiento de un auto

def calcularRendimiento (kilometros, gasolina):
    #Calcula el rendimiento en km/l
    division = kilometros / gasolina
    return division

def conversionMillas(kilometros, gasolina):
    # pasa todas las unidades al sistema inglés y da calcula el rendimiento.
    convertirMillas = kilometros * 1.6093
    convertirGalon = gasolina * 0.264
    rendimiento = convertirMillas / convertirGalon
    return rendimiento

def calcularGasolina (Kmrecorrer,Kilometros, gasolina):
    #Calcula  los litros que se necesitarán para recorrrer determinado numero de kilometros
    litros = (Kmrecorrer * gasolina)/ Kilometros
    return litros



def main():
    Km = int(input("Cuantos kilometros recorres: "))
    Gasolina = int(input("Cuantos litros de gasolina utilizaste: "))
    rendimiento = calcularRendimiento (Km, Gasolina)
    millas = conversionMillas(Km,Gasolina)

    print("Si recorres", Km," kms con ",Gasolina," litros de gasolina, recorreras: ")
    print("%.2f"%rendimiento," km/l")
    print("%.2f"%millas," mi/gal")

    kmRecorrer = int(input("¿Cuantos Kilometros vas a recorrer? "))
    recorrido = calcularGasolina(kmRecorrer, Km, Gasolina)
    print("Para recorrer",kmRecorrer,"se necesitan %.2f"%recorrido," L de gasolina")

main()