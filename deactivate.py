import keyboard

activated = False

def desactivar(key) :
    global activated
    activated = not keyboard.is_pressed("w")