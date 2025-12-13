import random

secreto = random.randint(1, 20)
tentativa = 0

while True:
    num = int(input("Digite um palpite (1 a 20): "))
    tentativa += 1

    if num == secreto:
        print("Acertou em", tentativa, "tentativas!")
        break
    else:
        print("Errado, tente novamente!")