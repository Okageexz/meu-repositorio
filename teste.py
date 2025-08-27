lista = [0, 1, 2, 3]
escolha = ["1", "2"]

escolha_usuario = int(input("\n Painel de Escolha \n 1 - Adicionar a lista  \n 2 - Remover da lista \n Escolha: "))

while True:
    if escolha_usuario == 1:
        num = int(input("Numero que deseja adicionar: "))
        lista.append(num)
        print(f"Imprimindo A Lista: {lista}")

    elif escolha_usuario == 2:
        num1 = int(input("Digite a  posição do numero que quer remover: "))
        lista.pop(num1)
        print(f"Imprimindo A Lista: {lista}")
    elif escolha_usuario == 3:
        print()
    else:
        print("Opção invalida!")