"""Exercício 1: Crie um programa que receba o valor do raio de uma circunferência e imprima o diâmetro, o perímetro e a área"""
from math import pi

raio = float(input("Insira o valor do raio da circunferência: "))
unidade = input("Em qual unidade está trabalhando: ")

print(f"""
O diâmetro da circunferência é: {2 * raio:.2f}{unidade}
O perímetro da circunferência é: {2 * pi * raio:.2f}{unidade}
A área da circunferência é: {pi * (raio ** 2):.2f}{unidade}²
""")

"""Exercício 2: Crie um programa que receba um valor em graus Celsius e calcule a temperatura correspondente em Kelvin e Farenheit"""

celsius = float(input("Insira a temperatura em graus celsius: "))
print(f"""
A temperatura em kelvin é: {(celsius * 1.8) + 32:.2f} ºK
A temperatura em Farenheit é: {celsius + 273.15:.2f} ºF
""")

"""Exercício 3: Crie um programa que calcule a média de 4 bimestres de um aluno e apresente ao usuário"""

n1 = float(input("Insira a nota da p1: "))
n2 = float(input("Insira a nota da p2: "))
n3 = float(input("Insira a nota da p3: "))
n4 = float(input("Insira a nota da p4: "))

print(f"\nA média anual do aluno foi: {(n1+n2+n3+n4)/4:.2f}")