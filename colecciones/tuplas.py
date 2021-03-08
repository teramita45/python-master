#las tuplan mantienen el orden pero no es posible modificarla
frutas = ("naranja", "platano", "guayaba"  )

print(frutas)

#largo de la tupla
print(len(frutas))

#accder a un elemento
print(frutas[2])

#navegacion inversa
print(frutas[-2])

#rango
print(frutas[0:2])

#modificar un valo
#frutas[0] = "naranjita"

frutasLista = list(frutas)
frutasLista[0] = "naranjita"

frutas = tuple(frutasLista)

print(frutas)

for fruta in frutas:
    print(fruta, end=", ")
#no podemos agregar ni eleiminar elementos de una tupla...
# pero si podemos eliminar latupla

tupla = (13, 1, 8, 3, 2, 5, 8)
numeros = []

for i in tupla:
    if i<5:
        numeros.append(i)

tupla = tuple(numeros)
