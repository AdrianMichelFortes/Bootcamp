# Herança simples:

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas 

    def ligar_motor(self):
        print("ligando o motor")

    def __str__(self):
        return self.cor
        

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhão(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) 
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("branco", "xde-0098", 4)
carro.ligar_motor()

caminhao = Caminhão("roxo", "gfd-8712", 8, False)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao.cor, caminhao.placa, caminhao.numero_rodas)

#------------------------------------------------------------------------------------#

# Herança Multipla:

class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)