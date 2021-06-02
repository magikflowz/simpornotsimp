import os
import pyautogui

def recycle():
    try:
        os.chdir(r"C:\Users\Magik\Desktop")
        cwd = os.getcwd()
        result = cwd
        if result == 'C:\\Users\\Magik\\Desktop':
            print("change was successfull!")
    except FileNotFoundError:
        print("Can't find directory\n check your directory input")
        
    recycle_bin = pyautogui.locateCenterOnScreen(r'C:\Users\Magik\Desktop\python\recycle.png', grayscale=False)
    pyautogui.rightClick(recycle_bin)
    empty_bin = pyautogui.locateCenterOnScreen(r'C:\Users\Magik\Desktop\python\empty.png')
    pyautogui.click(empty_bin)
    yes = pyautogui.locateCenterOnScreen(r'C:\Users\Magik\Desktop\python\yes.png', grayscale=False)
    pyautogui.press(['enter'])

recycle()