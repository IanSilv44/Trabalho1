import math

def menu():
    print("Bem-vindo à Calculadora Simples!")
    print("Selecione a operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Radiciação")
    print("6. Potenciação")
    print("7. Sair")

def get_numbers(operation):
    while True:
        try:
            quantidade_numeros = int(input("Quantos números você deseja calcular? "))
            if quantidade_numeros < 2 and operation in ('1', '2', '3', '4', '6'):
                print("Por favor, insira pelo menos dois números.")
                continue
            numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(quantidade_numeros)]
            return numeros
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

def calcular():
    while True:
        menu()
        escolha = input("Digite sua escolha (1/2/3/4/5/6/7): ")

        if escolha in ('1', '2', '3', '4', '6'):
            numeros = get_numbers(escolha)

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
                try:
                    resultado = numeros[0]
                    for num in numeros[1:]:
                        resultado /= num
                    print("Resultado:", f"{numeros[0]} / {' / '.join(map(str, numeros[1:]))}", "=", resultado)
                except ZeroDivisionError:
                    print("Erro: divisão por zero!")
            elif escolha == '6':
                base = numeros[0]
                expoente = numeros[1]
                resultado = math.pow(base, expoente)
                print("Resultado:", f"{base} ^ {expoente} =", resultado)

        elif escolha == '5':
            try:
                radicando = float(input("Digite o radicando: "))
                indice = float(input("Digite o índice da raiz: "))
                if radicando < 0 and indice % 2 == 0:
                    print("Erro: radiciação de número negativo com índice par não é permitida.")
                else:
                    resultado = radicando ** (1 / indice)
                    print(f"Resultado: raiz {indice} de {radicando} =", resultado)
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")

        elif escolha == '7':
            print("Saindo da calculadora.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Programa principal
if __name__ == "__main__":
    calcular()
