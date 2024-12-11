# Exercício 1: O programa deverá solicitar duas notas de um aluno, calcular a média e apresentar a mensagem:
# -"Aprovado" caso média >= 7
# -"Reprovado" caso média < 7
# -"Aprovado com distição" caso média == 10

condicao = ("aprovado com distinção", "aprovado", "reprovado")
notas = []
n = 0

while n < 2:
    notas.append(float(input(f"Insira a nota da P{n + 1}: ")))

    if (notas[n] <= 10) and (notas[n] > 0):
        n += 1
    else:
        notas.pop(n)
        print("Valor inserido está fora do intervalo 0 - 10.")

media = sum(notas) / len(notas)

if media == 10.0:
    i = 0
elif (media >= 7.0) and (media < 10.0):
    i = 1
elif (media < 7.0) and (media >= 0.0):
    i = 2

print(f"O aluno foi {condicao[i]} com a nota {media}")


# Exercício 2: O programa deverá solicitar a medida dos três lados de um triângulo:
# - Deverá verificar se os valores informados podem mesmo formar um triângulo
# - Deverá informar, de acordo com as medidas, e o mesmo é Isósceles, Equilátero ou Escaleno

tipo_triang = ("escaleno", "isósceles", "equilatero")
lados = []
n = 0

while n < 3:
    lados.append(float(input(f"Insira a medida do Lado_{n + 1}: ")))

    if lados[n] > 0:
        n += 1
    else:
        lados.pop(n)
        print("Valor inserido é inválido.")

if (lados[0] + lados[1] > lados[2]) and (lados[0] + lados[2] > lados[1]) and (lados[1] + lados[2] > lados[0]):
    if (lados[0] == lados[1]) and (lados[0] == lados[2]):
        i = 2
    elif (lados[0] == lados[1]) or (lados[0] == lados[2]) or (lados[1] == lados[2]):
        i = 1
    else:
        i = 0
    print(f"As medidas dos lados informados são de um triângulo {tipo_triang[i]}")
else:
    print(f"As medidas dos lados informados NÃO são de um triângulo")

# Exercício 3: O programa deverá solicitar o valor do salario bruto do usuário:
# - Deverá verificar e. qual alíquota de IR o valor se encaixa
# - Deverá calcular e informar o valor do salário líquido do usuário

aliquota = 0
salario = input("Insira o valor de salário bruto:")
while not salario.isdigit(): salario = input("Insira o valor de salário bruto:")
salario = float(salario)

if (salario > 0) and (salario <= 2000): aliquota = 0
elif (salario > 2000) and (salario <= 3500): aliquota = 0.1
elif (salario > 3500) and (salario <= 5000): aliquota = 0.15
elif (salario > 5000): aliquota = 0.2

s_liquido = salario * (1-aliquota)

print(f"O salário líquido será de {s_liquido}")