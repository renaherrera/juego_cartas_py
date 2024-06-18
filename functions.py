#-------COLORES--------#
RESET = "\033[0m"
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
MAGENTA = "\033[35m"
CIAN = "\033[36m"
BLANCO = "\033[37m"

def redprint(message):
    print(f"\033[31m{message}\033[0m")

def yellowprint(message):
    print(f"\033[33m{message}\033[0m")

def greenprint(message):
    print(f"\033[32m{message}\033[0m")
#-------COLORES--------#

#-------FUNCIONES------#
def menu(options):
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
            opc = int(input(f"{VERDE}Ingrese la opción que deseea:{RESET}"))
            
            if opc in options:
                break
            else:
                redprint("ERROR! no existe esa opción!")
        except:
            redprint("ERROR! el caractér ingresado no es un número!")
    return opc
            
#-------FUNCIONES------#