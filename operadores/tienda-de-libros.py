print("proporcione los siguientes datos del libro")

nombre = input("proporciona el nombre: ")
id = int(input("proporciona el id: "))
precio = float(input("proporciona el precio : "))
envio = input("indica si el envio es gratuito(Treu / False): ")

if envio =="True" or envio == "true":
    envio = True
elif envio == "False" or envio == "false":
    envio = False
else:
    envio = "valor incorrecto debe ser True/False"

print("nombre : " +nombre)
print("id: ", id)
print("precio: ",precio )
print("envio gratuito: ", envio )

