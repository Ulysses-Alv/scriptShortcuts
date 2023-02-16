import keyboard
import pyautogui as pyt
import winsound
import time


def fun(key) :
    if keyboard.is_pressed(key):
        return