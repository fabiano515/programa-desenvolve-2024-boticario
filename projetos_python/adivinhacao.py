from random import randrange

print("***********************************")
print("*Bem vindo ao jogo de adivinhação.*")
print("***********************************")

numeroSecreto = randrange(1, 101)
tentativas = 0
chance = 1

print("Escolha um nível de dificuldade")
print("Digite (1) Facil, (2) Médio ou (3) Difícil")
nivel = int(input("Escolha seu nível :\n"))

if nivel == 1:
        tentativas = 100

elif nivel == 2:
       tentativas = 50

else:
        tentativas = 10

while chance <= tentativas:
    chute = int(input("Digite um número entre 1 e 100 \n"))
    print(f"Tentativa {chance} de {tentativas}.")
    print(f"Você digitou {chute} ")

    if chute < 1 or chute >10:
        print("Você deve digitar um número entre 1 e 10 \n")

    chance = chance + 1
    acerto = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if acerto:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Seu chute foi maior que o número secreto, você errou!")
        elif menor:
            print("Seu chute foi menor que o número secreto, você errou!")

