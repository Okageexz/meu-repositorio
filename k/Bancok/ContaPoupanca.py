from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
    def calcular_juros_mensal(self, taxa_juros):
        juros = self.saldo * (taxa_juros / 100)
        self.saldo += juros
        self.registrar_transacao("Juros Mensais", juros)
class ContaInvestimento(ContaBancaria):
    def __init__(self, numero_conta):
        super().__init__(numero_conta)
        self.investimentos = []
    def realizar_investimento(self, produto, valor):
# Lógica para realizar o investimento
        self.registrar_transacao("Investimento", valor)