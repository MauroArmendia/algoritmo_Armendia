import random

def crear_tablero():
    tablero = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]
    ]
    return tablero

def mostrar_tablero(tablero):
    print("  0 1 2 3 4")
    for i in range(5):
        print(i, end=" ")
        for j in range(5):
            print(tablero[i][j], end=" ")
        print()

def colocar_barcos(tablero, cantidad):
    barcos = 0
    while barcos < cantidad:
        fila = random.randint(0, 4)
        columna = random.randint(0, 4)
        if tablero[fila][columna] == " ":
            tablero[fila][columna] = "B"
            barcos += 1

def disparar(tablero_visible, tablero_barcos):
    fila = int(input("Elija fila (0 a 4): "))
    columna = int(input("Elija columna (0 a 4): "))
    if tablero_barcos[fila][columna] == "B":
        print("Tocado")
        tablero_visible[fila][columna] = "X"
        tablero_barcos[fila][columna] = "X"
    else:
        print("Agua")
        tablero_visible[fila][columna] = "~"

def quedan_barcos(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == "B":
                return True
    return False

def jugar():
    tablero_jugador = crear_tablero()
    tablero_oculto = crear_tablero()
    colocar_barcos(tablero_oculto, 3)
    print("Comienza la batalla naval")
    while quedan_barcos(tablero_oculto):
        mostrar_tablero(tablero_jugador)
        disparar(tablero_jugador, tablero_oculto)
    mostrar_tablero(tablero_jugador)
    print("Hundiste todos los barcos. Victoria")

jugar()