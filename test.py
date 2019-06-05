"""

All coordinates assume a screen resolution of 1280x1024, and Chrome
maximized with the Bookmarks Toolbar enabled.
Down key has been hit 4 times to center play area in browser.
x_pad = 516
y_pad = 277
Play area =  x_pad+1, y_pad+1, 834,595
"""
#Globals
#----------------------------

from PIL import ImageGrab
import PIL.Image
from PIL import Image
import os
import time
import webbrowser
import win32api , win32con
import pyautogui
from state import State
from MovesGenerator import MovesGenerator
from MinimaxAlgorithm import minimax
from StateEvaluator import is_gameover
from StateEvaluator import evaluate
from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
class Coordinates():
    startBtn=(690, 425)
    playBtn=(683, 590)

def startGame():
    pyautogui.click(Coordinates.startBtn)


def playGame():
    pyautogui.click(Coordinates.playBtn)

def screenGrab():
    x = 526
    y = 275
    step = 40
    box = (x ,y , x+(8*step) , y+(8*step))
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\image' + '.png', 'PNG')

def sendState():
    board =[[],[],[],[],[],[],[],[]]
    row = []
    x = 7
    y = 14
    step = 40
    screenGrab()
    ima = Image.open('image.png')
    rgb_im = ima.convert('RGB')
    for i in range(8):
        for j in range(8):
            r, g, b = rgb_im.getpixel(((x+(step*i)), (y+(step*j))))
            if (r in range (150 , 250) and g in range (150 , 250)  and b in range (150 , 250)):
                board[j].append(2)
            elif(r in range (0 , 100 ) and g in range (0 , 100)  and b in range (0 , 100) ):
                board[j].append(1)
            else:
                board[j].append(0)
    for row in board:
        print(row)
    print("\n")
    return board


def calacePosition(second,first):
    x = 546
    y = 290
    step=40
    pyautogui.click(x+(step*first) , y+(step*second))

time.sleep(2)
startGame()
time.sleep(2)
playGame()
time.sleep(2)
playGame()
time.sleep(2)
playGame()

while(True):
    time.sleep(10)
    state = State(sendState(), WHITECELL)
    state = minimax(state)

    print("Next State: ")
    for row in state[0].board:
        print(row)
    print("\n")


    if(state[0].x == -1 and state[0].y == -1):
        print(
            f"Player didn't have a play")
        continue


    calacePosition(state[0].x, state[0].y)
    if(is_gameover(state[0])):
        break

