import streamlit as st

from crud import registrar_venda

from dados import (
    clientes,
    funcionarios,
    combustiveis,
    bombas,
    vendas
)

st.title("Vendas")

aba_registro, aba_listagem = st.tabs(
    [
        "Registrar Venda",
        "Listagem"
    ]
)

with aba_registro:

    st.subheader("Registrar Venda")

    if not clientes:
        st.warning("Cadastre pelo menos um cliente antes de registrar vendas.")

    elif not funcionarios:
        st.warning("Cadastre pelo menos um funcionário antes de registrar vendas.")

    elif not combustiveis:
        st.warning("Cadastre pelo menos um combustível antes de registrar vendas.")

    elif not bombas:
        st.warning("Cadastre pelo menos uma bomba antes de registrar vendas.")

    else:

        with st.form("form_venda"):

            cpf_cliente = st.selectbox(
                "Cliente",
                [cliente["cpf"] for cliente in clientes]
            )

            cpf_funcionario = st.selectbox(
                "Funcionário",
                [funcionario["cpf"] for funcionario in funcionarios]
            )

            numero_bomba = st.selectbox(
                "Bomba",
                [bomba["numero"] for bomba in bombas]
            )

            combustivel_nome = st.selectbox(
                "Combustível",
                [combustivel["nome"] for combustivel in combustiveis]
            )

            litros = st.text_input("Quantidade de litros")

            registrar = st.form_submit_button("Registrar Venda")

            if registrar:

                sucesso, mensagem = registrar_venda(
                    cpf_cliente,
                    cpf_funcionario,
                    numero_bomba,
                    combustivel_nome,
                    litros
                )

                if sucesso:
                    st.success(mensagem)
                else:
                    st.error(mensagem)

with aba_listagem:

    st.subheader("Lista de Vendas")

    if vendas:
        st.table(vendas)
    else:
        st.info("Nenhuma venda registrada.")