import pyautogui
import time

def screenshot():
    time.sleep(5)  
    name = time.time()
    name = ''
    img = pyautogui.screenshot()
    img.save("test.png")
    img.show()

screenshot()
