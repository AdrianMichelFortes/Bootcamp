#Recursos publicos e privados
#Público pode ser acessado de fora da classe.
#Privado só poder ser acessado pela classe
#qualquer informação que possa ser pedida fora da classe ela é publica qualquer um poderá
#fazer alterações
#já se ela for privada só poderá ser acessada o que tiver dentro da classe
#"pré padronizado" do codigo

class Conta:
    def __init__(self,  nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo


conta = Conta("0001", 100)
conta.depositar(100)
conta.sacar(50)
print(conta.nro_agencia)
print(conta.mostrar_saldo())


#------------------------------------------------------------------------------------#

# Propriedades:

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1

foo = Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)

#------------------------------------------------------------------------------------#

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Guilherme", 1994)
print(f"Nome:  {pessoa.nome} \tIdade: {pessoa.idade}")