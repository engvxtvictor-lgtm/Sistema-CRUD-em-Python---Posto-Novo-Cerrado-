from dados import clientes, cpfs_cadastrados
from utils import (
    gerar_id,
    validar_cpf,
    validar_telefone,
    validar_vazio,
    cpf_ja_existe
)


def cadastrar_cliente(nome, cpf, telefone):
    """
    Cadastra um novo cliente no sistema.
    """

    if not validar_vazio(nome):
        return False, "O nome não pode estar vazio."

    if not validar_cpf(cpf):
        return False, "CPF inválido. Deve conter exatamente 11 dígitos."

    if cpf_ja_existe(cpf):
        return False, "CPF já cadastrado."

    if not validar_telefone(telefone):
        return False, "Telefone inválido. Deve conter DDD + 9 dígitos."

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
def atualizar_cliente(cpf_antigo, novo_nome, novo_cpf, novo_telefone):
    """
    Atualiza os dados de um cliente.
    """

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
        return False, "Novo CPF já cadastrado."

    cpfs_cadastrados.discard(cliente["cpf"])

    cliente["nome"] = novo_nome
    cliente["cpf"] = novo_cpf
    cliente["telefone"] = novo_telefone

    cpfs_cadastrados.add(novo_cpf)

    return True, "Cliente atualizado com sucesso!"