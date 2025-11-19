import pyautogui as py
import time

### mudar parametro loja 3 com planilha excel

py.PAUSE = 0.5

py.hotkey('alt', 'tab')
py.hotkey('ctrl', 'c')

time.sleep(2)  

py.keyDown('alt')    
py.press('tab', presses=2, interval=0.3) 
py.keyUp('alt')
py.press('f2') 
py.hotkey('ctrl','v') 
py.press('f8') 

for x in range(5):
    py.hotkey('ctrl','tab') 

time.sleep(1)
py.moveTo(x=520,y=292)

py.doubleClick()

py.hotkey('alt', 'tab')

for x in range(2):
    py.press('right')

py.hotkey('ctrl', 'c')
py.hotkey('alt', 'tab')
py.hotkey('ctrl', 'v')
py.press('tab')

py.hotkey('alt', 'tab')
py.press('right')
py.hotkey('ctrl', 'c')
py.hotkey('alt', 'tab')
py.hotkey('ctrl', 'v')

time.sleep(1)

py.press('f4') 
time.sleep(1)

py.press('f2')

time.sleep(1)


py.hotkey('alt', 'tab')

py.hotkey('ctrl', 'left')

py.press('down') 




for x in range(15):
    py.hotkey('ctrl','c') 
    py.hotkey('alt', 'tab')
    py.hotkey('ctrl','v') 
    py.press('f8') 

    for x in range(5):
        py.hotkey('ctrl','tab') 

    time.sleep(1)
    py.moveTo(x=520,y=292)
    
    py.doubleClick()

    time.sleep(1)

    py.hotkey('alt', 'tab')

    
    for x in range(2):
        py.press('right')

    py.hotkey('ctrl', 'c')
    py.hotkey('alt', 'tab')
    py.hotkey('ctrl', 'v')
    py.press('tab')

    py.hotkey('alt', 'tab')
    py.press('right')
    py.hotkey('ctrl', 'c')
    py.hotkey('alt', 'tab')
    py.hotkey('ctrl', 'v')

    time.sleep(1)

    py.press('f4') 
    time.sleep(1)

    py.press('f2')

    time.sleep(1)


    py.hotkey('alt', 'tab')

    py.hotkey('ctrl', 'left')

    py.press('down') 

