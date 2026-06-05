from dados import (
    clientes,
    funcionarios,
    combustiveis,
    bombas,
    vendas,
    cpfs_cadastrados
)

from utils import (
    gerar_id,
    validar_cpf,
    validar_telefone,
    validar_vazio,
    cpf_ja_existe
)
# CLIENTES

def cadastrar_cliente(nome, cpf, telefone):

    if not validar_vazio(nome):
        return False, "O nome não pode estar vazio."

    if not validar_cpf(cpf):
        return False, "CPF inválido."

    if cpf_ja_existe(cpf):
        return False, "CPF já cadastrado."

    if not validar_telefone(telefone):
        return False, "Telefone inválido."

    novo_cliente = {
        "id": gerar_id(clientes),
        "nome": nome.strip(),
        "cpf": cpf,
        "telefone": telefone
    }

    clientes.append(novo_cliente)
    cpfs_cadastrados.add(cpf)

    return True, "Cliente cadastrado com sucesso!"


def buscar_cliente_por_cpf(cpf):

    for cliente in clientes:

        if cliente["cpf"] == cpf:
            return cliente

    return None


def atualizar_cliente(
    cpf_antigo,
    novo_nome,
    novo_cpf,
    novo_telefone
):

    cliente = buscar_cliente_por_cpf(cpf_antigo)

    if not cliente:
        return False, "Cliente não encontrado."

    if not validar_vazio(novo_nome):
        return False, "Nome inválido."

    if not validar_cpf(novo_cpf):
        return False, "CPF inválido."

    if not validar_telefone(novo_telefone):
        return False, "Telefone inválido."

    if novo_cpf != cpf_antigo and cpf_ja_existe(novo_cpf):
        return False, "CPF já cadastrado."

    cpfs_cadastrados.discard(cliente["cpf"])

    cliente["nome"] = novo_nome
    cliente["cpf"] = novo_cpf
    cliente["telefone"] = novo_telefone

    cpfs_cadastrados.add(novo_cpf)

    return True, "Cliente atualizado com sucesso!"


def excluir_cliente(cpf):

    cliente = buscar_cliente_por_cpf(cpf)

    if not cliente:
        return False, "Cliente não encontrado."

    clientes.remove(cliente)

    cpfs_cadastrados.discard(cpf)

    return True, "Cliente excluído com sucesso!"

# FUNCIONÁRIOS

def cadastrar_funcionario(
    nome,
    cpf,
    telefone,
    cargo,
    data_admissao
):

    if not validar_vazio(nome):
        return False, "Nome inválido."

    if not validar_cpf(cpf):
        return False, "CPF inválido."

    if cpf_ja_existe(cpf):
        return False, "CPF já cadastrado."

    if not validar_telefone(telefone):
        return False, "Telefone inválido."

    novo_funcionario = {
        "id": gerar_id(funcionarios),
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "cargo": cargo,
        "data_admissao": data_admissao
    }

    funcionarios.append(novo_funcionario)

    cpfs_cadastrados.add(cpf)

    return True, "Funcionário cadastrado com sucesso!"


def buscar_funcionario_por_cpf(cpf):

    for funcionario in funcionarios:

        if funcionario["cpf"] == cpf:
            return funcionario

    return None


def atualizar_funcionario(
    cpf_antigo,
    novo_nome,
    novo_cpf,
    novo_telefone,
    novo_cargo,
    nova_data_admissao
):

    funcionario = buscar_funcionario_por_cpf(cpf_antigo)

    if not funcionario:
        return False, "Funcionário não encontrado."

    if not validar_vazio(novo_nome):
        return False, "Nome inválido."

    if not validar_cpf(novo_cpf):
        return False, "CPF inválido."

    if not validar_telefone(novo_telefone):
        return False, "Telefone inválido."

    if novo_cpf != cpf_antigo and cpf_ja_existe(novo_cpf):
        return False, "CPF já cadastrado."

    cpfs_cadastrados.discard(funcionario["cpf"])

    funcionario["nome"] = novo_nome
    funcionario["cpf"] = novo_cpf
    funcionario["telefone"] = novo_telefone
    funcionario["cargo"] = novo_cargo
    funcionario["data_admissao"] = nova_data_admissao

    cpfs_cadastrados.add(novo_cpf)

    return True, "Funcionário atualizado com sucesso!"


def excluir_funcionario(cpf):

    funcionario = buscar_funcionario_por_cpf(cpf)

    if not funcionario:
        return False, "Funcionário não encontrado."

    funcionarios.remove(funcionario)

    cpfs_cadastrados.discard(cpf)

    return True, "Funcionário excluído com sucesso!"


# COMBUSTÍVEIS

def cadastrar_combustivel(
    nome,
    preco_litro,
    fornecedor,
    estoque,
    ultimo_abastecimento,
    quantidade_ultimo_abastecimento
):

    try:
        preco_litro = float(preco_litro)
        estoque = float(estoque)
        quantidade_ultimo_abastecimento = float(
            quantidade_ultimo_abastecimento
        )

    except ValueError:
        return False, "Valores numéricos inválidos."

    novo_combustivel = {
        "id": gerar_id(combustiveis),
        "nome": nome,
        "preco_litro": preco_litro,
        "fornecedor": fornecedor,
        "estoque": estoque,
        "ultimo_abastecimento": ultimo_abastecimento,
        "quantidade_ultimo_abastecimento":
            quantidade_ultimo_abastecimento
    }

    combustiveis.append(
        novo_combustivel
    )

    return True, "Combustível cadastrado com sucesso."


