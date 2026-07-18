# Posso passar uma funcao como retorno de outra. 
def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"


def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"


def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)


#print(executar(mensagem, "Joao"))
#print(executar(mensagem_longa, "Joao"))

# ------------------------------------------------------------------------------------
# E possivel definir funcoes dentro de outras funcoes: Funcao interna
def principal():
    print("executando a funcao principal")

    def funcao_interna():
        print("executando a funcao interna")

    def funcao_2():
        print("executando a funcao 2")

    funcao_interna()
    funcao_2()


#principal()

# ------------------------------------------------------------------------------------
# Retornando funcoes de funcoes 
def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div


op = calculadora("+")
#print(op(2, 2))
op = calculadora("-")
#print(op(2, 2))
op = calculadora("*")
#print(op(2, 2))
op = calculadora("/")
#print(op(2, 2))
# ------------------------------------------------------------------------------------

def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("faz algo depois de executar")

    return envelope

#@meu_decorador  simplifica o codico removendo a parte de baixa
def ola_mundo():
    print("Olá mundo!")


ola_mundo = meu_decorador(ola_mundo) # remove essa linha do codigo simplificando 
#ola_mundo()

#-------------------------------------------------------------------------------------

import functools


def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)

    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")


#print(ola_mundo.__name__)
# ------------------------------------------------------------------------------------

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        funcao(*args, **kwargs)
        print("faz algo depois de executar")

    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")


#ola_mundo("João", 1000)

# ------------------------------------------------------------------------------------

def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("faz algo depois de executar")
        return resultado

    return envelope


@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")
    return nome.upper()


resultado = ola_mundo("João", 1000)
print(resultado)
print(ola_mundo)

# ------------------------------------------------------------------------------------

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)


#----------------------------------------------------------------------------------------

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2 # em vez de usar return se utilizada yield 


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)