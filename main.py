import pyautogui,keyboard,psutil,time
def btnCheck():
    flw = pyautogui.locateOnScreen('dataset/follow.png', grayscale=True, confidence=0.92)
    if flw != None:
        pyautogui.leftClick(flw)
def btnYoure():
    cls = pyautogui.locateOnScreen('dataset/close.png', grayscale=True, confidence=0.92)
    scroll = pyautogui.locateOnScreen('dataset/scroll.png', grayscale=True, confidence=0.92)
    youre = pyautogui.locateOnScreen('dataset/youre.png', grayscale=True, confidence=0.92)
    if cls != None and youre == None:
        pyautogui.leftClick(scroll)
        pyautogui.leftClick(scroll)
        pyautogui.leftClick(youre)
    elif youre != None:
        pyautogui.leftClick(youre)
    else:
        pass
def btnBreak():
    breakfollow = pyautogui.locateOnScreen('dataset/break.png', grayscale=True, confidence=0.92)
    if  breakfollow != None:
        pyautogui.leftClick(breakfollow)
while True:
    btnCheck()
    time.sleep(0.50)
    btnYoure()
    time.sleep(0.25)
    btnBreak()
    
# SORRY, I FORGOT TO ADD STOP COMMAND
