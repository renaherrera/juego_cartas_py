import os
import time
import json
import msvcrt
import random
from dicts import *

rangos = ["Bronce 1", "Bronce 2", "Bronce 3", "Plata 1", "Plata 2", "Oro 1", "Oro 2", "Platino 1", "Platino 2", "Diamante"]
prof = "Alanbrito"
mazo = []

#-------COLORES--------#
RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"
BLANCO = "\033[37m"

def greenprint(message):
    print(f"\033[32m{message}\033[0m")

def redprint(message):
    print(f"\033[31m{message}\033[0m")

def yellowprint(message):
    print(f"\033[33m{message}\033[0m")

def greenprint(message):
    print(f"\033[32m{message}\033[0m")
#-------COLORES--------#
#te amo mi angelito de mi corazon eres el mejor novio del mundo#
#-------LEER JSONS-----#
with open("cartas.json", "r", encoding="utf-8") as archivo:
    cartas = json.load(archivo)
#-------LEER JSONS-----#

#-------PLAYER AND BOT---#

player = {
    "nombre": None,
    "rango": rangos[0],
    "puntos": 1,
    "dinero": 0
    #cantidad de cartas
    #cantidad de partidad jugadas
    #victorias y derrotas
}

bots = {
    "nombre": f"Guest{random.randint(1, 200)}",
    "puntos": {
        "puntos_bronce": random.randint(1, 20),
        "puntos_plata": random.randint(21, 40),
        "puntos_oro": random.randint(41, 60),
        "puntos_platino": random.randint(61, 80),
        "puntos_diamante": random.randint(81, 100)
    },
    "mazo":{ #completar
        "mazo_bronce": [
            cartas[0],
            cartas[1],
            cartas[2]
        ],#completar los demas mazos
        "mazo_plata": print(),
        "mazo_oro": print(),
        "mazo_platino": print(),
        "mazo_diamante": print()
    }
} 

#-------PLAYER---------#

#-------FUNCIONES------#
def fun_loading():
    puntos = ""
    for i in range(4):
        print(f"Cargando{puntos}")
        puntos += "."
        time.sleep(0.7)
        os.system("cls")

def press_tecla():
    print("» Pulse tecla para continuar")
    msvcrt.getch()
    os.system("cls")

def playername():
    player["nombre"] = input("Porfavor dime tu nombre: ").upper()

def messages():
    print("???: ¡Bienvenido Jugador!")
    press_tecla()
    print("???: Estas apunto de encaminarte en esta aventura muy emocionante...")
    press_tecla()
    print("???: Te ves un poco mal...¿Estás bien?") #Hacer sistema de si/no para respuestas diferentes...
    press_tecla()
    print("???: De pronto saliste de ese basurero muy aturdido...")
    press_tecla()
    print("???: Supuse que eras un jugador común y corriente, pero al parecer no...")
    press_tecla()
    print(f"{prof}: Oh...Disculpa la falta de respeto, soy el Prof. {prof},")
    press_tecla()
    
    playername()
    
    os.system("cls")
    print(f"{prof}: Oh, hola {player['nombre']} disculpa mi falta de respeto al inicio...")
    press_tecla()
    print(f"{prof}: Por cierto... bonito nombre")
    press_tecla()
    print(f"{prof}: Bueno... espero que te sientas preparado para esta aventura")
    press_tecla()
    print(f"{prof}: Ahora te dirigirás a un menú en el cual podrás iniciar la aventura o leer el tutorial.")
    press_tecla()
    print(f"{prof}: Mucha suerte {player['nombre']}. ¡Buen viaje!")

def menu_tutorial(options):
    while True:
        print(f"Bienvenido {player['nombre']} este es el Menú inicial.")
        yellowprint("-"*50)
        print("1. Leer un tutorial (Recomendado)")
        print("2. Iniciar Sesion")
        print("3. Registrase")
        print("4. Iniciar aventura")
        print("5. Cerrar juego")
        yellowprint("-"*50)
        try:
            opc = int(input(f"{VERDE}Ingrese la opción que deseea:{RESET} "))
            
            if opc in options:
                break
            else:
                redprint("ERROR! esa opcioón no existe!")
        except:
            redprint("ERROR! el caractér ingresado no es un número!")
    return opc
            
def menu_aventura(options):
    while True:
        print("*Menu Aventura*")
        yellowprint("-"*50)
        #Agregar datos como puntos, rango, dinero, y nombre del usuario
        print(f"1. Iniciar partida {ROJO}(RANKED){RESET}")
        print(f"2. Inciar partida {CIAN}(NORMAL){RESET}")
        print("3. Armar mazo")
        print("4. Ver perfil")
        print("5. Tienda")
        print("6. Cerrar juego")
        yellowprint("-"*50)
        try:
            opc = int(input(f"{VERDE}Ingrese la opción que deseea:{RESET} "))
            
            if opc in options:
                break
            else:
                redprint("ERROR! no existe esa opción!")
        except:
            redprint("ERROR! el caractér ingresado no es un número!")
    return opc

def ver_perfil():
    yellowprint("-"*50)
    print(f"Nombre: {player['nombre']}")
    print(f"Puntos: {player['puntos']}")
    print(f"Dinero: {player['dinero']}")
    print(f"Rango: {player['rango']}")
    if len(mazo) == 0:
        print("Mazo: Tienes que armarlo en la opcion 3!")
    else:
        print(f"Mazo: ")
        for i in range(len(mazo)):
            print(f"\t{mazo[i]['nom_carta']}")
    yellowprint("-"*50)
#-------FUNCIONES------#