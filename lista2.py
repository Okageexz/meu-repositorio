import time

frutas = []

while True:
    escolha_usuario = int(input("\n Painel de Escolha \n 1 - Adicionar a fruta a lista \n 2 - Remover a fruta da lista \n 3 - Mostrar lista \n 4 - Sair \n Escolha: "))
    
    if escolha_usuario == 1:
        add = input("Fruta que deseja adicionar: ")
        if add not in frutas:
            frutas.append(add)
            print("---------")
            print(f"{add.capitalize()} Adicionado!")
            print("---------")
        else:
            print("A fruta que deseja adicionar ja existe!")
            print("---------")
        print("Frutas Adicionadas: ")
        for i, fruta in enumerate(frutas):
            print(f"{i}.{fruta}")
        
    elif escolha_usuario == 2:
        print(frutas)
        remove = int(input("Digite a posição da fruta que deseja remover: "))
        if remove not in frutas:
            print("Opção invalida")
        else:
            print("---------")
            frutas.pop(remove)
            print(f"Imprimindo A Lista: {frutas}")
    
    elif escolha_usuario == 3:
            if not frutas:
                print("A Lista não possui frutas")
            else:
                print(f"{frutas}")
                time.sleep(2.5)
        
    elif escolha_usuario == 4:
        print("Saindo...")
        break
    else:
        print("Opção invalida! Tente novamente!")