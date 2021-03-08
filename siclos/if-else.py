condicion = True
if condicion:
    print("la condicion es verdadera")
else:
    print("la condicion es falsa")

#operador ternario    
print("condicion es verdadera") if condicion  else print("condicion es falsa")

numero =  int(input("proporciona un numero entre 1 y 3: "))

#if elseif else
if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "Numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "no se encuentra en el rango"

print(numeroTexto)

