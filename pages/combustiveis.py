import streamlit as st
from utils import verificar_cargo
from crud import (
    cadastrar_combustivel,
    buscar_combustivel_por_nome,
    atualizar_combustivel,
    excluir_combustivel
)

from dados import combustiveis, combustiveis_tipos

st.title(" Combustíveis")
verificar_cargo(st, ["Dono do Posto", "Frentista Gerente"]
)
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

    st.subheader("Cadastrar Combustível")

    with st.form("form_combustivel"):

        nome = st.selectbox(
            "Tipo de combustível",
            combustiveis_tipos
        )

        preco_litro = st.text_input("Preço por litro")

        fornecedor = st.text_input("Fornecedor")

        estoque = st.text_input("Quantidade em estoque")

        cadastrar = st.form_submit_button("Cadastrar Combustível")

        if cadastrar:

            sucesso, mensagem = cadastrar_combustivel(
                nome,
                preco_litro,
                fornecedor,
                estoque
            )

            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)

with aba_listagem:

    st.subheader("Lista de Combustíveis")

    if combustiveis:
        st.table(combustiveis)
    else:
        st.info("Nenhum combustível cadastrado.")

with aba_busca:

    st.subheader("Buscar Combustível")

    nome_busca = st.selectbox(
        "Combustível",
        combustiveis_tipos,
        key="busca_combustivel"
    )

    if st.button("Buscar Combustível"):

        combustivel = buscar_combustivel_por_nome(nome_busca)

        if combustivel:
            st.write(combustivel)
        else:
            st.error("Combustível não encontrado.")

with aba_atualizacao:

    st.subheader("Atualizar Combustível")

    nome_antigo = st.selectbox(
        "Combustível atual",
        combustiveis_tipos,
        key="combustivel_antigo"
    )

    novo_nome = st.selectbox(
        "Novo combustível",
        combustiveis_tipos,
        key="novo_combustivel"
    )

    novo_preco = st.text_input(
        "Novo preço por litro",
        key="novo_preco"
    )

    novo_fornecedor = st.text_input(
        "Novo fornecedor",
        key="novo_fornecedor"
    )

    novo_estoque = st.text_input(
        "Novo estoque",
        key="novo_estoque"
    )

    if st.button("Atualizar Combustível"):

        sucesso, mensagem = atualizar_combustivel(
            nome_antigo,
            novo_nome,
            novo_preco,
            novo_fornecedor,
            novo_estoque
        )

        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)

with aba_exclusao:

    st.subheader("Excluir Combustível")

    nome_exclusao = st.selectbox(
        "Combustível",
        combustiveis_tipos,
        key="excluir_combustivel"
    )

    confirmar = st.checkbox(
        "Confirmo que desejo excluir este combustível"
    )

    if st.button("Excluir Combustível"):

        if not confirmar:
            st.warning("Marque a confirmação para excluir.")
        else:

            sucesso, mensagem = excluir_combustivel(nome_exclusao)

            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)