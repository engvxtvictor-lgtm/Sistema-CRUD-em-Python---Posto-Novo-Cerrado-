#Utils do projeto 

from dados import clientes, funcionarios, vendas, cpfs_cadastrados

# Função geradora dos IDs dos clientes e funcionários:
def gerar_id(lista):
    # gera um id incremental baseado no tamanho da lista 
    if len(lista) == 0:
        return 1
    return lista[-1]["id"] + 1

# Função da busca pelo id:
def buscar_por_id(lista, id_busca):
    #busca o registro pelo id
    for item in lista:
        if item["id"] == id_busca:
            return item
    return None

# Função para buscar o Cpf: 
def buscar_por_cpf(lista, cpf):
    #busca registro pelo CPF 
    for item in lista:
        if item["cpf"] == cpf:
            return item
    return None

#verificação de validação do CPF:
def validar_cpf(cpf):
    #o CPF tem que ter 11 dígitos e eles devem ser apenas números e nada de ponto e coisas do gênero
    return cpf.isdigit() and len(cpf) == 11

# Validação do telefone: 
def validar_telefone(telefone):
    #o número do telefone deve ter 11 dígitos no total (DDD + 9 números)
    return telefone.isdigit() and len(telefone) == 11

# Campos vazios: 
def validar_vazio(valor):
    #fase de verificação = se campo está vazio
    return valor.strip() != ""

# Garantia de cpf não duplicado: 
def cpf_ja_existe(cpf):
    #Verifica se CPF já está cadastrado no sistema
    return cpf in cpfs_cadastrados
 
#Função geradora de clientes : 
def gerar_clientes():
  #olhar cliente por cliente na lista de clientes e retornar um por um usando yield
    for cliente in clientes:
        yield cliente
        
#Função geradora de vendas: 
def gerar_vendas():
    for venda in vendas:
        yield venda
def verificar_login(st):
    #Verifica se existe usuário logado no Streamlit

    if "usuario_logado" not in st.session_state:
        st.session_state.usuario_logado = None

    if st.session_state.usuario_logado is None:
        st.warning("Faça login para acessar esta página.")
        st.stop()

    return st.session_state.usuario_logado


def verificar_cargo(st, cargos_permitidos):
    #Verifica se o usuário possui permissão pelo cargo

    usuario = verificar_login(st)

    if usuario["cargo"] not in cargos_permitidos:
        st.error("Você não tem permissão para acessar esta funcionalidade.")
        st.stop()

    return usuario
def verificar_login(st):
    #Verifica se existe usuário logado no Streamlit

    if "usuario_logado" not in st.session_state:
        st.session_state.usuario_logado = None

    if st.session_state.usuario_logado is None:
        st.warning("Faça login para acessar esta página.")
        st.stop()

    return st.session_state.usuario_logado


def verificar_cargo(st, cargos_permitidos):
    #Verifica se o usuário possui cargo permitido

    usuario = verificar_login(st)

    if usuario["cargo"] not in cargos_permitidos:
        st.error("Você não tem permissão para acessar esta página.")
        st.stop()

    return usuario