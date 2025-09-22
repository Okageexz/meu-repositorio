from depositar import depositar
import random
Saldo = 100

#jogo de azar
def jogo_de_azar():
    print("Bem Vindo ao jogo de azar!")
    print(f"Você tem R$ {Saldo:.2f}")

    #loop com a escolha
    while True:
        saldo = 100
        print("O que você gostaria de fazer?")
        print("1.Apostar")
        print("2.Sair")
        escolha = input("Escola uma opção: ")

        if escolha == "1":
            aposta = float(input("Quanto você gostaria de Apostar?: "))
            if aposta > saldo or aposta == 0:
                print("*Saldo Insuficiente.*")

                op_usuario = input("O que deseja fazer?: \n1 - Depositar \n2 - Voltar \nEscolha: ")

                if op_usuario == "1":
                    depositar(saldo)
                elif op_usuario == "2":
                    continue

            else:
                num_usuario = int(input("Digite um numero de 1 a 3: "))
                escolha_computador = random.randint(1, 3)
                
                if num_usuario != escolha_computador:
                    print(f"Resultado: {escolha_computador}")
                    print("~~~ Você Perdeu! ~~~")
                    saldo -= aposta
                else:
                    print(f"Resultado: {escolha_computador}")
                    print("~~~ Você Ganhou! ~~~")
                    saldo += aposta

            print(f"Seu Saldo atual é R${saldo}")
        elif escolha == "2":
            print(f"Você saiu do jogo com R${saldo}")
            break
        else:
            print("Opção Invalida!")


jogo_de_azar()