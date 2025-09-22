from ContaCorrente import ContaCorrente
from ContaBancaria import ContaBancaria

if __name__ == '__main__':
    conta1 = ContaBancaria("0001",300)
    conta1.consultar_saldo()

    conta2 = ContaCorrente("002")
    conta2.consultar_saldo()

    conta2.depositar(100)
    conta2.consultar_saldo()