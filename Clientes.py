class Cliente:
    def __init__(self, nome, cpf, plano):
        self.nome = nome
        self.cpf = cpf
        self.lista_planos = ["basic", "premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
          raise Exception("Plano inválido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else: 
            print("Plano inválido")

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver Filme {filme}")
        elif self.plano == "premium":
            print(f"Ver Filme {filme}")
        elif self.plano == "basic":
            print("Faça upgrade para premium para ver esse filme")
        else:
            print("Plano inválido")
        
cliente = Cliente("Geo", "7070070", "basic")
print(cliente.plano)
cliente.ver_filme ("Harry Potter", "premium")

# no botao upgrade
cliente.mudar_plano("premium")
print(cliente.plano)
cliente.ver_filme ("Harry Potter", "premium")