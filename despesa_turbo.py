i = 0
total = 0
while True:

    nota = input(f'insira o valor da nota_{i+1} e digite "Sair" para computar o total e sair: ').lower()
    if nota.isdigit():
        total += int(nota)
        i += 1

    if nota == "sair":
        print(f"Foram iseridos os valores de {i} notas, e o somatório total foi de R$ {total:.2f}")
        break

