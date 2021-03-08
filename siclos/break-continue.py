#imprimir solo las letras a contenidas en una cadena

for letra in "holanda":
    if letra == "a":
        print (letra)
        break
else:
    print("fin siclo for")

print("continua el programa")

#imprimir numeros pares

# for i in range(6):
#     if i%2 == 0:
#         print(i)

#si el numero es diferente de par

for i in range(6):
    if i%2 != 0:
        continue
    print(i)