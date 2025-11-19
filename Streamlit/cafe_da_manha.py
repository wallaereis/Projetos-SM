import pandas as pd
import streamlit as st
import numpy as np


df = pd.read_excel(r"C:\Users\wallace.souza\Downloads\Lista de Café da manha.xlsx")

st.title("Cadastro de Produtos")

# Inicializa o DataFrame apenas na primeira execução
if "df_final" not in st.session_state:
    st.session_state.df_final = pd.DataFrame(columns=["Produto", "Quantidade"])

# Seleções
produtos = st.multiselect(
    "Selecione o Produto",
    df['Produtos'],
    placeholder="Escolha opções"
)

quantidades = st.multiselect(
    "Selecione a Quantidade",
    [1, 2, 3, 4, 5],
    placeholder="Escolha quantidade"
)

# Botão de envio
if st.button("Enviar"):
    if len(produtos) == 0 or len(quantidades) == 0:
        st.error("Escolha pelo menos um produto e uma quantidade.")
    else:
        # Cria um mini-DataFrame apenas com o envio atual
        novo_registro = pd.DataFrame({
            "Produto": produtos,
            "Quantidade": quantidades[:len(produtos)]
        })

        # Adiciona ao DataFrame final
        st.session_state.df_final = pd.concat(
            [st.session_state.df_final, novo_registro],
            ignore_index=True
        )

        st.success("Informações adicionadas com sucesso!")

# Exibir o DataFrame final atualizado
st.write("📄 DataFrame Final:")
st.dataframe(st.session_state.df_final)


