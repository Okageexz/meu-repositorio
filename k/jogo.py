import random, os

#jogo de azar
def jogo_de_azar():
    saldo = 100

    def depositar(Saldo):
        saldo_depositado = float(input("Saldo a ser Depositado: "))
        return f"Saldo Atual:{Saldo + saldo_depositado}"

    #saldo_usuario = 100
    print("Bem Vindo ao jogo de azar!")
    #loop com a escolha
    while True:
        print("O que você gostaria de fazer?")
        print("1.Apostar")
        print("2.Sair")
        print("3.Mostrar Saldo")
        escolha = input("Escola uma opção: ")
        os.system('cls')

        if escolha == "1":
            aposta = float(input("Quanto você gostaria de Apostar?: "))
            
            if aposta > saldo or saldo == 0:
                print("*Saldo Insuficiente.*")

                op_usuario = input("O que deseja fazer?: \n1 - Depositar \n2 - Voltar \nEscolha: ")
                if op_usuario == "1":
                    depositar(saldo)
                    continue
                elif op_usuario == "2":
                    continue

            if aposta <= 0:
                print("*Valor invalido!*")

            else:
                num_usuario = int(input("Digite um numero de 1 a 3: "))
                escolha_computador = random.randint(1, 3)
                
                if num_usuario > 3:
                    print("Valor Invalido!")
                    continue
                if num_usuario != escolha_computador:
                    print(f"Resultado: {escolha_computador}")
                    print("~~~ Você Perdeu! ~~~")
                    saldo -= aposta
                else:
                    print(f"Resultado: {escolha_computador}")
                    print("~~~ Você Ganhou! ~~~")
                    saldo += aposta

            print(f"Seu Saldo atual é R${saldo:.2f}")
            
        elif escolha == "2":
            print(f"Você saiu do jogo com R${saldo:.2f}")
            break
        elif escolha == "3":
            print(f"*Saldo Atual: R${saldo:.2f}*")
        else:
            print("Opção Invalida!")

jogo_de_azar()