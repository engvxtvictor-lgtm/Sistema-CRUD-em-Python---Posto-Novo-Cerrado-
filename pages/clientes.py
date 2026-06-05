import streamlit as st
from crud import (
    cadastrar_cliente,
    buscar_cliente_por_cpf,
    atualizar_cliente,
    excluir_cliente
)
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

    st.subheader("Buscar Cliente por CPF")

    cpf_busca = st.text_input(
        "Digite o CPF do cliente",
        key="cpf_busca"
    )

    if st.button("Buscar Cliente"):

        cliente = buscar_cliente_por_cpf(cpf_busca)

        if cliente:

            st.success("Cliente encontrado!")

            st.write(f"ID: {cliente['id']}")
            st.write(f"Nome: {cliente['nome']}")
            st.write(f"CPF: {cliente['cpf']}")
            st.write(f"Telefone: {cliente['telefone']}")

        else:
            st.error("Cliente não encontrado.")

# Aba de atualização de clientes

with aba_atualizacao:

    st.subheader("Atualizar Cliente")

    cpf_atual = st.text_input(
        "CPF do cliente",
        key="cpf_atualizacao"
    )

    novo_nome = st.text_input(
        "Novo nome",
        key="novo_nome"
    )

    novo_cpf = st.text_input(
        "Novo CPF",
        key="novo_cpf"
    )

    novo_telefone = st.text_input(
        "Novo telefone",
        key="novo_telefone"
    )

    if st.button("Atualizar Cliente"):

        sucesso, mensagem = atualizar_cliente(
            cpf_atual,
            novo_nome,
            novo_cpf,
            novo_telefone
        )

        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)

# Aba de exclusão de clientes
with aba_exclusao:

    st.subheader("Excluir Cliente")

    cpf_exclusao = st.text_input(
        "CPF do cliente",
        key="cpf_exclusao"
    )

    confirmar = st.checkbox(
        "Confirmo que desejo excluir este cliente"
    )

    if st.button("Excluir Cliente"):

        if not confirmar:
            st.warning("Marque a confirmação para excluir.")
        else:

            sucesso, mensagem = excluir_cliente(
                cpf_exclusao
            )

            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)
    
