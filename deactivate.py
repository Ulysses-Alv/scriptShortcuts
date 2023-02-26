import keyboard

activated = True

def desactivate(key) :
    global activated
    activated = not keyboard.is_pressed(key)