contador = 0

while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    if num > 0:
        contador += 1

print("Quantidade de positivos digitados:", contador)