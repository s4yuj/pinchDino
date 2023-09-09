import pyautogui
from PIL import Image, ImageGrab
import time


def takeScreenshot():
    image = ImageGrab.grab().convert("L")
    return image


def hit(key):
    pyautogui.keyDown(key)


def isCollision(data):
    for x in range(500, 600):
        for y in range(560, 670):
            while data[x, y] in range(170,190):
                return True
    return False


if __name__ == '__main__':
    print('bot is starting...')
    time.sleep(2)
    while True:
        image = takeScreenshot()
        data = image.load()
        if isCollision(data):
            hit('space')   
'''
            #rectangle tester
        for x in range(500, 600):
            for y in range(560,670):
                data[x,y] = 0
        image.show()
        break
'''