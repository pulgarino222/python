def main():
  productos = {}

  print("BIENVENIDO A GESTIÓN DE INVENTARIO")
  while True:

    print("""¿Qué quieres hacer?
          1. Agregar un nuevo producto al inventario.
          2. Actualizar la cantidad de un producto existente en el inventario.
          3. Eliminar un producto del inventario.
          4. Listar todos los productos en el inventario.
          5. Verificar si un producto especifico está en el inventario.
          6. Cerrar el programa.
          """)
    opcion = int(input("Ingresa una opción"))

    if opcion == 1:
      productos=diccionario_productos()

    elif opcion == 2:
      list(productos.values()).index(int(input("Ingrese el valor del producto a actualizar")))
    elif opcion == 3:
      for i in (productos.keys)[input("ingrese poducto a eliminar")]:
        del productos[i]
    elif opcion == 4:
      pass
         
      
      

    elif opcion ==5:
      #verificar o buscar producto.
        pass
    elif opcion == 6:
        print("¡Hasta luego,que tengas un lindo día!")
        exit()
    else:
      print("Por favor elige una opcion valida")




def diccionario_productos():
    clavepro=input("agregue un nuevo producto:")
    cantpro=int(input("agregue valor de el producto: "))
    diccionario_productos[clavepro]=cantpro



   



  
    

main()