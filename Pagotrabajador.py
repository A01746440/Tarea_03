#David Arnaiz Gaona
#Calcula el salario

def calcularPagoNormal (horasNormales,costoHora):
    #Calcula el pago por horaario normal de trabajo
    pagoNormal = horasNormales * costoHora
    return pagoNormal

def calcularPagoExtra (HorasExtra, costoHora):
    #Calcula el 75% por hora extra y el pago por el total de horas extras trabajadas.
    porcentaje = costoHora * 0.75
    costoExtra = costoHora + porcentaje
    pagoExtra = HorasExtra * costoExtra
    return pagoExtra

def main ():
    hNormales = int(input("teclea las horas normales trabajadas: "))
    hExtras = int(input("teclea las horas extras trabajadas: "))
    costoHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal (hNormales,costoHora)
    pagoExtra = calcularPagoExtra (hExtras,costoHora)
    pagoTotal = pagoNormal + pagoExtra
    print("Pago Normal: $%.2f"% pagoNormal)
    print("Horas Extras: $%.2f"% pagoExtra)
    print("-------------------------------")
    print("pago total: $%.2f"% pagoTotal)

main()