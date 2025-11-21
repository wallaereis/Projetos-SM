import pyautogui as py
import time
import pyperclip

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

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)


py.write('Recibos - Premiações de Novembro 2025 - Fonseca')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')


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

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Piratininga')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')


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

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Itaipu')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')


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

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Santa Cruz')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')


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

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')



# LOJA DE PORTO NOVO

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.portonovo')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('julio cezar')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')


# LOJA DE BATALHA

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.largo')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('julio cezar')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')



# LOJA DE NOVA IGUACU

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.novai')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('robertos')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')




# LOJA DE PORTO VELHO

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.portovelho')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('julio cezar')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')



# LOJA DE ENGENHO

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.engenho')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('julio cezar')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')




# LOJA DE MESQUITA

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.mesquita')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('robertos')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')



# LOJA DE VALVERDE

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.valverde')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('robertos')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')




# LOJA DE BARRETO

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.barreto')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('julio cezar')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')




# LOJA DE NOVA AMÉRICA

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.novaam')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('robertos')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')


# LOJA DE INHAUMA

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.inhauma')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('robertos')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')


# LOJA DE CURTUME

# transforma o generator em lista
botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

if len(botoes) > 0:
    # pega o primeiro elemento da lista
    primeiro = botoes[0]
    
    # clica no botão
    py.click(primeiro)


py.write('gerencia.curtume')

py.press('enter')

py.write('savio ')

py.press('enter')

py.write('robertos')

py.press('enter')

py.write('thiago.bon')

py.press('enter')

# transforma o generator em lista
assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

if len(assunto) > 0:
    # pega o primeiro elemento da lista
    segundo = assunto[0]
    
    # clica no botão
    py.click(segundo)

py.write('Recibos - Premiações de Novembro 2025 - Lote XV')

for x in range(2):
    py.press('tab')

texto = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"

pyperclip.copy(texto)
py.hotkey('ctrl', 'v')







