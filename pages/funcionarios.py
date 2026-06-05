import streamlit as st

st.title("👨‍💼 Gerenciamento de Funcionários")

aba_cadastro, aba_listagem, aba_busca, aba_atualizacao, aba_exclusao = st.tabs(
    [
        "Cadastro",
        "Listagem",
        "Busca",
        "Atualização",
        "Exclusão"
    ]
)

with aba_cadastro:
    st.subheader("Cadastrar Funcionário")

with aba_listagem:
    st.subheader("Listar Funcionários")

with aba_busca:
    st.subheader("Buscar Funcionário")

with aba_atualizacao:
    st.subheader("Atualizar Funcionário")

with aba_exclusao:
    st.subheader("Excluir Funcionário")