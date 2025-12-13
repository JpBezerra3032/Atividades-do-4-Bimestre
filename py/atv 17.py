soma = 0
qtd = 0

while True:
    idade = int(input("Digite uma idade (0 para sair): "))
    if idade == 0:
        break
    soma += idade
    qtd += 1

if qtd > 0:
    media = soma / qtd
    print("Média das idades:", media)
else:
    print("Nenhuma idade informada.")