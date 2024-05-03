def main():
    print("bienvenido a gestion de inventario")
    nombre_precio={}
    nombre_cantidad={}
    while True:
        menu()
        option=int(input("ingrese una opcion"))
        if(option==1):
            nuevo_productovalor(nombre_precio,nombre_cantidad)
            
        elif(option==2):
            actualizar_cantidad(nombre_cantidad)
            
        elif(option==3):
            eliminar_producto(nombre_precio,nombre_cantidad)
        elif(option==4):
            listar_productos(nombre_precio)
        elif(option==5):
            verificar_siesta_producto(nombre_precio)
        elif(option==6):
            break
        else: 
            print("opcion invalida, seleccione una opcion ")
       
              
def menu():
    print("1: Agregar un nuevo producto al inventario.")
    print("2: Actualizar la cantidad de un producto existente en el inventario.")
    print("3:Eliminar un producto del inventario.")
    print("4: Listar todos los productos en el inventario.")
    print("5: Verificar si un producto específico está en el inventario.")
    print("6: salir de el programa")
        
def nuevo_productovalor(diccionario1,diccionario2):#nos va a servir para ingresar un nuevo producto al inventario y su valor
    producto=input("ingrese un nuevo producto: ")
    valor=int(input("ingrese el precio del producto: "))
    valor1=int(input("ingrese la cantidad del producto: "))
    diccionario1[producto]=valor
    diccionario2[producto]=valor1
def actualizar_cantidad(diccionario2):#vamos a actualizar la cantidad de productos que tenemos 
    for producto, cantidad in diccionario2.items():
        print(producto,cantidad)
    productoactualizar=input("ingrese el producto que desea modificar")
    cantidadnueva=int(input("ingrese la nueva acantidad de el producto"))
    diccionario2[productoactualizar]=cantidadnueva

    
def eliminar_producto(diccionario1,diccionario2):# mediante la funcion .pop() en el parametro ingresamos la llave a eliminar
    print("los productos que hay son:")
    for productos, precio in diccionario1.items():
            pass
    for productos, cantidad in diccionario2.items():
        print(f"producto:",productos,"precio:",precio,"cantidad",cantidad)
    diccionario2.pop(input("ingrese el producto a eliminar:"))
    diccionario1.pop(input("confirme nuevamente el producto a eliminar"))
def listar_productos (diccionario1):# nos va a imprimir la lista solo de los productos , se cra una lista y adentro de esta se almacenan solo los productos
    print("en el inventario estan los siguientes productos")
    lista1=[]
    for lista in diccionario1.keys():
        lista1=lista
        print(lista1)

def verificar_siesta_producto(diccionario1):#buscaremos un producto por su lllave en el diccionario
        esta=input("ingrese el producto que esta buscando")
        for claves in diccionario1.keys():
            if esta == claves:
                print("el producto", esta, "si esta en el inventario")
            else:
                print("el producto no esta en el inventario")
            
        
main()



