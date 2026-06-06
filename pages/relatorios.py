import streamlit as st
from utils import verificar_cargo

from dados import clientes, funcionarios, combustiveis, vendas

st.title("Relatórios")
verificar_cargo(st, ["Dono do Posto", "Frentista Gerente"])
aba_geral, aba_estoque, aba_vendas = st.tabs(
    [
        "Geral",
        "Estoque",
        "Vendas"
    ]
)

with aba_geral:

    st.subheader("Resumo Geral")

    st.write(f"Clientes cadastrados: {len(clientes)}")
    st.write(f"Funcionários cadastrados: {len(funcionarios)}")
    st.write(f"Combustíveis cadastrados: {len(combustiveis)}")
    st.write(f"Vendas registradas: {len(vendas)}")


with aba_estoque:

    st.subheader("Relatório de Estoque")

    if combustiveis:

        estoque_classificado = []

        for combustivel in combustiveis:

            if combustivel["estoque"] <= 100:
                status = "Baixo"
            elif combustivel["estoque"] < 500:
                status = "Médio"
            else:
                status = "Alto"

            estoque_classificado.append(
                {
                    "Combustível": combustivel["nome"],
                    "Estoque": combustivel["estoque"],
                    "Status": status
                }
            )

        st.table(estoque_classificado)

    else:
        st.info("Nenhum combustível cadastrado.")


with aba_vendas:

    st.subheader("Relatório de Vendas")

    if vendas:

        total_vendido = sum(
            venda["valor_total"]
            for venda in vendas
        )

        total_litros = sum(
            venda["litros"]
            for venda in vendas
        )

        st.write(f"Total arrecadado: R$ {total_vendido:.2f}")
        st.write(f"Total de litros vendidos: {total_litros:.2f} L")
        st.write(f"Quantidade de vendas: {len(vendas)}")

        litros_por_combustivel = {}

        for venda in vendas:
            combustivel = venda["combustivel"]

            if combustivel not in litros_por_combustivel:
                litros_por_combustivel[combustivel] = 0

            litros_por_combustivel[combustivel] += venda["litros"]

        st.subheader("Litros vendidos por combustível")
        st.write(litros_por_combustivel)

        combustivel_mais_vendido = max(
            litros_por_combustivel,
            key=litros_por_combustivel.get
        )

        st.success(
            f"Combustível mais vendido: {combustivel_mais_vendido}"
        )

    else:
        st.info("Nenhuma venda registrada.")