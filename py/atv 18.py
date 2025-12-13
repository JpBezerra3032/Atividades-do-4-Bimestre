opcao = 0

while opcao != 3:
    print("\n1 - Somar dois números")
    print("2 - Subtrair dois números")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Soma =", a + b)

    elif opcao == 2:
        a = float(input("Número 1: "))
        b = float(input("Número 2: "))
        print("Subtração =", a - b)

    elif opcao == 3:
        print("Encerrando...")

    else:
        print("Opção inválida!")