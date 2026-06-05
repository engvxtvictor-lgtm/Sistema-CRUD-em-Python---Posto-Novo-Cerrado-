import streamlit as st
from crud import cadastrar_funcionario
from dados import funcionarios

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

    with st.form("form_funcionario"):

        nome = st.text_input("Nome")

        cpf = st.text_input("CPF")

        telefone = st.text_input("Telefone")

        cargo = st.selectbox(
            "Cargo",
            [
                "Frentista",
                "Frentista Gerente",
                "Dono do Posto"
            ]
        )

        data_admissao = st.date_input(
            "Data de Admissão"
        )

        cadastrar = st.form_submit_button(
            "Cadastrar Funcionário"
        )

        if cadastrar:

            sucesso, mensagem = cadastrar_funcionario(
                nome,
                cpf,
                telefone,
                cargo,
                str(data_admissao)
            )

            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)

with aba_listagem:

    st.subheader("Lista de Funcionários")

    if funcionarios:
        st.table(funcionarios)
    else:
        st.info("Nenhum funcionário cadastrado.")

with aba_busca:
    st.subheader("Buscar Funcionário")

with aba_atualizacao:
    st.subheader("Atualizar Funcionário")

with aba_exclusao:
    st.subheader("Excluir Funcionário")