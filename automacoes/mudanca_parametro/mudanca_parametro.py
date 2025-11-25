import pyautogui as py
import time
import openpyxl as xl

# AUTOMAÇÃO PARA MUDANÇA DE PARAMETRO DE PRODUTO LOJA INHAUMA

df = xl.load_workbook(r"C:\Users\wallace.souza\Downloads\teste.xlsx", data_only=True)

ws = df["Plan1"]

print("o programa começou")

py.hotkey('alt' , 'tab')

py.FAILSAFE = True
py.PAUSE = 0.5


for row in ws.iter_rows(min_row=2):
    py.press("f2")
    py.write(str(row[0].value))
    py.press("f8")
    py.click(183,159)
    py.moveTo(469,345)
    for x in range(2):
        py.scroll(-5000)
    
    py.click(539,395)
    py.doubleClick()
    py.press("delete")
    py.write(str(row[2].value))
    py.press("tab")
    py.write(str(row[3].value))
    py.press("f4")
    py.press("f2")



print("o programa terminou")




