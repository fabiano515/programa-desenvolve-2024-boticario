print("***********************************")
print("*Bem vindo ao jogo de adivinhação.*")
print("***********************************")

numero_secreto = 42
chute = int(input("Digite um número entre 0 e 100 \n"))
print("Você digitou ", chute)

acerto = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acerto):
    print("Você acertou")
else:
    if (maior):
        print("Seu chute foi maior que o número, você errou!")
    elif (menor):
        print("Seu chute foi menor que o número secreto, você errou!")
