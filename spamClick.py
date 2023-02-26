import keyboard
import pyautogui as pyt
import mouse


def spamClick(key, mousebutton):
    if keyboard.is_pressed(key) or mouse.is_pressed(button=mousebutton):
        pyt.click()