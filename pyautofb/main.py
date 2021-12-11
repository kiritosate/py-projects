import pyautogui
import time

time.sleep(5)

pyautogui.FAILSAFE = True

while(True):

    for i in range(100):

        pyautogui.write(f'{i}')

        pyautogui.press('enter')

