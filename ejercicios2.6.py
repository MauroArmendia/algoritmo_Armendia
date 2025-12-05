def ej1():
    matriz = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]


    print("Recorrido de la matriz:")
    for fila in matriz:
        for elemento in fila:
            print(elemento, end=" ")
        print()


def ej2():
    matriz = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]
    suma=0
    print("Recorrido de la matriz:")
    for fila in matriz:
        for elemento in fila:
            suma=elemento+suma
    print("el resultado de la suma es:", suma)


ej2()


def ej3():
    matriz1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    fila = int(input("Ingrese que número de fila desea revisar: ")) - 1
    elemento_fila = int(input(f"Ingrese que elemento de la fila {fila} desea revisar: ")) - 1
    print(matriz1[fila][elemento_fila])


def ej4():
    matriz1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    num_grande=0
    for fila in matriz1:
        for num in fila:
            if num > num_grande:
                num_grande = num

    print(num_grande)
ej4()
