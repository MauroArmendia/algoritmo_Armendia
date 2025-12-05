def crear_tablero():
    return tablero

def mostrar_tablero(tablero):
    for fila in tablero:
        print(fila)


def verificar_ganador(tablero, jugador):

    for fila in tablero:
        if fila[0] == fila[1] == fila[2] == jugador:
            return True

    for c in range(3):
        if tablero[0][c] == tablero[1][c] == tablero[2][c] == jugador:
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def tablero_lleno(tablero):
    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                return False
    return True

def turno(tablero, jugador):
    print("Turno del jugador", jugador)
    fila = int(input("Elige fila (1, 2, 3): ")) - 1
    columna = int(input("Elige columna (1, 2, 3): ")) - 1
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, elegí otra.")
        turno(tablero, jugador)

def jugar():
    tablero = crear_tablero()
    jugador = "X"
    ganador = False

    while not ganador and not tablero_lleno(tablero):
        mostrar_tablero(tablero)
        turno(tablero, jugador)

        if verificar_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print("El jugador", jugador, "ha ganado")
            ganador = True
        elif tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("Empate")
        else:
            if jugador == "X":
                jugador = "O"
            else:
                jugador = "X"

    respuesta = input("¿Queres jugar de nuevo? (s/n): ")
    if respuesta == "s":
        print("Empezando nueva partida")
        jugar()
    else:
        print("Finalizando")

jugar()