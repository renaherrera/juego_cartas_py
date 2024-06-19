import json

def validacion_input(p_usrmessage,p_passmessage):
    while True:
        usr = input(p_usrmessage)
        if len(usr) > 0:
            break
        else:
            print("ERROR! no puede estar vacío!")
    while True:
        passwd = input(p_passmessage)
        if len(usr) > 0:
            break
        else:
            print("ERROR! no puede estar vacío!")
    return usr, passwd
