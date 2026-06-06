from dados import clientes, funcionarios, combustiveis, bombas,vendas, cpfs_cadastrados

from utils import (
    gerar_id,
    validar_cpf,
    validar_telefone,
    validar_vazio,
    cpf_ja_existe
)

def cadastrar_cliente(nome, cpf, telefone):
    #Cadastra um cliente

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
    #Busca cliente pelo CPF

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente

    return None


def atualizar_cliente(cpf_antigo, novo_nome, novo_cpf, novo_telefone):
    #Atualiza os dados de um cliente

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

    cliente["nome"] = novo_nome.strip()
    cliente["cpf"] = novo_cpf
    cliente["telefone"] = novo_telefone

    cpfs_cadastrados.add(novo_cpf)

    return True, "Cliente atualizado com sucesso!"


def excluir_cliente(cpf):
    #Exclui um cliente pelo CPF

    cliente = buscar_cliente_por_cpf(cpf)

    if not cliente:
        return False, "Cliente não encontrado."

    clientes.remove(cliente)
    cpfs_cadastrados.discard(cpf)

    return True, "Cliente excluído com sucesso!"

def cadastrar_funcionario(nome, cpf, telefone, cargo, data_admissao):
    #Cadastra um funcionário

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
        "nome": nome.strip(),
        "cpf": cpf,
        "telefone": telefone,
        "cargo": cargo,
        "data_admissao": data_admissao
    }

    funcionarios.append(novo_funcionario)
    cpfs_cadastrados.add(cpf)

    return True, "Funcionário cadastrado com sucesso!"


def buscar_funcionario_por_cpf(cpf):
    #Busca funcionário pelo CPF

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
    #Atualiza os dados de um funcionário

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

    funcionario["nome"] = novo_nome.strip()
    funcionario["cpf"] = novo_cpf
    funcionario["telefone"] = novo_telefone
    funcionario["cargo"] = novo_cargo
    funcionario["data_admissao"] = nova_data_admissao

    cpfs_cadastrados.add(novo_cpf)

    return True, "Funcionário atualizado com sucesso!"


def excluir_funcionario(cpf):
    #Exclui um funcionário pelo CPF.

    funcionario = buscar_funcionario_por_cpf(cpf)

    if not funcionario:
        return False, "Funcionário não encontrado."

    funcionarios.remove(funcionario)
    cpfs_cadastrados.discard(cpf)

    return True, "Funcionário excluído com sucesso!"
def cadastrar_combustivel(nome, preco_litro, fornecedor, estoque):
    #Cadastra um combustível.

    if not validar_vazio(nome):
        return False, "Nome inválido."

    if not validar_vazio(fornecedor):
        return False, "Fornecedor inválido."

    try:
        preco_litro = float(preco_litro)
        estoque = float(estoque)
    except ValueError:
        return False, "Preço e estoque devem ser números."

    novo_combustivel = {
        "id": gerar_id(combustiveis),
        "nome": nome,
        "preco_litro": preco_litro,
        "fornecedor": fornecedor,
        "estoque": estoque
    }

    combustiveis.append(novo_combustivel)

    return True, "Combustível cadastrado com sucesso!"


def buscar_combustivel_por_nome(nome):
    #Busca combustível pelo nome.

    for combustivel in combustiveis:
        if combustivel["nome"] == nome:
            return combustivel

    return None


def atualizar_combustivel(nome_antigo, novo_nome, novo_preco, novo_fornecedor, novo_estoque):
    #Atualiza um combustível

    combustivel = buscar_combustivel_por_nome(nome_antigo)

    if not combustivel:
        return False, "Combustível não encontrado."

    try:
        novo_preco = float(novo_preco)
        novo_estoque = float(novo_estoque)
    except ValueError:
        return False, "Preço e estoque devem ser números."

    combustivel["nome"] = novo_nome
    combustivel["preco_litro"] = novo_preco
    combustivel["fornecedor"] = novo_fornecedor
    combustivel["estoque"] = novo_estoque

    return True, "Combustível atualizado com sucesso!"


def excluir_combustivel(nome):
    #Exclui combustível pelo nome

    combustivel = buscar_combustivel_por_nome(nome)

    if not combustivel:
        return False, "Combustível não encontrado."

    combustiveis.remove(combustivel)

    return True, "Combustível excluído com sucesso!"
def cadastrar_bomba(numero, combustivel, status):

    for bomba in bombas:

        if bomba["numero"] == numero:
            return False, "Número da bomba já cadastrado."

    nova_bomba = {
        "id": gerar_id(bombas),
        "numero": numero,
        "combustivel": combustivel,
        "status": status
    }

    bombas.append(nova_bomba)

    return True, "Bomba cadastrada com sucesso!"


def buscar_bomba(numero):

    for bomba in bombas:

        if bomba["numero"] == numero:
            return bomba

    return None


def atualizar_bomba(
    numero_antigo,
    novo_numero,
    novo_combustivel,
    novo_status
):

    bomba = buscar_bomba(numero_antigo)

    if not bomba:
        return False, "Bomba não encontrada."

    bomba["numero"] = novo_numero
    bomba["combustivel"] = novo_combustivel
    bomba["status"] = novo_status

    return True, "Bomba atualizada com sucesso!"


def excluir_bomba(numero):

    bomba = buscar_bomba(numero)

    if not bomba:
        return False, "Bomba não encontrada."

    bombas.remove(bomba)

    return True, "Bomba excluída com sucesso!"
def registrar_venda(
    cpf_cliente,
    cpf_funcionario,
    numero_bomba,
    combustivel_nome,
    litros
):

    cliente = buscar_cliente_por_cpf(
        cpf_cliente
    )

    if not cliente:
        return False, "Cliente não encontrado."

    funcionario = buscar_funcionario_por_cpf(
        cpf_funcionario
    )

    if not funcionario:
        return False, "Funcionário não encontrado."

    bomba = buscar_bomba(
        numero_bomba
    )

    if not bomba:
        return False, "Bomba não encontrada."

    combustivel = buscar_combustivel_por_nome(
        combustivel_nome
    )

    if not combustivel:
        return False, "Combustível não encontrado."

    try:
        litros = float(litros)

    except ValueError:
        return False, "Quantidade inválida."

    if litros <= 0:
        return False, "Quantidade inválida."

    if combustivel["estoque"] < litros:
        return False, "Estoque insuficiente."

    valor_total = round(
        litros * combustivel["preco_litro"],
        2
    )

    nova_venda = {
        "id": gerar_id(vendas),
        "cliente": cpf_cliente,
        "funcionario": cpf_funcionario,
        "combustivel": combustivel_nome,
        "bomba": numero_bomba,
        "litros": litros,
        "valor_total": valor_total
    }

    vendas.append(
        nova_venda
    )

    combustivel["estoque"] -= litros

    return True, (
        f"Venda registrada com sucesso. "
        f"Total: R$ {valor_total}"
    )