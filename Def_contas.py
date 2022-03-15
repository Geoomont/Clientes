class CriaConta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        print("Conta Criada")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)

    def pagamento_boleto (self, valor):
        self.saldo -= valor

    def extrato(self):
        print("O Saldo da conta {} do(a) titular: {}, é de R${}.".format(self.numero, self.titular, self.saldo))
