def main():
    nombre,apellido,documento=dato()
    diccionariofact={}
    dato()
    while True:
        menu()
        opcion=int(input("ingrese una opcions"))
        if opcion==1:
            dato()
        elif opcion==2:
            regprod(diccionariofact)
        elif opcion==3:
            listaprod(diccionariofact)
        elif opcion==4:
            mostrarfact(diccionariofact,nombre,apellido,documento)
    



def menu():
    print("(1) Volver a registrar el documento, nombres y apellidos del cliente")
    print("(2) Registrar un nuevo producto a la factura (nombre producto, valor producto)")
    print("(3) Listar productos actuales de la factura.")
    print("(4) Mostrar factura")
    print("(5) Apagar el programa" )
    
    

def dato():
    nombre=input("ingrese su nombre: ")
    apellido=input("ingrese su apellido: ")
    documento=int(input("ingrese numero de documento: "))
    return nombre,apellido,documento

def regprod(dic):
    nombreprod=input("ingrese el nombre de el producto a registrar")
    valorprod=int(input("ingrese el valor de el producto nuevo "))
    dic[nombreprod]=valorprod

def listaprod(dic1):
    for productos in dic1.keys():
        print(productos)
    
def mostrarfact(dic2,nombre,ape,docu):
    print(nombre)
    print(ape)
    print(docu)
    for productos,valores in dic2.items():
        print(f"los productos son",{productos},"y los valores son: ",{valores})
    total=0
    print("el total de la compra es: ", sum(dic2.values()))





















main()