from random import randrange

print("***********************************")
print("*Bem vindo ao jogo de adivinhação.*")
print("***********************************")

numeroSecreto = randrange(0, 11)
tentativas = 3
chance = 1

while chance <= tentativas:
    chute = int(input("Digite um número entre 0 e 10 \n"))
    print(f"Tentativa {chance} de 3.")
    print(f"Você digitou {chute} ")

    acerto = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if acerto:
        print("Você acertou!")
    else:
        if maior:
            print("Seu chute foi maior que o número secreto, você errou!")
        elif menor:
            print("Seu chute foi menor que o número secreto, você errou!")
    chance = chance + 1
