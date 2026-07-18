class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod #METODO DE CLASSES
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod #METODO ESTATICO
    def e_maior_de_idade(idade):
        return idade >= 18 

#p = Pessoa("Guilherme", 28)
#print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(1994, 3, 21, "Raissa") #METODO DE CLASSES
print(p2.nome, p2.idade)

print(Pessoa.e_maior_de_idade(18)) #METODO ESTATICO
print(Pessoa.e_maior_de_idade(8)) #METODO ESTATICO

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

