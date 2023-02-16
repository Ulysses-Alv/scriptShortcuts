import keyboard
import pyautogui as pyt
import winsound


Apretado = False 

def holdClick(key):
    global Apretado
    
    if keyboard.is_pressed(key):
        Apretado = not Apretado
        winsound.PlaySound('sample.wav', winsound.SND_FILENAME|winsound.SND_NOWAIT)    
    if Apretado == True:
        pyt.mouseDown()
    else :
        pyt.mouseUp()
