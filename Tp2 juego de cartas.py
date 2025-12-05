import random


def dar_carta():
    num_carta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    palo_carta = ["Corazones", "Diamantes", "Tréboles", "Picas"]
    carta = []
    num = random.choice(num_carta)
    palo = random.choice(palo_carta)
    carta.append(num)
    carta.append(palo)
    return carta


def generar_mano_y_valor():
    carta1=dar_carta()
    carta2=dar_carta()
    carta3=dar_carta()

    if carta1[0]>=10:
        valordelamano=10 + carta2[0] + carta3[0]
    elif carta2[0]>=10:
        valordelamano=carta1[0] + 10 + carta3[0]
    elif carta3[0]>=10:
        valordelamano=carta1[0] + carta2[0] + 10
    elif carta1[0]>=10 and carta2[0]>=10 and carta3[0]>=10:
        valordelamano=10 + 10 + 10
    else:
        valordelamano = carta1[0] + carta2[0] + carta3[0]

    return valordelamano, carta1, carta2, carta3


def menu_juego():
    valoractual=0
    while True:
        accion=int(input("Ingrese 1 si quiere seguir o 2 si quiere salir: "))
        if accion==1:
            valordelamano, carta1, carta2, carta3=generar_mano_y_valor()
            print(f"La mano es: {carta1},{carta2},{carta3}")
            valoractual=valordelamano+valoractual
            print(f"El valor de la mano es:{valoractual}")
        elif accion==2 and valoractual>=100:
            print(f"Usted Gano, tu puntaje total es: {valoractual}")
            break
        elif accion==2 and valoractual<100:
            print(f"Perdiste, tu puntaje total es: {valoractual}")
            break
        else:
            print("Ingrese una acción correcta")
menu_juego()
