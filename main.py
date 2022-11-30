from os import system

def whoami ():
    system("whoami > whoami.txt")
    im = open('whoami.txt')
    user = im.read()
    return user


def tryPass (password):
    while True:
     userBefore = whoami()
     print("Intentando con la Contraseña \"{}\"".format(password))
     userAfter = whoami()
     if (userBefore != userAfter):
        break


tryPass("gCeF")