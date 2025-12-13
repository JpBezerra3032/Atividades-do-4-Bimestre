soma = 0

for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

media = soma / 5
print("Média final =", media)