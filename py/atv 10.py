maior = None
menor = None

for i in range(10):
    num = int(input("Digite um número: "))

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

print("Maior número:", maior)
print("Menor número:", menor)