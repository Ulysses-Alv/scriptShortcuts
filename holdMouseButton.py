import keyboard
import pyautogui as pyt
import winsound


pressed = False 

def holdClick(key):
    global pressed
    
    if keyboard.is_pressed(key):
        pressed = not pressed
        winsound.PlaySound('sample.wav', winsound.SND_FILENAME|winsound.SND_NOWAIT)    
    if pressed == True:
        pyt.mouseDown()
    else :
        pyt.mouseUp()
