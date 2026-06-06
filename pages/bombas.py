import streamlit as st

from crud import (
    cadastrar_bomba,
    buscar_bomba,
    atualizar_bomba,
    excluir_bomba
)

from dados import bombas, combustiveis_tipos

st.title("⛽ Bombas")

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

    st.subheader("Cadastrar Bomba")

    with st.form("form_bomba"):

        numero = st.number_input(
            "Número da bomba",
            min_value=1,
            step=1
        )

        combustivel = st.selectbox(
            "Combustível",
            combustiveis_tipos
        )

        status = st.selectbox(
            "Status",
            [
                "Ativa",
                "Em manutenção"
            ]
        )

        cadastrar = st.form_submit_button(
            "Cadastrar Bomba"
        )

        if cadastrar:

            sucesso, mensagem = cadastrar_bomba(
                numero,
                combustivel,
                status
            )

            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)

with aba_listagem:

    st.subheader("Lista de Bombas")

    if bombas:
        st.table(bombas)
    else:
        st.info("Nenhuma bomba cadastrada.")

with aba_busca:

    st.subheader("Buscar Bomba")

    numero = st.number_input(
        "Número",
        min_value=1,
        step=1,
        key="busca_bomba"
    )

    if st.button("Buscar Bomba"):

        bomba = buscar_bomba(numero)

        if bomba:
            st.write(bomba)
        else:
            st.error("Bomba não encontrada.")

with aba_atualizacao:

    st.subheader("Atualizar Bomba")

    numero_antigo = st.number_input(
        "Número atual",
        min_value=1,
        step=1,
        key="numero_antigo"
    )

    novo_numero = st.number_input(
        "Novo número",
        min_value=1,
        step=1,
        key="novo_numero"
    )

    novo_combustivel = st.selectbox(
        "Novo combustível",
        combustiveis_tipos,
        key="novo_comb_bomba"
    )

    novo_status = st.selectbox(
        "Novo status",
        [
            "Ativa",
            "Em manutenção"
        ],
        key="novo_status"
    )

    if st.button("Atualizar Bomba"):

        sucesso, mensagem = atualizar_bomba(
            numero_antigo,
            novo_numero,
            novo_combustivel,
            novo_status
        )

        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)

with aba_exclusao:

    st.subheader("Excluir Bomba")

    numero = st.number_input(
        "Número da bomba",
        min_value=1,
        step=1,
        key="excluir_bomba"
    )

    confirmar = st.checkbox(
        "Confirmo a exclusão"
    )

    if st.button("Excluir Bomba"):

        if not confirmar:
            st.warning("Confirme a exclusão.")
        else:

            sucesso, mensagem = excluir_bomba(numero)

            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)