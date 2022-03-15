from conta import CriaConta

# >>>> Contas Criadas
conta1 = CriaConta(4863, "Geovana", 700000, 80)
conta2 = CriaConta(4569, "Leidiane", 300000, 1000)
conta3 = CriaConta(4766, "Werson", 50000, 15000)

# >>>> Movimentando contas
conta1.transferir(30000, conta2)
conta1.depositar(13000)
conta1.sacar(16000)

conta2.transferir(13000, conta3)
conta2.depositar(20000)
conta2.sacar(18000)

conta3.transferir(17000, conta1)
conta3.depositar(14000)
conta3.sacar(21000)
conta1.extrato()
conta2.extrato()
conta3.extrato()