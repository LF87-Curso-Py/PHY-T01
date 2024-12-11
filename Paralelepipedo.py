import time

palavra = "paralelepipedo"

indice = 0
for i in range(len(palavra)//2):
    i *= 2
    print(palavra[i] + palavra[i + 1])
    time.sleep(0.5)

lista_alunos = ["João", "Maria", "Ana", "Davi"]
notas_alunos = [5, 7, 10, 9]

print(list(enumerate(lista_alunos)))

for posicao, nome in enumerate(lista_alunos):
    if nome == "João":
        notas_alunos[posicao] = 7.5

print(notas_alunos)

meu_dicionario = {"a": 1, "b": 2, "c": 3, "d": 4,}
print(meu_dicionario)
meu_dicionario.update({"e": 1, "f": 2, "g": 3, "h": 4,})
print(meu_dicionario)
for chave, valor in meu_dicionario.items():
    print(chave + "---" + str(valor))