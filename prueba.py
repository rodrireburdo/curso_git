from time import sleep
SALUDO = "NOS ALEGRA QUE CREES UNA CUENTA CON NOSOTROS"
def main ():
    print("\n" + SALUDO + "\n" + "-" * len(SALUDO))
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

    print("Fin del programa")
    sleep(1)


__name__ == "__ main __ "
main () 

