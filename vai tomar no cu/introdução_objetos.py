# O que e POO:Paradigma de programacao (Um estilo de programacao)
# Paradigmas: Imperativo ou procedural; Funcional; Orientado a eventos e a objetos.
# Orientado a objetos: estrutura o codigo abstraindo problemas em objetos do mundo real



#------------------------------------------------------------------------------------#

# __init__ método inicializador do classe

class Cachorro:
    def __init__(self, nome, cor, acordado=True): # pode ser colocado qualquer palavra no lugar de "self"
        self.nome = nome
        self.cor = cor    
        self.acordado = acordado

    def latir(self): # <--------- função
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzzzzz...")

cao_1 = Cachorro("Chappie", "amarelo", False)
cao_2 = Cachorro("Raissa", "rosinha") #atribuindo a variavel cao 2 a classe cachorro e suas caracteristicas


print(cao_2.nome, cao_2.cor) # chamar no self

cao_2.dormir()  # chamar a função

print(cao_2.nome, cao_2.cor, cao_2.acordado) # print de every body tudão sobre o cao 2

#------------------------------------------------------------------------------------#

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def __str__(self):
        return f"Biblioteca: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"

#    def __str__(self):
#        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
b2.correr()
print(b2)

#------------------------------------------------------------------------------------#

# __del__

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

c = Cachorro("Chappie", "amarelo")
c.falar()

del c #chamando a função para deletar a instancia c antes do codigo terminar
# pode ser chamado a qualquer momento do codigo

print("MAOKAI BATATEIRO")

