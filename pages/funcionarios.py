import streamlit as st

from crud import (
    cadastrar_funcionario,
    buscar_funcionario_por_cpf,
    atualizar_funcionario,
    excluir_funcionario
)

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

    cpf_busca = st.text_input(
        "CPF",
        key="busca_funcionario"
    )

    if st.button("Buscar Funcionário"):

        funcionario = buscar_funcionario_por_cpf(
            cpf_busca
        )

        if funcionario:
            st.write(funcionario)
        else:
            st.error("Funcionário não encontrado.")

with aba_atualizacao:

    st.subheader("Atualizar Funcionário")

    cpf_antigo = st.text_input(
        "CPF do Funcionário",
        key="cpf_antigo_func"
    )

    novo_nome = st.text_input(
        "Novo Nome"
    )

    novo_cpf = st.text_input(
        "Novo CPF"
    )

    novo_telefone = st.text_input(
        "Novo Telefone"
    )

    novo_cargo = st.selectbox(
        "Novo Cargo",
        [
            "Frentista",
            "Frentista Gerente",
            "Dono do Posto"
        ],
        key="cargo_update"
    )

    nova_data = st.date_input(
        "Nova Data de Admissão",
        key="data_update"
    )

    if st.button("Atualizar Funcionário"):

        sucesso, mensagem = atualizar_funcionario(
            cpf_antigo,
            novo_nome,
            novo_cpf,
            novo_telefone,
            novo_cargo,
            str(nova_data)
        )

        if sucesso:
            st.success(mensagem)
        else:
            st.error(mensagem)
with aba_exclusao:

    st.subheader("Excluir Funcionário")

    cpf_exclusao = st.text_input(
        "CPF do Funcionário",
        key="cpf_excluir_func"
    )

    confirmar = st.checkbox(
        "Confirmo a exclusão"
    )

    if st.button("Excluir Funcionário"):

        if not confirmar:
            st.warning(
                "Confirme a exclusão."
            )
        else:

            sucesso, mensagem = excluir_funcionario(
                cpf_exclusao
            )

            if sucesso:
                st.success(mensagem)
            else:
                st.error(mensagem)