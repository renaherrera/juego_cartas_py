from functions import *
import os

vida = 100
mazo = []

def armar_mazo():
    while len(mazo) <= 2:
        for arm_mazo in mazo_player:
            yellowprint("*"*50)
            print(f"Carta {arm_mazo['num']}")
            print(f"Nombre: {arm_mazo["nom_carta"]}")
            print(f"Daño: {arm_mazo['danio']}")
            print(f"Tipo: {arm_mazo['tipo']}")
            print(f"Usos: {arm_mazo['usos_partida']['usos_player']}")
            yellowprint("*"*50)
            print("")
        
        opc = input("Ingresa el nombre de la carta que quieres agregar: ")
        
        for i in range(len(mazo_player)):
            if opc.capitalize() == mazo_player[i]['nom_carta']:
                mazo.append(mazo_player[i])
                os.system("cls")
                greenprint("Carta agregada a tu mazo!")
                press_tecla()
                break
        else:
            os.system("cls")
            redprint("ERROR! no se ha encontrado la carta!")
            press_tecla() 
                    
def system_game():
    if len(mazo) > 0:
        pass
    else:
        redprint("ERROR! debes armar un mazo en la opción 3!")

armar_mazo()