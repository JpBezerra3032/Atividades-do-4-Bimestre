quantidade = 0
soma = 0
pares = 0
maior = None
menor = None

while True:
    num = int(input("Digite um número (0 para parar): "))

    if num == 0:
        break
    quantidade += 1
    soma += num

    if num % 2 == 0:
        pares += 1

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor ("RESULTADOS")
    print("Quantidade digitada:", quantidade)
    print("Média:", media)
    print("Maior número:", maior)
    print("Menor número:", menor)
    print("Quantidade de números pares:", pares)
else:
    print("Nenhum número foi digitado.")