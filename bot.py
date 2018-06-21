from PIL import ImageGrab
import pyautogui

class coordinates():
    replayBtn = (344,382)

def restartgame ():
    pyautogui.click(coordinates.replayBtn)
