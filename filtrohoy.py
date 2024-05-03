def principal():
  producto_cantidad={}
  producto_nota={}

  while True:
    menu()
    opcion=int(input("ingrese una opcion"))
    if opcion ==1:
      agregarnuevoproducto(producto_cantidad,producto_nota)
    elif opcion==2:
      modificarproducto(producto_cantidad,producto_nota)
    elif opcion==3:
      eliminarproducto(producto_cantidad,producto_nota)
    elif opcion==4:
      listadeproductos(producto_cantidad,producto_nota)
    elif opcion==5:
      buscarproductos(producto_cantidad)
      
    
  
def menu():# solo imprime las opciones se puso dentro de una funcion para poderla ocultar 
  print("(1): Agregar Producto")
  print("(2): Modificar Producto") 
  print("(3):Eliminar Producto)")
  print("(4):Listar Productos") 
  print("(5):Buscar Productos ")


def agregarnuevoproducto(dic1,dic2):#esta funcion nos agrega un nuevo producto a los diccionarios
    producto=str(input("ingrese el nombre de el producto"))
    cantidad=int(input("ingrese la cantidad requerida"))
    nota=input("ingrese una nota adicional de el producto")
    dic1[producto]=cantidad
    dic2[producto]=nota
    return dic1,dic2
  
def modificarproducto(dic1,dic2): #nos permite modificar el producto de una manera muy dinamica ya que dentro de la funcion hay otro menu 
  productoabuscar=str(input("ingrese el nombre de el producto que va a buscar "))
  
  
  for buscar1,buscar2 in dic1.items():
    if buscar1==productoabuscar:
      print("si esta en la lista ")
      opcion=int(input("ingrese una opcion 1 para cambiar la nota 2 para cambiar la cantidad"))
      if opcion==1:
        modificarnota=input("ingrese la nota nueva que desea sobre el producto ")
        dic2[productoabuscar]=modificarnota
        print("nota cambiada correctamente")
      elif opcion==2:
        modificarcantida=input("ingrese la cantidad que desea modificar ")
        dic1[productoabuscar]=modificarcantida
    else:print("el producto que busca no se encuentra en su lista")
        

def eliminarproducto(dic1,dic2):# es una forma muy segura de eliminar un producto ya que para eliminarlo se pide una doble validacion 
    productoabuscar=str(input("ingrese el nombre de el producto que va a eliminar "))
    for buscar1,buscar2 in dic1.items():
      pass
    if buscar1==productoabuscar:
      dic1.pop(input("ingrese el producto a eliminar"))
      dic2.pop(input("confirme nuevamente el producto a eliminar"))
      print("productoeliminado")
    else:print("el producto no esta en su lista no se pude eliminar")
  
def listadeproductos(dic1,dic2):#nos muestra los productos que hay 
  lista=[]
  for clave,valor in dic1.items():
    pass
  for valor2 in dic2.values():
    lista=[("el producto es: "),clave,("la cantidad es: "),valor,("la nota que tienes sobre el producto es: "),valor2]
    print(lista)
    
    
def buscarproductos(dic1):#nos indica si un producto en especifico se encuentra en el diccionario
  productoabuscar=str(input("ingrese el nombre de el producto que va a buscar "))
  for buscar1,buscar2 in dic1.items():
    if buscar1==productoabuscar:
      print("el producto buscado si esta en la lista:",buscar1)
    else: print("el producto buscado no esta en la lista")
    
    
principal()