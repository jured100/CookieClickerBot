import pyautogui
import os
import time
import _thread
pyautogui.PAUSE = 0.025

# import mss

cursorcount = 0
grandmacount = 0
farmcount = 0
minecount = 0
factorycount = 0
bankcount = 0
templecount = 0

cursorflag = False
grandmaflag = False
farmflag = False
mineflag = False
factoryflag = False
bankflag = False
templeflag = False

confidencer = 0.9992
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()
# pyautogui.moveTo(100, 150)
# pyautogui.click('button.png')

cwd = os.getcwd() + "/pictures/"
time.sleep(3)

screen = pyautogui.screenshot()
screen.save(cwd + 'current.png')
cookiecoords = pyautogui.locateOnScreen(cwd + "cookie.png", confidence=0.8)
pyautogui.moveTo(cookiecoords)


def cursordoer():
    global cursorcount
    coords3 = pyautogui.locateOnScreen(cwd + "cursor2.png", confidence=confidencer)
    if coords3 is not None:
        cursorcount += 1
        pyautogui.click(coords3)
        pyautogui.moveTo(cookiecoords)


def grandmadoer():
    global grandmacount, cursorcount
    coords3 = pyautogui.locateOnScreen(cwd + "grandma2.png", confidence=confidencer)
    print("grandmadoer", coords3)
    if coords3 is None:
        if cursorcount < grandmacount * 3:
            cursordoer()
    else:
        grandmacount += 1
        pyautogui.click(coords3)
        pyautogui.moveTo(cookiecoords)


def farmdoer():
    global farmcount, grandmacount, cursorcount
    coords3 = pyautogui.locateOnScreen(cwd + "farm2.png", confidence=confidencer)
    if coords3 is None:
        if grandmacount < farmcount * 3:
            grandmadoer()
    else:
        farmcount += 1
        pyautogui.click(coords3)
        pyautogui.moveTo(cookiecoords)


def minedoer():
    global minecount, farmcount, grandmacount, cursorcount
    coords3 = pyautogui.locateOnScreen(cwd + "mine2.png", confidence=confidencer)
    if coords3 is None:
        if farmcount < minecount * 3:
            farmdoer()
    else:
        minecount += 1
        pyautogui.click(coords3)
        pyautogui.moveTo(cookiecoords)


def factorydoer():
    global factorycount, minecount, farmcount, grandmacount, cursorcount
    coords3 = pyautogui.locateOnScreen(cwd + "factory2.png", confidence=confidencer)
    if coords3 is None:
        if minecount < factorycount * 3:
            farmdoer()
    else:
        factorycount += 1
        pyautogui.click(coords3)
        pyautogui.moveTo(cookiecoords)


def bankdoer():
    global bankcount, factorycount, minecount, farmcount, grandmacount, cursorcount
    coords3 = pyautogui.locateOnScreen(cwd + "bank2.png", confidence=confidencer)
    if coords3 is None:
        if factorycount < bankcount * 3:
            farmdoer()
    else:
        bankcount += 1
        pyautogui.click(coords3)
        pyautogui.moveTo(cookiecoords)


def templedoer():
    global templecount, bankcount, factorycount, minecount, farmcount, grandmacount, cursorcount
    coords3 = pyautogui.locateOnScreen(cwd + "temple2.png", confidence=confidencer)
    if coords3 is None:
        if bankcount < templecount * 3:
            farmdoer()
    else:
        templecount += 1
        pyautogui.click(coords3)
        pyautogui.moveTo(cookiecoords)

#def click():
    #while True:
        #pyautogui.click()


flagchecker = -1
upgradechecker = -1
#_thread.start_new_thread( click() )
while True:
    screen = pyautogui.screenshot()
    screen.save(cwd + 'current.png')
    flagchecker += 1
    upgradechecker += 1
    for i in range(20):
        pyautogui.click()
    coords = pyautogui.locateOnScreen(cwd + "godcookie.png", confidence=0.9)
    if coords is not None:
        pyautogui.click(coords)
        pyautogui.moveTo(cookiecoords)
    screen = pyautogui.screenshot(region=(1510, 400, 350, 600))
    screen.save(cwd + 'current.png')
    coords=0
    if upgradechecker == 25:
        pyautogui.moveTo(1560, 300)
        pyautogui.click()
        pyautogui.moveTo(cookiecoords)
        upgradechecker=0

    if not grandmaflag:
        cursordoer()
    elif not farmflag:
        grandmadoer()
    elif not mineflag:
        farmdoer()
    elif not factoryflag:
        minedoer()
    elif not bankflag:
        factorydoer()
    elif not templeflag:
        bankdoer()
    else:
        templedoer()

    if not templeflag and (flagchecker == 10 or flagchecker == 0):
        coords2=0
        coords=0
        flagchecker = -1
        if not cursorflag:
            coords = pyautogui.locateOnScreen(cwd + "cursor1.png", confidence=confidencer)
            coords2 = pyautogui.locateOnScreen(cwd + "cursor2.png", confidence=confidencer)
            print(coords2)
            if coords is not None or coords2 is not None:
                cursorflag = True
                print("cursorflag: True")
        elif not grandmaflag:
            coords = pyautogui.locateOnScreen(cwd + "grandma1.png", confidence=confidencer)
            coords2 = pyautogui.locateOnScreen(cwd + "grandma2.png", confidence=confidencer)
            if coords is not None or coords2 is not None:
                grandmaflag = True
                print("grandmaflag: True", coords, coords2)
        elif not farmflag:
            coords = pyautogui.locateOnScreen(cwd + "farm1.png", confidence=confidencer)
            coords2 = pyautogui.locateOnScreen(cwd + "farm2.png", confidence=confidencer)
            if coords is not None or coords2 is not None:
                farmflag = True
                print("farmflag: True")
        elif not mineflag:
            coords = pyautogui.locateOnScreen(cwd + "mine1.png", confidence=confidencer)
            coords2 = pyautogui.locateOnScreen(cwd + "mine2.png", confidence=confidencer)
            if coords is not None or coords2 is not None:
                mineflag = True
                print("mineflag: True")
        elif not factoryflag:
            coords = pyautogui.locateOnScreen(cwd + "factory1.png", confidence=confidencer)
            coords2 = pyautogui.locateOnScreen(cwd + "factory2.png", confidence=confidencer)
            if coords is not None or coords2 is not None:
                factoryflag = True
                print("factoryflag: True")
        elif not bankflag:
            coords = pyautogui.locateOnScreen(cwd + "bank1.png", confidence=confidencer)
            coords2 = pyautogui.locateOnScreen(cwd + "bank2.png", confidence=confidencer)
            if coords is not None or coords2 is not None:
                bankflag = True
                print("bankflag: True")
        elif not templeflag:
            coords = pyautogui.locateOnScreen(cwd + "temple1.png")
            coords2 = pyautogui.locateOnScreen(cwd + "temple2.png")
            if coords is not None or coords2 is not None:
                templeflag = True
                print("templeflag: True")

