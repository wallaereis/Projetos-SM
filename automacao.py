import pyautogui as py
import time

py.FAILSAFE = True
py.PAUSE = 0.5

time.sleep(3)


# LOJA DO FONSECA

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.fonseca')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('julio cezar')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

for x in range(4):
    py.press('tab')

py.write('Recibos - Premiações de Novembro 2025 - Fonseca')

for x in range(2):
    py.press('tab')

py.write("Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mes de Novembro.\n\nFico a disposicao para quaisquer esclarecimentos que se fizerem necessarios.\n\nAtenciosamente,")



# LOJA DE PIRATININGA


# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.piratininga')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('julio cezar')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

for x in range(4):
    py.press('tab')

py.write('Recibos - Premiações de Novembro 2025 - Piratininga')

for x in range(2):
    py.press('tab')

py.write("Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mes de Novembro.\n\nFico a disposicao para quaisquer esclarecimentos que se fizerem necessarios.\n\nAtenciosamente,")




# LOJA DE ITAIPÚ


# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.itaipu')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('julio cezar')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

for x in range(4):
    py.press('tab')

py.write('Recibos - Premiações de Novembro 2025 - Itaipu')

for x in range(2):
    py.press('tab')

py.write("Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mes de Novembro.\n\nFico a disposicao para quaisquer esclarecimentos que se fizerem necessarios.\n\nAtenciosamente,")



# LOJA DE SANTA CRUZ


# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.santa')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('robertos')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

for x in range(4):
    py.press('tab')

py.write('Recibos - Premiações de Novembro 2025 - Santa Cruz')

for x in range(2):
    py.press('tab')

py.write("Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mes de Novembro.\n\nFico a disposicao para quaisquer esclarecimentos que se fizerem necessarios.\n\nAtenciosamente,")



# LOJA DE LOTE XV

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.lote')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('robertos')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

for x in range(4):
    py.press('tab')

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

py.write("Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mes de Novembro.\n\nFico a disposicao para quaisquer esclarecimentos que se fizerem necessarios.\n\nAtenciosamente,")

