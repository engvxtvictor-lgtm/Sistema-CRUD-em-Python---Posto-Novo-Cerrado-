def gerar_id(lista):
    #vai gerar um ID automático
    return len(lista) + 1


def validar_cpf(cpf):
    #validar se o CPF tem 11 dígitos e é composto apenas por números
    return cpf.isdigit() and len(cpf) == 11


def buscar_por_cpf(lista, cpf):
    #vai buscar um registro pelo CPF
    for item in lista:
        if item["cpf"] == cpf:
            return item
    return None


def buscar_por_id(lista, id_busca):
    #vai buscar um registro pelo ID
    for item in lista:
        if item["id"] == id_busca:
            return item
    return None


def gerar_registros(lista):
    #vai gerar registros formatados para exibição
    for item in lista:
        yield item


def ler_float(mensagem):
    #aqui ele vai ler o num. decimal com tratamento de erro
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite um número válido.")


def ler_int(mensagem):
    #aqui ele vai ler o número e caso não seja um num. inteiro ele vai exibir a msg de erro e ...
    #pedir pra digitar novamente até que seja um número inteiro válido
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")