
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