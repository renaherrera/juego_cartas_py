import json

usuarios = []

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

def reg(p_usr, p_passwd):
    user = {
        "usuario": p_usr,
        "contrasenia": p_passwd
    }

    usuarios.append(user)

    with open("usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(usuarios, archivo, indent=4)