import os
import pyautogui
import keyboard
import time


#os.startfile(r'C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64\mpc-hc64.exe')
os.startfile(r'C:\Program Files\K-Lite Codec Pack\MPC-HC\mpc-hc.exe')
time.sleep(10)
pyautogui.moveTo(16, 936, duration = 1)
pyautogui.click()
pyautogui.moveTo(640, 512, duration = 1)
while True:
    if keyboard.read_key() == "0" or keyboard.read_key() == "ctrl" or keyboard.read_key() == "space":
        #pyautogui.hotkey('altleft', 'f4')вместо этой функции используем закрытие файла программы системное
        os.system('taskkill /pid mpc-hc.exe')
        pyautogui.moveTo(640, 512, duration = 1)
        os.startfile(r'C:\Program Files\AIMP\AIMP.exe')
        break

