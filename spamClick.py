import keyboard
import pyautogui as pyt


def spamClick(key):
    if keyboard.is_pressed(key):
        pyt.click()