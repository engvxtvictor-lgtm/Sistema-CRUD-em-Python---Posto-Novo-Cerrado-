import streamlit as st

st.title("Combustíveis")

aba_cadastro, aba_listagem = st.tabs(
    [
        "Cadastro",
        "Listagem"
    ]
)

with aba_cadastro:
    st.subheader("Cadastrar Combustível")

with aba_listagem:
    st.subheader("Lista de Combustíveis")