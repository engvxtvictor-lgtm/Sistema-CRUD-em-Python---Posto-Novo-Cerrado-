from crud import (
    cadastrar_cliente,
    listar_clientes,
    buscar_cliente,
    atualizar_cliente,
    excluir_cliente,
    cadastrar_combustivel,
    listar_combustiveis,
    registrar_venda,
    listar_vendas,
    relatorio
)


def main():
    #menu principal
    while True:
        print("\n===== POSTO NOVO CERRADO =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Atualizar cliente")
        print("5 - Excluir cliente")
        print("6 - Cadastrar combustível")
        print("7 - Listar combustíveis")
        print("8 - Registrar venda")
        print("9 - Listar vendas")
        print("10 - Relatório")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "4":
            atualizar_cliente()
        elif opcao == "5":
            excluir_cliente()
        elif opcao == "6":
            cadastrar_combustivel()
        elif opcao == "7":
            listar_combustiveis()
        elif opcao == "8":
            registrar_venda()
        elif opcao == "9":
            listar_vendas()
        elif opcao == "10":
            relatorio()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


main()