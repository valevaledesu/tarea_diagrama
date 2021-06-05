dolar_hoy = 19.96

dolares = float(input("Cuántos dólares quiere convertir?\n"))

if(dolares >= 1  and dolares <=1000):
    pesos = dolares * dolar_hoy
    print(pesos)
else:
    print("transacción inválida")