def calcular():
    print("Bem-vindo à Calculadora Simples!")
    print("Selecione a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    while True:
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        if escolha in ('1', '2', '3', '4'):
            quantidade_numeros = int(input("Quantos números você deseja calcular? "))
            numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(quantidade_numeros)]

            if escolha == '1':
                resultado = sum(numeros)
                print("Resultado:", " + ".join(map(str, numeros)), "=", resultado)
            elif escolha == '2':
                resultado = numeros[0] - sum(numeros[1:])
                print("Resultado:", f"{numeros[0]} - {' - '.join(map(str, numeros[1:]))}", "=", resultado)
            elif escolha == '3':
                resultado = 1
                for num in numeros:
                    resultado *= num
                print("Resultado:", " * ".join(map(str, numeros)), "=", resultado)
            elif escolha == '4':
                if 0 in numeros[1:]:
                    print("Erro: divisão por zero!")
                else:
                    resultado = numeros[0] / (numeros[1] * numeros[2] if len(numeros) > 2 else numeros[1])
                    print("Resultado:", f"{numeros[0]} / {' / '.join(map(str, numeros[1:]))}", "=", resultado)
        
        elif escolha == '5':
            print("Saindo da calculadora.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Programa principal
if __name__ == "__main__":
    calcular()




