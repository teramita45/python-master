mes = int(input("proporciona un mes en numero: "))

estacion = None
if mes == 1 or mes == 2 or mes == 3 :
    estacion = "inverno"
elif mes == 5 or mes == 6 or mes == 4:
    estacion = "otoño"
elif mes == 7 or mes == 8 or mes ==9:
    estacion = "verano"
elif mes == 10 or mes == 11 or mes == 12:
    estacion = "primavera"
else:
    estacion= "no corresponde a ningun mes del año"





print("estacion " ,estacion, " para el mes " , mes)


nota = int(input("proporciona un valor entre 0 y 10: "))

calificacion = None

if nota == 9 or nota == 10 :
    calificacion = "A"
elif nota == 8 :
    calificacion = "B"
elif nota == 7:
    calificacion = "C"
elif nota == 6:
    calificacion = "C"
elif nota <=5 and nota >=0 :
    calificacion = "F"
else:
    calificacion = True

if calificacion == True :
    print("valor incorrecto")
else:
    print(calificacion)