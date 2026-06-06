#BD do Posto Cerrado 

#Tables do Systema 
clientes = []
funcionarios = []
combustiveis = []
bombas = []
vendas = []

# Set 
cpfs_cadastrados = {"00000000000"}

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
está logado no sistema e controlar as permissões e funcionalidades disponíveis dependendo seu cargo."""
usuario_logado = None

{
    "id": 1,
    "nome": "Administrador",
    "cpf": "00000000000",
    "telefone": "86999999999",
    "cargo": "Dono do Posto",
    "data_admissao": "2026-06-05"
}