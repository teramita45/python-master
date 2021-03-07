a = int(input("proporciona un valor : "))
valorMin = 0
valorMax = 5

dentroRango = a >= valorMin and a <= valorMax

print (dentroRango)

if (dentroRango):
    print("dentro de rango")
else:
     print("fuerda de rango")
    
alto = int(input("proporciona un alto: "))
ancho= int(input("proporciona un ancho: "))

print("area: ", alto*ancho)
print("perimetro: ", (alto+ancho)*2)

numero1 = int(input("Proporciona el primer numero: "))
numero2 = int(input("Proporciona el segundo numero: "))

if(numero1 > numero2):
    print("el mayor numero es: ", numero1)
else:
    print("el mayor numero es: ", numero2)
