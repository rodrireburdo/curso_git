SALIR = "Q" 
titulo = "Bienbenido al programa lista de compra"
print ("\n" + titulo + "\n" + "-" * len(titulo) + "\n")


def main ():
    lista_compra = []
    input_usuario = input("que decea comprar: ")
    
    while input_usuario != "Q":
        if input_usuario in lista_compra:
            print("El item ya se encuentra en la lista")
        else:
            lista_compra.append(input_usuario)
            print(lista_compra)
        input_usuario = input("que decea comprar: ")
    
    print("La lista final de compras es :\n {} ".format(lista_compra))
__name__ == "__ main __ "
main ()


