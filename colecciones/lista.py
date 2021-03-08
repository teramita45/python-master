nombres = ["juan", "carla", "ricardo", "maria"]

print(nombres)
print(len(nombres))

print(nombres[0])
print(nombres[1])

#navegacion inversa
print(nombres[-4])

#imprimir rango

print(nombres[0:2]) #sin incluir el indice 2

#imprimir los elementos hasta el indice 

print(nombres[:3]) 

#imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[2])

#cambiar los elementops de la la lista
nombres[3] ="ivone"

print(nombres)
#iterar lista
for i in nombres:
    print(i)
#revisar sii existe un elemetno en una lista

if "Karla" in nombres:
    print("carla si existe en la lista")
else :
    print("el elemento buscado no existe en la lsita")
    
#agregar elementos
nombres.append("lorenzo")

print(nombres)

#insertar un nuevo elemtno en el indice proporcionado
nombres.insert(1,"octavio")
print(nombres)
#remover un elemtno de la lista

nombres.remove("octavio")
print(nombres)

#remover el ultimo elemento de la lista
nombres.pop()
print(nombres)

#remover el indice indicado
del nombres[0]
print(nombres)

#limpiar elemento de nuestra lista
nombres.clear()
print(nombres)

#eliminar por completo la lista elimina la variable
del nombres


#tarea
numeros = [0,1,2,3,4,5,6,7,8,9,10]

for i in numeros:
    if i%3 ==0:
        print(i)    
    