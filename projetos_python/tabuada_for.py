print("Digite um número para calcular sua tabuada\n ")
number = int(input())

for i in range(1,11):
    print(f"{number} X {i} =",number*i)