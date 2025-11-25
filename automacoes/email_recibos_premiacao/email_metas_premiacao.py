import pyautogui as py
import time
import pyperclip

py.FAILSAFE = True
py.PAUSE = 0.5


def titulo(loja):
    # titulo =f'Recibos - Premiações de Novembro 2025 - {loja}'
    titulo =f"Planilha para a Criação das Metas de Venda - Dezembro 2025 - {loja}"
    pyperclip.copy(titulo)
    py.hotkey('ctrl', 'v')


def descricao():
    # descricao = "Bom dia,\n\nEncaminho em anexo os recibos correspondentes ao mês de Novembro.\n\nFico à disposição para quaisquer esclarecimentos que se fizerem necessários.\n\nAtenciosamente,"
    descricao = "Bom dia,\n\nSegue a planilha para sugestão de Meta de Venda do Mês de Dezembro 2025.\n\nAtenciosamente,"
    pyperclip.copy(descricao)
    py.hotkey('ctrl', 'v')

def arquivo(loja):
    caminho = fr"C:\Users\wallace.souza\Desktop\Definição Meta Dez25 - {loja}.xlsm"
    pyperclip.copy(caminho)
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

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Fonseca')

py.press('enter')

py.click(540,935)

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

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Piratininga')

py.press('enter')

py.click(540,935)

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


py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Itaipú')

py.press('enter')

py.click(540,935)

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

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Santa Cruz')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo("Lote XV")

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Lote XV')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo("Porto Novo")

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Porto Novo')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo('Batalha')

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Batalha')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo("Nova Iguaçú")

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Nova Iguaçú')


py.press('enter')

py.click(540,935)

py.press('tab')

descricao()


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

titulo("Porto Velho")

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Porto Velho')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo('Engenho')

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Engenho')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo('Mesquita')

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Mesquita')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo('Valverde')

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Valverde')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()


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

titulo('Barreto')

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Barreto')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo('Nova América')

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Nova América')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo("Inhaúma")
py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Inhaúma')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()

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

titulo('Curtume')

py.press('tab')
for x in range(2):
    py.press('enter')

arquivo('Curtume')

py.press('enter')

py.click(540,935)

py.press('tab')

descricao()






