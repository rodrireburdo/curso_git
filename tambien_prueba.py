SALIR = "Q" 
titulo = "Bienbenido al programa lista de compra"
print ("\n" + titulo + "\n" + "-" * len(titulo) + "\n")


def main ():
    lista_compra = []
    input_usuario = input("que decea comprar: ")
    
    while input_usuario != "Q":
        lista_compra.append(input_usuario)
        print(lista_compra)
        input_usuario = input("que decea comprar: ")

__name__ == "__ main __ "
main ()


