#BD do Posto Cerrado 

#Tables do Systema 
clientes = []
funcionarios = []
combustiveis = []
bombas = []
vendas = []

# Set 
cpfs_cadastrados = set()

# Tupla 
cargos = (
    "Frentista",
    "Frentista Gerente",
    "Dono do Posto"
)

combustiveis_tipos = (
    "Gasolina Comum",
    "Gasolina Aditivada",
    "Etanol",
    "Diesel",
    "Diesel S10"
)

"""Armazena os dados do usuário logado sendo usado pra identificar qual funcionário 
está logado no sistema e controlar as permissões e funcionalidades disponíveis dependendo do seu cargo."""
usuario_logado = None