def buscar_combustivel(nome):

    for combustivel in combustiveis:

        if combustivel["nome"] == nome:
            return combustivel

    return None


def atualizar_combustivel(
    nome_antigo,
    novo_nome,
    novo_preco_litro,
    novo_fornecedor,
    novo_estoque,
    novo_ultimo_abastecimento,
    nova_quantidade_ultimo_abastecimento
):

    combustivel = buscar_combustivel(nome_antigo)

    if not combustivel:
        return False, "Combustível não encontrado."

    try:
        novo_preco_litro = float(novo_preco_litro)
        novo_estoque = float(novo_estoque)
        nova_quantidade_ultimo_abastecimento = float(
            nova_quantidade_ultimo_abastecimento
        )

    except ValueError:
        return False, "Valores numéricos inválidos."

    combustivel["nome"] = novo_nome
    combustivel["preco_litro"] = novo_preco_litro
    combustivel["fornecedor"] = novo_fornecedor
    combustivel["estoque"] = novo_estoque
    combustivel["ultimo_abastecimento"] = novo_ultimo_abastecimento
    combustivel["quantidade_ultimo_abastecimento"] = (
        nova_quantidade_ultimo_abastecimento
    )

    return True, "Combustível atualizado com sucesso."


def excluir_combustivel(nome):

    combustivel = buscar_combustivel(nome)

    if not combustivel:
        return False, "Combustível não encontrado."

    combustiveis.remove(combustivel)

    return True, "Combustível removido com sucesso."


# BOMBAS

def cadastrar_bomba(
    numero,
    tipo_combustivel,
    status
):

    if not validar_vazio(str(numero)):
        return False, "Número da bomba inválido."

    for bomba in bombas:
        if bomba["numero"] == numero:
            return False, "Número de bomba já cadastrado."

    nova_bomba = {
        "id": gerar_id(bombas),
        "numero": numero,
        "tipo_combustivel": tipo_combustivel,
        "status": status
    }

    bombas.append(nova_bomba)

    return True, "Bomba cadastrada com sucesso."


def buscar_bomba_por_numero(numero):

    for bomba in bombas:

        if bomba["numero"] == numero:
            return bomba

    return None


def atualizar_bomba(
    numero_antigo,
    novo_numero,
    novo_tipo_combustivel,
    novo_status
):

    bomba = buscar_bomba_por_numero(numero_antigo)

    if not bomba:
        return False, "Bomba não encontrada."

    if novo_numero != numero_antigo:
        for b in bombas:
            if b["numero"] == novo_numero:
                return False, "Número de bomba já cadastrado."

    bomba["numero"] = novo_numero
    bomba["tipo_combustivel"] = novo_tipo_combustivel
    bomba["status"] = novo_status

    return True, "Bomba atualizada com sucesso."


def excluir_bomba(numero):

    bomba = buscar_bomba_por_numero(numero)

    if not bomba:
        return False, "Bomba não encontrada."

    bombas.remove(bomba)

    return True, "Bomba excluída com sucesso."


# VENDAS

def registrar_venda(
    cpf_cliente,
    cpf_funcionario,
    numero_bomba,
    tipo_combustivel,
    litros,
    forma_pagamento,
    data_venda
):

    try:
        litros = float(litros)

    except ValueError:
        return False, "Quantidade de litros inválida."

    if litros <= 0:
        return False, "A quantidade de litros deve ser maior que zero."

    combustivel = buscar_combustivel(tipo_combustivel)

    if not combustivel:
        return False, "Combustível não encontrado."

    if combustivel["estoque"] < litros:
        return False, "Estoque insuficiente para esta venda."

    valor_total = round(litros * combustivel["preco_litro"], 2)

    nova_venda = {
        "id": gerar_id(vendas),
        "cpf_cliente": cpf_cliente,
        "cpf_funcionario": cpf_funcionario,
        "numero_bomba": numero_bomba,
        "tipo_combustivel": tipo_combustivel,
        "litros": litros,
        "valor_total": valor_total,
        "forma_pagamento": forma_pagamento,
        "data_venda": data_venda
    }

    vendas.append(nova_venda)

    combustivel["estoque"] = round(
        combustivel["estoque"] - litros, 2
    )

    return True, f"Venda registrada com sucesso! Total: R$ {valor_total:.2f}"


def listar_vendas_por_data(data_inicio, data_fim):

    resultado = []

    for venda in vendas:

        if data_inicio <= venda["data_venda"] <= data_fim:
            resultado.append(venda)

    return resultado


def calcular_total_vendas():

    total = 0.0

    for venda in vendas:
        total += venda["valor_total"]

    return round(total, 2)


def calcular_total_por_combustivel():

    totais = {}

    for venda in vendas:

        tipo = venda["tipo_combustivel"]

        if tipo not in totais:
            totais[tipo] = {"litros": 0.0, "valor": 0.0}

        totais[tipo]["litros"] = round(
            totais[tipo]["litros"] + venda["litros"], 2
        )
        totais[tipo]["valor"] = round(
            totais[tipo]["valor"] + venda["valor_total"], 2
        )

    return totais