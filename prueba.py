

nombre = input("Introduce tu nombre: ")
print("Bienvenido {}".format(nombre))
edad = int(input("Introduzca su edad: "))

if edad > 0:
    if edad > 18:
        print("Eres mayor de edad")
    else:
        print("Te faltan {} años para ser mayor de edad...".format(18-edad))
else:
    print("Edad invalida... ")