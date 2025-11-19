import pandas as pd
import streamlit as st
import numpy as np


st.set_page_config(
    page_title="Controle",
    page_icon="🛒", # Use um emoji ou caminho de arquivo de imagem
    layout="wide"
)


df = pd.read_excel(r"C:\Users\wallace.souza\Downloads\Produto Abaixo de 6 dias.xlsx")

df["DATA"] = df["DATA"].dt.strftime("%d/%m/%Y")

# Páginas do sidebar
pagina = st.sidebar.radio("Ir para", ["Produtos", "Ajuste de Parâmetro", "Score Card"])

if pagina == "Produtos":
    #Título
    st.title("Produtos abaixo de 6 dias")

    # Filtro de Seleção

    st.sidebar.title("Filtros")

    lojas = st.sidebar.multiselect("Selecione a Loja",df["LOJA"].sort_values().unique(), default=df["LOJA"].sort_values().unique(),placeholder="Escolha opções")

    datas = st.sidebar.multiselect("Selecione a Data", df["DATA"].sort_values().unique(), default=[],placeholder="Escolha opções")


    #Aplicando Filtros

    filtro = df[(df["LOJA"].isin(lojas)) & (df["DATA"].isin(datas))]



    produtos_por_loja = filtro.groupby("LOJA")["SEQPRODUTO"].count().reset_index()

    #Contagem da loja
    itens = len(filtro)

    st.bar_chart(produtos_por_loja, x = "LOJA", y="SEQPRODUTO")


    # Dataframe
    st.dataframe(filtro,use_container_width=True)
    st.metric("Total de Produtos", itens)

#####################################################################################################

#Ajuste de pârametro

elif pagina == "Ajuste de Parâmetro":
    arquivo = st.file_uploader("Envie o Arquivo Excel", type=["xlsx"])

    if arquivo is not None:
        abs = pd.read_excel(arquivo, sheet_name=0)
        abs1 = pd.read_excel(arquivo, sheet_name=1)
        abs2 = pd.read_excel(arquivo, sheet_name=2)

        # --- Ajustes iniciais ---
        abs['CURVA ATUAL'] = abs['CURVA ATUAL'].replace(0, 'C')

        def dias_cobertura(x):
            x['DIAS COBERT MÍNIMO'] = x['CURVA ATUAL'].apply(lambda curva: 7 if curva == 'A' else (12 if curva == 'B' else 15))
            x['DIAS COBERT MÁXIMO'] = x['CURVA ATUAL'].apply(lambda curva: 10 if curva == 'A' else (15 if curva == 'B' else 20))
            return x

        # Merge com abs1
        abs = abs.merge(abs1, on='SEQPRODUTO', how='left')
        abs = abs[abs['SETOR'] == 'MERCEARIA']

        abs = abs.sort_values(by=['LOJA', 'DESCRICAO PRODUTO', 'FRENTE'], ascending=[True, True, False])
        abs = abs.drop_duplicates(subset=['LOJA', 'DESCRICAO PRODUTO'], keep='first')

        abs = abs[['LOJA', 'SEQPRODUTO','UNID', 'FRENTE', 'TOTAL UND','CURVA ATUAL', 'QTD ESTQ MÍNIMO','QTD ESTQ MÁXIMO']]

        abs['QTD ESTQ MÁXIMO'] = abs['UNID']
        abs['QTD ESTQ MÍNIMO'] = abs['TOTAL UND']
        abs['DIAS COBERT MÍNIMO'] = np.nan
        abs['DIAS COBERT MÁXIMO'] = np.nan

        # Merge com abs2
        abs = abs.merge(abs2, left_on=['LOJA','SEQPRODUTO'], right_on=['Empresa','Cód. Produto'], how='left')
        abs = abs.drop_duplicates(subset=['LOJA', 'SEQPRODUTO'], keep='first')

        # Aplica regra de cobertura
        abs = dias_cobertura(abs)

        # Filtro final
        abs = abs[['LOJA', 'SEQPRODUTO','QTD ESTQ MÍNIMO', 'QTD ESTQ MÁXIMO','DIAS COBERT MÍNIMO','DIAS COBERT MÁXIMO']]
        abs = abs[~abs['SEQPRODUTO'].isin([41102,1257,3938,31013,52])]

        # Renomear colunas
        abs.columns = ['LOJA', 'SEQPRODUTO', 'QTD ESTQ MINIMO', 'QTD ESTQ MAXIMO','DIAS COBERT MINIMO', 'DIAS COBERT MAXIMO']

        # Mostrar resultado
        st.success("Arquivo processado com sucesso!")
        st.dataframe(abs, use_container_width=True)

        # Botão para download
        csv = abs.to_csv(index=False, sep=";").encode("utf-8")
        st.download_button(
            label="⬇️ Baixar Ajuste de Parâmetro",
            data=csv,
            file_name="Ajuste_de_Parametro.csv",
            mime="text/csv"
        )
####################################################################################################################

#Score Card

elif pagina == "Score Card":
    st.title("Score Card")
    sc = pd.read_excel(r"C:\Users\wallace.souza\Desktop\Score card\Premiação Geral.xlsx")
    sc["LOJA"] = sc["LOJA"].str.upper().str.strip()

    sc_meses = ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"]

    sc["MÊS"] = pd.Categorical(sc["MÊS"], categories=sc_meses, ordered=True)

    sc = sc.sort_values(["ANO", "MÊS"])
    

    sc_ano = st.sidebar.multiselect("Selecione o Ano", sc["ANO"].unique(), placeholder="Escolha Opções")

    ft = sc.copy()

    if sc_ano:
        ft = ft[ft["ANO"].isin(sc_ano)]

    sc_mes = st.sidebar.multiselect("Selecione o Mês", ft["MÊS"].unique(),placeholder="Escolha Opções")

    if sc_mes:
        ft = ft[ft["MÊS"].isin(sc_mes)]

    sc_setor = st.sidebar.multiselect("Selecione o Setor", ft["SETOR"].unique(),placeholder="Escolha Opções")

    if sc_setor:
        ft = ft[ft["SETOR"].isin(sc_setor)]  
    
    
    ft1 = ft.groupby("LOJA", as_index=False)["NOME DO RECEBEDOR"].count()
    ft1 = ft1.rename(columns={"NOME DO RECEBEDOR": "QUANTIDADE"})

    qtd = len(ft)
   
    st.bar_chart(ft1,x="LOJA", y="QUANTIDADE")

    st.dataframe(ft)   
    st.metric("Quantidade", qtd)

    sc["teste"] = np.nan    
    
    qtd_2024 = sc.loc[sc["ANO"] == 2024, "teste"].values[0]
    qtd_2025 = sc.loc[sc["ANO"] == 2025, "teste"].values[0]

    # Calculando o crescimento percentual
    crescimento = ((qtd_2025 - qtd_2024) / qtd_2024) * 100

    # Exibindo no Streamlit
    st.metric(
        label="Crescimento Quantidade 2024 vs 2025",
        value=f"{qtd_2025}",           # valor atual
        delta=f"{crescimento:.2f}%"    # diferença em %
)




    

    




  



            









