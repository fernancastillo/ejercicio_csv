import csv
import os
import time
contactos=[["Nombre","Telefono","Correo"]]

def opc1():
    os.system("cls")
    print("\tAGREGAR CONTACTO")
    while True:
        nombre=input("Ingrese el nombre: ")
        if len(nombre)<3:
            print("Error! El nombre debe tener más de 3 caracteres!")
            time.sleep(2)
        else:
            break     
    while True:
        try:   
            telefono=int(input("Ingrese el número de teléfono: "))
            break
        except:
            print("Error! Debe ingresar números enteros")
            time.sleep(2)
    while True:
        correo=input("Ingrese correo electrónico: ")
        if len(correo)<3:
            print("Error! El correo debe tener más de 3 caracteres!")
            time.sleep(2)
        else:
            break
    contacto=[nombre, telefono, correo]
    contactos.append(contacto)
    print("Contacto agregado con éxito!")

def opc2():
    print("\tMOSTRAR CONTACTOS")
    for x in range(len(contactos)):
        print(f"{x+1}. Nombre: {contactos[x]["nombre"]}. Teléfono: {contactos[x]["telefono"]}. Correo: {contactos[x]["correo"]}.\n")
        time.sleep(3)

def opc3():
    print("\tGUARDAR CONTACTO EN UN ARCHIVO CSV")
    nombre_archivo=input("Ingrese el nombre que tendrá el archivo CSV: ")
    with open (f"{nombre_archivo}.csv", "w", newline="") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerows(contactos)
        print("Archivo guardado con éxito!")
        time.sleep(2)

def opc4():
    print("Hasta la próxima!")
    exit()