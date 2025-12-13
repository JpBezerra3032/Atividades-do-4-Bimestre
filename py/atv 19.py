A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

print(f"Números ímpares entre {A} e {B}:")

# Garantir que A < B
if A > B:
    A, B = B, A

for i in range(A, B + 1):
    if i % 2 != 0:
        print(i)