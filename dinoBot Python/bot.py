# -*- coding: utf-8 -*-
from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np

class Coordinates():
    replayButton = (303,390)
    dinosaur = (107,425) #401 it was when standing
    # 200 = x coordinate to check for tree
    # 425 = y coordinate yo check
def restartGame():
    pyautogui.click(Coordinates.replayButton)
    pyautogui.keyDown('down')
    
def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')
    
def imageGrab():
    box = (Coordinates.dinosaur[0]+95, Coordinates.dinosaur[1], Coordinates.dinosaur[0]+135, Coordinates.dinosaur[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = np.array(grayImage.getcolors())
    print(a.sum())
    return a.sum()
    
# while True:
#     imageGrab()
    
def main():
    restartGame()
    while True:
        if imageGrab() > 447:
            pressSpace()
            # time.sleep(0.1)
            
main()