from dados import clientes, combustiveis, vendas, cpfs, tipos_combustivel
from utils import (
    gerar_id,
    validar_cpf,
    buscar_por_cpf,
    buscar_por_id,
    gerar_registros,
    ler_float,
    ler_int
)


# BUG CORRIGIDO:
# Antes, o programa quebrava se o usuário digitasse letras em campos numéricos.
# A correção foi usar try/except nas funções ler_float() e ler_int().


def cadastrar_cliente():
    """Cadastra um cliente."""
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()

    if not nome or not validar_cpf(cpf):
        print("Dados inválidos.")
        return

    if cpf in cpfs:
        print("CPF já cadastrado.")
        return

    clientes.append({
        "id": gerar_id(clientes),
        "nome": nome,
        "cpf": cpf
    })

    cpfs.add(cpf)
    print("Cliente cadastrado.")


def listar_clientes():
    """Lista clientes."""
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    for cliente in gerar_registros(clientes):
        print(f"{cliente['id']} | {cliente['nome']} | {cliente['cpf']}")


def buscar_cliente():
    """Busca cliente por CPF."""
    cpf = input("CPF: ").strip()
    cliente = buscar_por_cpf(clientes, cpf)
    print(cliente if cliente else "Cliente não encontrado.")


def atualizar_cliente():
    """Atualiza o nome do cliente."""
    cpf = input("CPF: ").strip()
    cliente = buscar_por_cpf(clientes, cpf)

    if not cliente:
        print("Cliente não encontrado.")
        return

    novo_nome = input("Novo nome: ").strip()

    if not novo_nome:
        print("Nome inválido.")
        return

    cliente["nome"] = novo_nome
    print("Cliente atualizado.")


def excluir_cliente():
    """Exclui um cliente."""
    cpf = input("CPF: ").strip()
    cliente = buscar_por_cpf(clientes, cpf)

    if not cliente:
        print("Cliente não encontrado.")
        return

    if input("Confirmar exclusão? (s/n): ").lower() == "s":
        clientes.remove(cliente)
        cpfs.discard(cpf)
        print("Cliente excluído.")


def cadastrar_combustivel():
    """Cadastra combustível."""
    for i, tipo in enumerate(tipos_combustivel, start=1):
        print(f"{i} - {tipo}")

    opcao = ler_int("Tipo: ")

    if opcao < 1 or opcao > len(tipos_combustivel):
        print("Tipo inválido.")
        return

    preco = ler_float("Preço por litro: ")
    estoque = ler_float("Estoque em litros: ")
    nome = tipos_combustivel[opcao - 1]

    combustiveis.append({
        "id": gerar_id(combustiveis),
        "nome": nome,
        "sigla": nome[:3],
        "preco": preco,
        "estoque": estoque
    })

    print("Combustível cadastrado.")


def listar_combustiveis():
    """Lista combustíveis."""
    if not combustiveis:
        print("Nenhum combustível cadastrado.")
        return

    for item in combustiveis:
        print(
            f"{item['id']} | {item['nome']} | {item['sigla']} | "
            f"R$ {item['preco']:.2f} | {item['estoque']} L"
        )


def registrar_venda():
    """Registra uma venda."""
    if not clientes or not combustiveis:
        print("Cadastre cliente e combustível primeiro.")
        return

    listar_clientes()
    id_cliente = ler_int("ID do cliente: ")
    cliente = buscar_por_id(clientes, id_cliente)

    listar_combustiveis()
    id_combustivel = ler_int("ID do combustível: ")
    combustivel = buscar_por_id(combustiveis, id_combustivel)

    if not cliente or not combustivel:
        print("Cliente ou combustível não encontrado.")
        return

    litros = ler_float("Litros vendidos: ")

    if litros <= 0 or litros > combustivel["estoque"]:
        print("Venda inválida.")
        return

    total = litros * combustivel["preco"]
    combustivel["estoque"] -= litros

    vendas.append({
        "id": gerar_id(vendas),
        "cliente": cliente["nome"],
        "combustivel": combustivel["nome"],
        "litros": litros,
        "total": total
    })

    print(f"Venda registrada. Total: R$ {total:.2f}")


def listar_vendas():
    """Lista vendas."""
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    for venda in vendas:
        print(
            f"{venda['id']} | {venda['cliente']} | "
            f"{venda['combustivel']} | {venda['litros']} L | "
            f"R$ {venda['total']:.2f}"
        )


def relatorio():
    """Mostra relatório de vendas e estoque."""
    estoque_baixo = [
        item for item in combustiveis
        if item["estoque"] <= 100
    ]

    resumo_estoque = {
        item["nome"]: item["estoque"]
        for item in combustiveis
    }

    total_vendas = sum(venda["total"] for venda in vendas)

    print("\nResumo de estoque:")
    print(resumo_estoque)

    print("\nEstoque baixo:")
    print(estoque_baixo if estoque_baixo else "Nenhum.")

    print(f"\nTotal vendido: R$ {total_vendas:.2f}")