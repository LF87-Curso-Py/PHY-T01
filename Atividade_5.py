from click import clear
clear()

# ########### EXERCICIO 01 ############
#
# # Crie uma lista com 5 nomes de frutas
# fruteira = ["Maçã","Banana","Cereja","Amora","Mamão"]
#
# # Imprima a primeira e a última fruta da lista
# print(fruteira[0],'e', fruteira[-1])
#
# # Adicione 3 novas frutas à lista
# extras = ["Manga","Abacaxi","Melancia"]
# for i in extras:
#     fruteira.append(i)
# print(fruteira)
#
# # Remova a segunda fruta da lista
# fruteira.pop(1)
#
# # Ordene a lista em ordem alfabética
# fruteira.sort()
# print(fruteira)
#
# # Conte quantas vezes a fruta "banana" aparece na lista
# contador = fruteira.count("Banana")
# print(f"Banana aparece {contador} vezes na lista")
#
#
# ########### EXERCICIO 02 ############
#
# #Crie um tupla com os seguintes elementos: Seu nome, sua idade, e sua cidade natal:
# dados = ("Luiz", 36, "São Bernardo")
#
# #Imprima cada elemento da tupla e observe o que acontece. Explique o motivo.
# for i in dados:
#     print(i)        #A cada iteração do loop for a variável i recebe o valor armazenado na respectiva posição da lista
#
# #Tente modificar o primeiro elemento da tupla
# # dados[0] = "Felipe"     #Isso não é possível pois os dados dentro das tuplas são imutáveis
#
# #Crie uma nova tupla concatenando a tupla inicial com uma nova tupla contendo seus hobbies
# hobbies = ("musica","academia","video-game")
# nova= dados + hobbies
# print(nova)


# ########### EXERCICIO 03 ############

# # Crie um dicionario que representa um contato telefonico. As chaves devem ser nomes e os valores os números.
# agenda = {"MARIA": 98765432, "JOSÉ": 123445669, "JOÃO": [7387549889, 73283982]}

# # Adicione um novo contato ao dicionario
# agenda.update({"MARIO": 9847289742})
# print(agenda)

# # Mude o número de telefone de um contato
# agenda["JOSÉ"] = 87948398493
# print(agenda["JOSÉ"])

# # Imprima todos os nomes dos contatos
# print(*agenda.keys())


########### EXERCICIO 04 ############

# Crie um programa que simule um cadastro de produtos de uma loja. 
# Cada produto deve ter um Nome, Preço e Quantidade em Estoque.
# Utilize um dicionário para armazenar essas informações.
# O programa também deverá permitir:
#   - Cadastro de novos produtos;
#   - Consulta de informações de um produto específico;
#   - Alteração de preço de um produto;
#   - Remoção de produto do cadastro.

cadastro = {"Batata": [2.00, 150], "Macarrão": [4.00, 300]}

while True:
    opcao = input(f"\n1- Cadastro de produto"
                  f"\n2- Consulta de informações de um produto"
                  f"\n3- Alteração de preço de um produto"
                  f"\n4- Remoção de um produto do cadastro."
                  f"\nSelecione a opção desejada (1-4 ou 'S' para ): ").lower()
    match opcao:
        case "1":
            clear()
            len_ini = len(cadastro)
            nome = input(f"Digite o nome do produto que deseja cadastrar: ").title()

            preco = input(f"Digite o preço unitário do produto que deseja cadastrar: ").replace(",",".")
            try: float(preco)
            except:
                while not type(preco) == "float":
                    preco = input(f"Valor inválido. Insira o preço do produto que está cadastrando: ").replace(",",".")
                    try:
                        float(preco)
                        break
                    except: continue

            qtd = input(f"Insira a quantidade do produto que está cadastrando: ")
            while not qtd.isdigit():
                qtd = input(f"Insira a quantidade do produto que está cadastrando: ")
            int(qtd)

            cadastro.update({nome:[preco,qtd]})
            if len(cadastro) > len_ini: print("\nProduto cadastrado com sucesso")
            continue

        case "2":
            clear()
            if not len(cadastro):
                print("CADASTRO VAZIO")
                continue
            else:
                clear()
                c = 1
                for nome, qtd in cadastro.items():
                    print(f"{c}- ",nome)
                    c += 1
                while True:
                    produto = input(f"\nDigite o nome do produto desejado (sem as aspas) ou '0' para sair: ").title()
                    clear()
                    if produto in cadastro.keys():
                        print(f"O estoque atual de {produto} é de {cadastro[produto][1]} unidades e o preço unitário R$ {cadastro[produto][0]:.2f}.")
                        continue
                    elif produto == "0":
                        clear()
                        break
                    else:
                        print("O produto solicitado não está cadastrado.")
                        continue
        case "3":
            clear()
            c = 1
            for nome, lista in cadastro.items():
                print(f"{c}- ", nome, f" - R$ {lista[0]:.2f}")
                c += 1
            while True:
                produto = input(f"\nDigite o nome do produto (sem as aspas) ou '0' para sair: ").title()
                clear()
                if produto in cadastro.keys():
                    print(f"O preço atual do produto {produto} é R$ {cadastro[produto][0]:.2f} por unidade.")
                    novo_preco = input(f"Insira o preço de {produto} atualizado: ").replace(",", ".")
                    try:
                        float(novo_preco)
                    except:
                        while not type(novo_preco) == "float":
                            novo_preco = input(f"Valor inválido. Insira o preço do produto que está cadastrando: ").replace(",", ".")
                            try:
                                float(novo_preco)
                                break
                            except:
                                continue
                    cadastro[produto][0] = float(novo_preco)
                    print(type(cadastro[produto][0]))

                elif produto == "0":
                    clear()
                    break
                else:
                    print("O produto solicitado não está cadastrado.")
                    continue

        case "4":
            print("")

        case "s":
            print("\nObrigado por utilizar o nosso sistema. Tenha um bom dia.")
            break

        case _:
            print("")


########### EXERCICIO 05 ############

# Crie uma lista de dicionários para representar um conjunto de alunos.
# Cada dicionário deve conter as seguintes informações: Nome, Idade, Notas (uma lista com as notas das provas).
# Calcule a média de cada aluno;
# Encontre o aluno com a maior média;
# Ordene os alunos por idade ***;
# Crie uma lista contendo apenas ons nomes dos alunos com médias acima de 7.