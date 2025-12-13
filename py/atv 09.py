soma_pares = 0
soma_impares = 0

for i in range(10):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        soma_pares += num
    else:
        soma_impares += num

print("Soma dos pares:", soma_pares)
print("Soma dos ímpares:", soma_impares)