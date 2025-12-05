def ejercio1 ():
   plata=1000
   while 0 == 0:
      print("seleccione que accion quiere realizar")
      print("1. Depositar dinero")
      print("2. Retirar dinero")
      print("3. Salir")
      menu = int(input(""))
      if menu==1:
        try:
             deposito = float(input("¿Cuanto dinero quiere depositar?"))
             plata= plata + deposito
             print("Este es su saldo total", plata) 
        except ValueError:
           print("No se pueden ingresar otra cosa que no sean numeros")
      if menu == 2:
         print("Saldo disponible:", plata)
         try:
            retiro = float(input("Ingrese la cantidad que desea retirar"))
            plata= plata - retiro
            print(" Este es el saldo que le quedo:", plata)
            if retiro > plata:
               print(" No se puede retirar una cantidad mayor al saldo")
         except ValueError:
            print("No se puede retirar letras o palabras")
      if menu == 3:
         print("Cerrando el programa")
         break


def ejercicio2 ():
   try:
      n1=float(input("Ingrese su peso"))
      n2=float(input("Ingrese su altura"))
      Imc=n1/n2**2
      if Imc<18.5:
         print("Usted tiene bajo peso")
      elif Imc>18.5 and Imc<24.5:
         print("Usted tiene un peso saludable")
      elif Imc>25.0 and Imc<29.9:
         print("Usted tiene sobrepeso")
      else:
         print("Usted tiene obesidad")
   except ValueError:
      print("Ingrese un valor apropiado")

def ejercicio3():
    import random
    vocales = ["a", "e", "i", "o", "u"]
    while frase != "agusfortnite2008":
        frase = str(input("Ingrese una frase: "))
        frase_final = ""
        for letra in frase:
            if letra in vocales:
                letra = random.choice(vocales)
            frase_final = frase_final + letra

def ejercicio4():
    try:
        frase = str(input("Ingrese una frase: "))
        palabras = frase.split()
        for letra in palabras:
            print(letra[::-1])
    except ValueError:
        print("Ingresar un texto, no numeros.")

def ejercicio5():
    nombres = []
    while 0 == 0:
        print("Base de datos")
        print("Ingrese que desea hacer: ")
        print("1) Agregar nombre.")
        print("2) Revisar nombre.")
        print("3) Cerrar Programa.")
        menu = int(input("--> "))
        if menu == 1:
            try:
                nombre = str(input("Ingrese que nombre desea agregar: "))
                nombres.append(nombre)
                print(f"\n \n \n")
            except ValueError:
                print("")
                print(f"\n \nIngrese un nombre, no números. \n")
        elif menu == 2:
            try:
                buscar = int(input("Ingrese el número de índice del nombre que desea ver: "))
                print(f"\n \n{nombres[buscar]} \n")
            except (ValueError, IndexError):
                print(f"\n \nPor favor, no ingrese un número de índice mayor al que esta disponible y no ingrese cosas que no sean números.. \n")
        elif menu == 3:
            print("Cerrando programa...")
            break
        else:
            print(f"\n \nEsa opción no se encuentra disponible, intente otra vez. \n")

while 0 == 0:
    print("Este es el menú")
    ejercicio = int(input("Ingrese el ejercicio desea corregir (Ingrese 0 para terminar): "))
    if ejercicio == 1:
        ejercicio1()
    elif ejercicio == 2:
        ejercicio2()
    elif ejercicio == 3:
        ejercicio3()
    elif ejercicio == 4:
        ejercicio4()
    elif ejercicio == 5:
        ejercicio5()
    elif ejercicio == 0:
        print("Finalizando programa...")

        break
