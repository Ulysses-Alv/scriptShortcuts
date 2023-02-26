import keyboard
import pyautogui as pyt
import mouse
import winsound
import time


def fun(key, mousebutton) :
    if keyboard.is_pressed(key) or mouse.is_pressed(button=mousebutton):
        return