from functions import *
from juego import *

os.system("cls")

#messages()

while True:
    opc = menu_tutorial( [1,2,3] )
    
    os.system("cls")
    if opc == 1:
        pass
    elif opc == 2:
        while True:
            opc = menu_aventura( [1,2,3,4,5,6] )

            os.system("cls")
            if opc == 1:
                pass
            elif opc == 2:
                pass
            elif opc == 3:
                armar_mazo()
            elif opc == 4:
                pass
            elif opc == 5:
                pass
            else:
                greenprint("¡NOS VEMOS PRONTO!")
                exit()
    else:
        break