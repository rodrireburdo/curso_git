from time import sleep

def main ():
    print("Nos alegra que crees una cuenta con nosotros\n")
    nombre = input("Introduce tu nombre: ")
    print("Bienvenido {}".format(nombre))
    edad = int(input("Introduzca su edad: "))

    sleep(1)

    if edad > 0:
        if edad >= 18:
            print("Eres mayor de edad")
        else:
            print("Te faltan {} años para ser mayor de edad...".format(18-edad))
    else:
        print("Edad invalida... ")

    documento = int(input("Ingrese su numero de documento: "))

    print("DNI: {}".format(documento))

__name__ == "__ main __ "
main () 

