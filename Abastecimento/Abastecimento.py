import pandas as pd
import numpy as np

# Parâmetros de cada loja
abs = pd.read_excel(r"C:\Users\wallace.souza\Desktop\Scripts\Abastecimento\Parametro.xlsx")

# Planilha de cadastro para mesclar os produtos de mercearia

abs1 = pd.read_excel(r"C:\Users\wallace.souza\Desktop\Scripts\Abastecimento\Parametro.xlsx", sheet_name=1)

# Planiliha ponto extra

abs2 = pd.read_excel(r"C:\Users\wallace.souza\Desktop\Scripts\Abastecimento\Parametro.xlsx", sheet_name=2)


abs['CURVA ATUAL'] = abs['CURVA ATUAL'].replace(0, 'C')

def ajustar_quantidade(row):
    while (row['QTD ESTQ MÁXIMO'] <= row['QTD ESTQ MÍNIMO']).any():
        row.loc[row['QTD ESTQ MÁXIMO'] <= row['QTD ESTQ MÍNIMO'], 'QTD ESTQ MÁXIMO'] += row['UNID']

def ajustar_quantidade2(row2):
    while (row2['QTD ESTQ MÍNIMO'] < (row2['QTD ESTQ MÁXIMO'] - row2['QTD ESTQ MÍNIMO'])).any():
     row2.loc[row2['QTD ESTQ MÍNIMO'] < (row2['QTD ESTQ MÁXIMO'] - row2['QTD ESTQ MÍNIMO']), 'QTD ESTQ MÍNIMO'] += 1

def dias_cobertura(x):
  x['DIAS COBERT MÍNIMO'] = x['CURVA ATUAL'].apply(lambda curva: 7 if curva == 'A' else (12 if curva == 'B' else 15))
  x['DIAS COBERT MÁXIMO'] = x['CURVA ATUAL'].apply(lambda curva: 10 if curva == 'A' else (15 if curva == 'B' else 20))
  return x

abs = abs.merge(abs1, on='SEQPRODUTO', how='left')
abs = abs[abs['SETOR']=='MERCEARIA']

abs = abs.sort_values(by=['LOJA','DESCRICAO PRODUTO', 'FRENTE'], ascending=[True, True, False])
abs = abs.drop_duplicates(subset=['LOJA', 'DESCRICAO PRODUTO'], keep='first')

abs = abs[['LOJA', 'SEQPRODUTO','UNID', 'FRENTE', 'TOTAL UND','CURVA ATUAL', 'QTD ESTQ MÍNIMO',
       'QTD ESTQ MÁXIMO']]

abs ['QTD ESTQ MÁXIMO'] = abs['UNID']
abs['QTD ESTQ MÍNIMO'] = abs['TOTAL UND']
abs['DIAS COBERT MÍNIMO'] = abs['DIAS COBERT MÍNIMO'] = np.nan
abs['DIAS COBERT MÁXIMO'] = abs['DIAS COBERT MÁXIMO'] = np.nan

abs = abs.merge(abs2, left_on=['LOJA','SEQPRODUTO'] , right_on=['Empresa','Cód. Produto'], how='left')

abs = abs.drop_duplicates(subset=['LOJA', 'SEQPRODUTO'], keep='first')

abs['GONDULA + PONTA FONSECA'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==1] +  abs['MIN']
abs['GONDULA + PONTA PIRATININGA'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==3] +  abs['MIN']
abs['GONDULA + PONTA ITAIPU'] =abs['QTD ESTQ MÍNIMO'][abs['LOJA']==4] +  abs['MIN']
abs['GONDULA + PONTA SANTA CRUZ'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==8] +  abs['MIN']
abs['GONDULA + PONTA LOTE XV'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==10] +  abs['MIN']
abs['GONDULA + PONTA PORTO NOVO'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==11] + abs['MIN']
abs['GONDULA + PONTA BATALHA'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==12] +  abs['MIN']
abs['GONDULA + PONTA NOVA IGUAÇU'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==13] + abs['MIN']
abs['GONDULA + PONTA PORTO VELHO'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==15] + abs['MIN']
abs['GONDULA + PONTA ENGENHO'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==17] +  abs['MIN']
abs['GONDULA + PONTA MESQUITA'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==18] +  abs['MIN']
abs['GONDULA + PONTA VALVERDE'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==19] +  abs['MIN']
abs['GONDULA + PONTA BARRETO'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==21] +  abs['MIN']
abs['GONDULA + PONTA NOVA AMERICA'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==22] +  abs['MIN']
abs['GONDULA + PONTA INHAUMA'] =abs['QTD ESTQ MÍNIMO'][abs['LOJA']==23] +  abs['MIN']
abs['GONDULA + PONTA CURTUME'] = abs['QTD ESTQ MÍNIMO'][abs['LOJA']==24] + abs['MIN']

abs.loc[(abs['LOJA'] == 1) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA FONSECA']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA FONSECA']
abs.loc[(abs['LOJA'] == 3) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA PIRATININGA']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA PIRATININGA']
abs.loc[(abs['LOJA'] == 4) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA ITAIPU']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA ITAIPU']
abs.loc[(abs['LOJA'] == 8) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA SANTA CRUZ']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA SANTA CRUZ']
abs.loc[(abs['LOJA'] == 10) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA LOTE XV']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA LOTE XV']
abs.loc[(abs['LOJA'] == 11) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA PORTO NOVO']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA PORTO NOVO']
abs.loc[(abs['LOJA'] == 12) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA BATALHA']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA BATALHA']
abs.loc[(abs['LOJA'] == 13) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA NOVA IGUAÇU']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA NOVA IGUAÇU']
abs.loc[(abs['LOJA'] == 15) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA PORTO VELHO']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA PORTO VELHO']
abs.loc[(abs['LOJA'] == 17) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA ENGENHO']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA ENGENHO']
abs.loc[(abs['LOJA'] == 18) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA MESQUITA']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA MESQUITA']
abs.loc[(abs['LOJA'] == 19) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA VALVERDE']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA VALVERDE']
abs.loc[(abs['LOJA'] == 21) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA BARRETO']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA BARRETO']
abs.loc[(abs['LOJA'] == 22) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA NOVA AMERICA']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA NOVA AMERICA']
abs.loc[(abs['LOJA'] == 23) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA INHAUMA']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA INHAUMA']
abs.loc[(abs['LOJA'] == 24) & (abs['QTD ESTQ MÍNIMO'] < abs['GONDULA + PONTA CURTUME']), 'QTD ESTQ MÍNIMO'] = abs['GONDULA + PONTA CURTUME']

dias_cobertura(abs)
ajustar_quantidade(abs)


abs = abs[['LOJA', 'SEQPRODUTO','QTD ESTQ MÍNIMO', 'QTD ESTQ MÁXIMO', 'DIAS COBERT MÍNIMO',
       'DIAS COBERT MÁXIMO']]

abs = abs[~abs['SEQPRODUTO'].isin([17208,444,13759,41102,1257,3938,31013,52])]


abs.columns= [['LOJA', 'SEQPRODUTO', 'QTD_ESTQ_MINIMO', 'QTD_ESTQ_MAXIMO',
       'DIAS_COBERT_MINIMO', 'DIAS_COBERT_MAXIMO']]

abs.to_csv(r"C:\Users\wallace.souza\Downloads\Ajuste de Parâmetro.csv", sep=';', index=False)

