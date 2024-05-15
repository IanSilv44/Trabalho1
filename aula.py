tabela = {'Alface': 5.00, 
          'Batata': 4.89, 
          'Tomate': 10.50, 
          'Feijão': 7.45}
valor_total = 0

while True:
    produto = input("Qual produto pesquisar: ")
   
    produto = produto.capitalize()
    if produto == "Sair":
        print("Bye!")
        break
    quantidade = int(input("Quantos produtos você quer ? "))
    total_produto = (tabela[produto]) * quantidade
    valor_total = valor_total + total_produto

    print(f"O valor total fico em R$ {valor_total:.2f}")


