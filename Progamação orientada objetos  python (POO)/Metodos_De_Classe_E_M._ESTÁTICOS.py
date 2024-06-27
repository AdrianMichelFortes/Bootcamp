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

# Classe abstrata "ABC" @abstractmethod

from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    
    @abstractmethod
    def ligar(self):
        pass
   
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
       pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando a Tv")
        print("Ligada!")
    

    def desligar(self):
        print("Desligando a Tv ...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"
    
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando  o Ar Condicionado ...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar condicionado")
        print("Desligado!")

    @property
    def marca(self):
        return "Philco"

controle = ControleTv()

controle.ligar()

controle.desligar()

print(controle.marca)


controle = ControleArCondicionado()

controle.ligar()

controle.desligar()

print(controle.marca)