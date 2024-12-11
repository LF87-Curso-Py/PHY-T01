palavra = input("Entre com a palavra: ").lower()
jogo = ["_" for letra in palavra] # Cria uma lista com "_" para cada letra da palavra

print("Vamos Jogar Forca!")
print("\nPalavra Secreta:", " ".join(jogo))

chances = 6
letras_usadas = set()

while chances > 0:
    letra = input("Fale uma letra: ").lower()

    if letra in letras_usadas:
        print("Você já usou essa letra!")
    else:
        letras_usadas.add(letra)

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                jogo[i] = letra
                print("".join(jogo))
    else:
        chances -= 1
        print(f"Essa letra não tem, sobraram {chances} chances.")

    if "_" not in jogo: # Verifica se todas as letras foram descobertas
        print("Você acertou!")
        break

if "_" in jogo:
    print("Que pena, você perdeu!")
    print("A palavra era:", palavra)