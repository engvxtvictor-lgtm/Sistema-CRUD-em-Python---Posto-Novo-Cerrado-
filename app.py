import streamlit as st

from dados import funcionarios
from crud import buscar_funcionario_por_cpf

st.set_page_config(
    page_title="Posto Novo Cerrado",
    layout="wide"
)

st.write(funcionarios)

if "usuario_logado" not in st.session_state:
    st.session_state.usuario_logado = None

if st.session_state.usuario_logado is None:
    st.subheader("Login")

    cpf = st.text_input("Digite seu CPF")

    if st.button("Entrar"):
        funcionario = buscar_funcionario_por_cpf(cpf)

        if funcionario:
            st.session_state.usuario_logado = funcionario
            st.success(f"Bem-vindo, {funcionario['nome']}!")
            st.rerun()
        else:
            st.error("CPF não encontrado.")

else:
    usuario = st.session_state.usuario_logado

    st.success(
        f"Usuário logado: {usuario['nome']} | Cargo: {usuario['cargo']}"
    )

    if st.button("Sair"):
        st.session_state.usuario_logado = None
        st.rerun()

    st.write("Selecione uma página no menu lateral.")