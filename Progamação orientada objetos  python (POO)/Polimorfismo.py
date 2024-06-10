# Polimorfismo:
# Mesmo metodo da herança de classe pai pra filha a diferença é q é possivel modificar
# a classe filha por mais que tenha recebido caracteristicas da classe pai

class Passaro:
    def voar(self):
        print("Voando....")

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

#Exemplo ruim do uso de herança para "ganha o método voar"
class Avião(Passaro):
    def voar(self):
        print("Avião está decolando")


def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Avião())
