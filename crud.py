from dados import (
    clientes,
    funcionarios,
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