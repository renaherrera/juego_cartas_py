from functions import *
from juego import *
from login_system import *

os.system("cls")

#messages()

while True:
    opc = menu_tutorial( [1,2,3,4,5] )
    
    os.system("cls")
    if opc == 1:
        pass
    elif opc == 2:        
        pass
    elif opc == 3:
        usr,passwd = validacion_input("Ingrese su nuevo nombre de usuario: ", "Ingrese su nueva contraseña: ")
    elif opc == 4:
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
                ver_perfil()
            elif opc == 5:
                pass
            else:
                greenprint("¡NOS VEMOS PRONTO!")
                exit()
    else:
        break