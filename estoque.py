estoque = {}

def adicionar_item(item, quantidade):
    if item in estoque:
        estoque[item] += quantidade
    else:
        estoque[item] = quantidade

def remover_item(item, quantidade):
    if item in estoque:
        if estoque[item] >= quantidade:
            estoque[item] -= quantidade
            print("Item removido do estoque.")
            if estoque[item] == 0:
                del estoque[item]
        else:
            print("Quantidade insuficiente de", item, "no estoque.")
    else:
        print(item, "não encontrado no estoque.")

def exibir_estoque():
    print("Estoque atual:")
    for item, quantidade in estoque.items():
        print(item + ":", quantidade)

while True:
    print("\nO que deseja fazer?")
    print("1. Adicionar item ao estoque")
    print("2. Remover item do estoque")
    print("3. Exibir estoque")
    print("4. Fechar o sistema")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        item = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade a adicionar: "))
        adicionar_item(item, quantidade)
        print("Item adicionado ao estoque.")

    elif escolha == "2":
        item = input("Digite o nome do item: ")
        quantidade = int(input("Digite a quantidade a remover: "))
        remover_item(item, quantidade)

    elif escolha == "3":
        exibir_estoque()

    elif escolha == "4":
        print("Fechando o sistema de estoque.")
        break

    else:
        print("Opção inválida. Por favor, escolha novamente.")