
""""Seguimiento de Ingresos y Gastos
Descripción del problema: Debes crear un programa para realizar un seguimiento de tus gastos
mensuales y categorizarlos. El programa debe permitir al usuario ingresar su salario mensual y luego
registrar los gastos adicionales que ha realizado durante el mes. Los gastos se deben categorizar en
diferentes categorías, como "alimentos", "transporte", "vivienda" y "entretenimiento". El programa
calculará el saldo restante después de restar los gastos al salario mensual y mostrará el total de
gastos en cada categoría, así como el saldo restante. 
"""""
def principal():
    diccionario={}
    totalingreso=int(input("ingrese su sueldo mensual"))
    datos(diccionario)
    while True:
        menu_principal()
        opcion=int(input("ingrese una opcion"))
        if opcion==1:
            gastos_adicionales(diccionario)
        elif opcion==2:
                total_gastos(diccionario,totalingreso)
        elif opcion==3:
            total_gastos_por_categoria(diccionario)
        elif opcion==4:
            print("hasta luego, gracias por usar el programa")
            break
        else:
            print("opcion invalida ingrese una opcion valida ")
def menu_principal():
    print("seleccione una opcion")
    print("1 ingresar gastos adicionales") 
    print("2 Calcular el saldo restante,mostrar el total de gastos")
    print("3 mostrar gastos por categoria")
    print("4 salir de el programa.")
def datos(diccionario):
    diccionario["alimentos"]=int(input("ingrese su gastos en alimentos: "))
    diccionario["transporte"]=int(input("ingrese su gastos en transporte: "))
    diccionario["vivienda"]=int(input("ingrese su gastos en vivienda: "))
    diccionario["entretenimiento"]=int(input("ingrese su gastos en entretenimiento: "))
def gastos_adicionales(diccionario):
   while True:
    print("seleccione una opcion")
    print("1 ingresar gastos adicionales") 
    print("0 volver al menu principal") 
    option=int(input("ingrese una opcion: "))
    if option==1:
        monto=int(input("ingrese el monto de el gasto: "))
        categoria=input("ingrese la categoria: ")
        for cate,valor in diccionario.items():
            if cate== categoria:
                diccionario[cate]=valor+monto
                print("gasto sumado con exito en la categoria ")
                break
        else:
            print("no se puede agregar el gasto verifique la caregoria")
    elif(option==0):
        print("retornas al menu principal")
        break
    else:
        print("ingrese una opcion valida") 
def total_gastos(diccionario,ingreso_total):
    cont=0
    total=0
    cont=sum(diccionario.values())
    print("el total de gastos es: ",cont)
    total=ingreso_total-cont
    if total<0:
        print( "Estás gastando más de lo que ganas: ",total)
    else:print("tu saldo restante es: ",total)
def total_gastos_por_categoria(diccionario):
    lista=[]
    print("tus gastos son: ")
    for encontrar in diccionario.items:
        lista=[encontrar]
        print(lista)        
principal()




























