# EXERCICIO 01 - Escreva um programa que solicite a entrada de um número, calcule a tabuada e apresente os resultados ao usuário.
a = 1

numero = int(input("Para saber a tabuada, insira um número qualquer: "))

while a <= 10:
    mult = numero * a
    print(f"{numero} * {a} = {mult}")
    a += 1

print("\nFim do programa\n")

# EXERCICIO 02 - Escreva um programa que pergunte ao usuário quantas despesas deseja somar,
#                solicite os valores gastos em cada uma e apresente o somatório total ao final.

total = 0

qt_dps = int(input("Informe a quantidade de despesas que serão inseridas: "))

for i in range(qt_dps):
    nota = float(input(f"insira o valor da nota_{i + 1}: "))
    total += nota

print(f"Foram iseridos os valores de {qt_dps} notas fiscais, e o somatório total foi de R$ {total:.2f}")

# EXERCICIO 02.1 (EXTRA) - Escreva um programa que receba valores de despesas de um usuário até que o mesmo
#                          indique o fim das entradas. Ao final apresente o somatório total das entradas.

i = 0
total = 0

while True:

    dsp = input(f'insira o valor da nota_{i + 1} e digite "fim" para computar o total e sair: ').lower()

    if dsp.isdigit():
        total += float(dsp)
        i += 1

    elif dsp == "fim":
        print(f"Foram iseridos os valores de {i} notas, e o somatório total foi de R$ {total:.2f}")
        break

    else:
        print("Valor inválido")

# EXERCICIO 03 - Escreva um programa que simule um sistema de banco simples com as seguintes opções:
#                - Menu com: 1- Saldo, 2- Saque, 3- Depósito, "S"- Sair.
#                - A aplicação deve parar quando o cliente escolher "S".
#                - Ao final, imprima uma mensagem com o saldo final do cliente.

saldo = 0

while True:

    opcao = input('\n1- Saldo\n2- Saque\n3- Depósito\nS- Sair\n\nDigite a alternativa desejada:').lower()

    match opcao:

        case "1":
            print(f"\nSeu saldo é de: R$ {saldo:.2f}")

        case "2":
            if saldo == 0:
                print(f"\nO saldo da conta é de R$ {saldo:.2f}, por gentileza deposite antes de sacar.\n")
                continue

            saque = float(input("Insira o valor que deseja sacar: "))

            if saque > saldo:
                print("\nO valor solicitado excede o limite disponível.\nREPITA A OPERAÇÃO\n")
                continue

            else:
                saldo -= saque
                print(f"\nRetire seu dinheiro.\n\nSaldo remanescente: R$ {saldo:.2f}\n")

        case "3":
            deposito = float(input("Insira o valor que deseja depositar: "))

            if deposito < 0:
                print("\nO valor informado é inválido.\nREPITA A OPERAÇÃO\n")
                continue

            else:
                saldo += deposito
                print(f"\nSaldo atualidado: R$ {saldo:.2f}\n")

        case "s":
            break

        case _:
            print(f'\nOpção inválida.\nDigite uma das opçãoes de 1 a 3 ou "S" para sair.\n')
            continue

# print(f"\nObrigado pela preferência.\nSISTEMA ENCERRADO.\n")