import pyautogui as py
import time
import pyperclip

py.FAILSAFE = True
py.PAUSE = 0.5


def titulo(loja):
    titulo ='Recibos - Premiações de Novembro 2025'
    pyperclip.copy(titulo + " - " + loja)
    py.hotkey('ctrl', 'v')


def descricao():
    descricao = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"
    pyperclip.copy(descricao)
    py.hotkey('ctrl', 'v')



time.sleep(3)


# # LOJA DO FONSECA

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


titulo("Fonseca")

for x in range(2):
    py.press('tab')

descricao()

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

titulo("Piratininga")

for x in range(2):
    py.press('tab')

descricao()

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

titulo("Itaipú")

for x in range(2):
    py.press('tab')

descricao()

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

titulo("Santa Cruz")

for x in range(2):
    py.press('tab')


descricao()

# # LOJA DE LOTE XV

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.lote')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('robertos')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo("Lote XV")

# for x in range(2):
#     py.press('tab')

# descricao()

# # LOJA DE PORTO NOVO

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.portonovo')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('julio cezar')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo("Porto Novo")

# for x in range(2):
#     py.press('tab')

# descricao()

# # LOJA DE BATALHA

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.largo')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('julio cezar')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo('Batalha')

# for x in range(2):
#     py.press('tab')

# descricao()

# # LOJA DE NOVA IGUACU

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.novai')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('robertos')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo("Nova Iguaçú")

# for x in range(2):
#     py.press('tab')

# descricao()


# # LOJA DE PORTO VELHO

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.portovelho')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('julio cezar')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo("Porto Velho")

# for x in range(2):
#     py.press('tab')

# descricao()

# # LOJA DE ENGENHO

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.engenho')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('julio cezar')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo('Engenho')

# for x in range(2):
#     py.press('tab')

# descricao()

# # LOJA DE MESQUITA

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.mesquita')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('robertos')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo('Mesquita')

# for x in range(2):
#     py.press('tab')

# descricao()

# # LOJA DE VALVERDE

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.valverde')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('robertos')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo('Valverde')

# for x in range(2):
#     py.press('tab')

# descricao()


# # LOJA DE BARRETO

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.barreto')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('julio cezar')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo('Barreto')

# for x in range(2):
#     py.press('tab')

# descricao()

# # LOJA DE NOVA AMÉRICA

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.novaam')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('robertos')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo('Nova América')

# for x in range(2):
#     py.press('tab')

# descricao()

# # LOJA DE INHAUMA

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.inhauma')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('robertos')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo("Inhaúma")
# for x in range(2):
#     py.press('tab')

# descricao()

# # LOJA DE CURTUME

# # transforma o generator em lista
# botoes = list(py.locateAllOnScreen('f.png', confidence=0.9))

# if len(botoes) > 0:
#     # pega o primeiro elemento da lista
#     primeiro = botoes[0]
    
#     # clica no botão
#     py.click(primeiro)


# py.write('gerencia.curtume')

# py.press('enter')

# py.write('savio ')

# py.press('enter')

# py.write('robertos')

# py.press('enter')

# py.write('thiago.bon')

# py.press('enter')

# # transforma o generator em lista
# assunto = list(py.locateAllOnScreen('assunto.png', confidence=0.9))

# if len(assunto) > 0:
#     # pega o primeiro elemento da lista
#     segundo = assunto[0]
    
#     # clica no botão
#     py.click(segundo)

# titulo('Curtume')

# for x in range(2):
#     py.press('tab')

# descricao()






