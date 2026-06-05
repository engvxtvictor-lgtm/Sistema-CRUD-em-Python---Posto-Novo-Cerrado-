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