import streamlit as st

# Título da página
st.title("👥 Gerenciamento de Clientes")

# Criação das abas
aba_cadastro, aba_listagem, aba_busca, aba_atualizacao, aba_exclusao = st.tabs(
    [
        "Cadastro",
        "Listagem",
        "Busca",
        "Atualização",
        "Exclusão"
    ]
)

# Conteúdo temporário de cada aba
with aba_cadastro:
    st.subheader("Cadastrar Cliente")

with aba_listagem:
    st.subheader("Listar Clientes")

with aba_busca:
    st.subheader("Buscar Cliente")

with aba_atualizacao:
    st.subheader("Atualizar Cliente")

with aba_exclusao:
    st.subheader("Excluir Cliente")