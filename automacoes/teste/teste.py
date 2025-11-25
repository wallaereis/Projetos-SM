import pyautogui as py
import time
import openpyxl as xl

# Carrega Excel
df = xl.load_workbook(r"C:\Users\wallace.souza\Downloads\teste.xlsx", data_only=True)
ws = df["Plan1"]

print("o programa começou")

py.hotkey('alt', 'tab')
py.PAUSE = 1

# Caminho da imagem enviada
imagem_botao = r"imagem.png"

for row in ws.iter_rows(min_row=1):

    # --------------------------
    # AÇÕES DO LOOP
    # --------------------------
    py.click(86, 194)
    py.write("2753")
    py.press('enter')
    time.sleep(5)


    py.click(862, 336)
    py.write(str(row[0].value))
    py.press("enter")

    py.click(1089, 381)

    # --------------------------
    # ESPERAR A IMAGEM APARECER
    # --------------------------
    print("Aguardando o botão aparecer...")

    botao = None
    while botao is None:
        botao = py.locateCenterOnScreen(imagem_botao, confidence=0.8)
        time.sleep(0.5)

    # Quando aparecer, clicar!
    py.click(botao)
    print("Botão encontrado e clicado!")

    # Depois ele volta para o início do loop automaticamente

print("o programa terminou!")
