class Cliente:
    def __init__(self, nome, CPF, idade):
        self.nome = nome
        self.CPF = CPF
        self.idade = idade
    def get_nome(self):
        return self.nome.title()
    