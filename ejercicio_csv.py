from funciones_ejercicio_csv import *
while True:
    print("MENÚ")
    print("1. Agregar contacto")
    print("2. Mostrar contactos")
    print("3. Guardar contacto en un archivo CSV")
    print("4. Salir")
    while True:
        try:
            opc=int(input("Ingrese el número del menú: "))
            if opc in (1,2,3,4):
                break
            else:
                print("Error! Debe ingresar un número del menú!")
                time.sleep(2)
        except:
            print("Error! Debe ingresar un número entero!")
            time.sleep(2)
    if opc==1:
        opc1()
    elif opc==2:
        opc2()
    elif opc==3:
        opc3()
    else:    
        opc4()