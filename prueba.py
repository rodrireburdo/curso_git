from time import sleep

nombre = input("Introduce tu nombre: ")
print("Bienvenido {}".format(nombre))
edad = int(input("Introduzca su edad: "))

sleep(1)

if edad > 0:
    if edad > 18:
        print("Eres mayor de edad")
    else:
        print("Te faltan {} años para ser mayor de edad...".format(18-edad))
else:
    print("Edad invalida... ")

documento = int(input("Ingrese su numero de documento: "))
if len(documento) == 8:
    print("Su incripcion a terminado")
else:
    print("Error en el numero de documeno") 