#un diccionario esta compuesto de los elementos clave valor
diccionario = {
    "ide": "integrated Development Environment",
    "OOP": "onject Oriented Programing",
    "DBMS": "data base management system"
}
print(diccionario)

#largo de un diccionario
print(len(diccionario))

#acceder
print(diccionario["ide"])

#acceder con get
print(diccionario.get("ide"))

#modificando valores

diccionario["ide"] = "IDEEEEEEEEE"
print(diccionario)

#iterar
for i in diccionario:
    print(diccionario[i])

for i in diccionario.values():
    print(i)

#comprobando si existe un elemtno

print("ide" in diccionario)

#agregar elementos
diccionario["PK"] = "Primary Key"
print(diccionario)

#remover elemtnos
diccionario.pop("DBMS")
print(diccionario)

#limpiar con clear
diccionario.clear()

#elminiar
del diccionario