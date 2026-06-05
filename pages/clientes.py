import streamlit as st
from crud import cadastrar_cliente
from dados import clientes

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


# Aba de cadastro de clientes
with aba_cadastro:

    st.subheader("Cadastrar Cliente")

    with st.form("form_cliente"):

        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        telefone = st.text_input("Telefone")

        cadastrar = st.form_submit_button("Cadastrar Cliente")

        if cadastrar:

            sucesso, mensagem = cadastrar_cliente(
                nome,
                cpf,
                telefone
            )

            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)


# Aba listagem de clientes
with aba_listagem:

    st.subheader("Lista de Clientes")

    if clientes:
        st.table(clientes)
    else:
        st.info("Nenhum cliente cadastrado.")

# Aba de busca de clientes
with aba_busca:
    st.subheader("Buscar Cliente")

# Aba de atualização de clientes

with aba_atualizacao:
    st.subheader("Atualizar Cliente")

# Aba de exclusão de clientes
with aba_exclusao:
    st.subheader("Excluir Cliente")