#no podemos cambiar elementos pero si podemos añadir o elimnar elementos nuevos en el set
# set es una coleccion sin orden, no titne indices y elementos repetidos

planetas = {"tierra", "marte", "mercurio", "jupiter"}
print(planetas)

#largo
print(len(planetas))
#revisar si un elemetno esta presente
print("marte" in planetas)

#agregar
planetas.add("venus")
print(planetas)

#eliminar con remove
planetas.remove("venus")
print(planetas)

#eliminar con discard

planetas.discard("jupiters")
print(planetas)

#limpiar el set
planetas.clear()
print(planetas)

#elinar el set
del planetas
print(planetas)
