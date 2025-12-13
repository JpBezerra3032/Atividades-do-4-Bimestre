soma = 0

while True:
    num = int(input("Digite um número (negativo para parar): "))
    if num < 0:
        break
    soma += num

print("Soma dos números positivos:", soma)