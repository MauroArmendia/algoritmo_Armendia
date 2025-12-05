import random

matriz_tesoro = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

matriz_guia = [
    ['?¿', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10' ],
    [1, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [2, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [3, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [4, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [5, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [6, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [7, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [8, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [9, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    [10, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
]

#Crear coordenadas de bombas
def Seleccionar_Bomba():
    bomba_coordenadas = []
    fila_bomba = random.randint(0, 9)
    columna_bomba = random.randint(0, 9)
    bomba_coordenadas.append(fila_bomba)
    bomba_coordenadas.append(columna_bomba)
    return bomba_coordenadas

#Crear bombas
bomba1 = Seleccionar_Bomba()
bomba2 = Seleccionar_Bomba()
bomba3 = Seleccionar_Bomba()

#Verificar que sean diferentes
while bomba1 == bomba2 or bomba1 == bomba3 or bomba2 == bomba3:
    bomba1 = Seleccionar_Bomba()
    bomba2 = Seleccionar_Bomba()
    bomba3 = Seleccionar_Bomba()

#Posicionar bombas
matriz_tesoro [bomba1[0]] [bomba1[1]] = 1
matriz_tesoro [bomba2[0]] [bomba2[1]] = 1
matriz_tesoro [bomba3[0]] [bomba3[1]] = 1

#Variable juego
def Ejecutar_Juego():
    intentos = 5
    bombas_encontradas = 0
    while intentos > 0:
        try:
            for fila in matriz_guia:
                print("\n------------------------------------------------------")
                for elemento in fila:
                    print(elemento, end= " | ")
            print(f"\nIntentos disponibles : {intentos}")
            coordenada_x = int(input("Ingrese la coordenada X donde crees que esta la bomba (1 - 10): "))
            coordenada_y = int(input("Ingrese la coordenada Y donde crees que esta la bomba (1 - 10): "))   
            try:
                if matriz_tesoro [coordenada_x] [coordenada_y]:
                    print("Felicidades, haz encontrado una bomba")
                    intentos += 1
                    print("Intentos restaurados. \nTienes 5 intentos otra vez.")
                    bombas_encontradas += 1
                    matriz_guia [coordenada_x] [coordenada_y] = 'Correcto'
                else:
                    print("No encontraste una bomba.")
                    matriz_guia [coordenada_x] [coordenada_y] = 'Incorrecto'
            except IndexError:
                print("Por favor ingrese un número del 1 al 10")
                intentos -= 1
        except ValueError:
            print("Por favor ingrese un número,")
            intentos -= 1
        if bombas_encontradas == 3:
            print("Encontraste la bomba.")
            break                                       
        intentos -= 1
        if intentos == 0:
            print("Perdiste")
            break

#Menu interactivo
while 0 == 0:
    print("Bienvenido al buscador de tesoros ")
    try:
        menu = int(input(f"Ingrese que desea hacer: \n1. Jugar \n2. Salir \n"))
        if menu == 1:
            Ejecutar_Juego()
            break
        elif menu == 2:
            break
        else:
            print("Ingrese 1 o 2.")
    except ValueError:
        print("Por favor ingrese 1 o 2, no otro numero")