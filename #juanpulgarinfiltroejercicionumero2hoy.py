
def principal():# esta funcion nos contiene los datos de todas la demas asi se realiza de forma mas eficiente
  numerodearticulos=int(input("ingrese el numero de articulos comprados"))
  articulos={}
  while True:
    print("opcion 1: ingrese los articulos que compro")
    print("opcion 2: mostrar factura")
    print("opcion 3: salir de el programa")
    opcion=int(input("ingrese una opcion"))
    if opcion==1:
      entrada_de_datos(articulos)
    elif opcion==2:
      condiciones(numerodearticulos,articulos)
def entrada_de_datos(articulos):#podemos llamar esta funcion en cualquier momento para ingresar datos
  valor_de_articulo=int(input("ingrese el valor unitario de los articulo: "))
  articulo_que_compro=input("ingrese el nombre de los articulos comprado")
  articulos[articulo_que_compro]=valor_de_articulo
  return articulos
def condiciones(numeroarticulos,articulos):# esta funcion nos resume el funcionamiento de todo el programa
  print("el numero de articulos es",numeroarticulos)
  if numeroarticulos<5:
    print("usted no tine ningun descuento")
    print("el total es:",sum(articulos.values()))
  elif numeroarticulos>20:
    print("usted tiene un descuento de el 15%")
    print("el total con el descuento es",(sum(articulos.values()))*0.85)
  elif numeroarticulos in range(5, 10):
    print("usted tiene un buen descuento de el 5%")
    print("el total con el descuento es",(sum(articulos.values()))*0.95)
  elif numeroarticulos in range(11,20):
    print("usted tiene un buen descuento de el 10%")
    print("el total con el descuento es",(sum(articulos.values()))*0.90)
    
  
    
    
  
    
    
  

  
    
  
  
  
  
  
  
  
principal()



