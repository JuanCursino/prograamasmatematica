import random

opcoes = ["tesoura", "papel", "pedra"]

eu = input("Escolha sua jogada: pedra, papel ou tesoura? ").lower()
computador = random.choice(opcoes)

print("Você jogou " + eu)
print("Computador jogou " + computador)

if eu not in opcoes:
    print("Jogada inválida.")
elif eu == computador:
    print("deu empate")
elif eu == "tesoura":
    if computador == "pedra":
        print("você perdeu")
    else:
        print("você ganhou")
elif eu == "papel":
    if computador == "tesoura":
        print("você perdeu")
    else:
        print("você ganhou")
elif eu == "pedra":
    if computador == "tesoura":
        print("você perdeu")
    else:
        print("você ganhou")

# O jogo "Pedra, Papel e Tesoura" envolve conceitos de teoria dos conjuntos, 
# onde cada jogador escolhe um elemento de um conjunto predefinido.