# def função

def exibir_mensagem():
    print("Ola mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome="Anonimo"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Raissa")
exibir_mensagem_3() # Se eu nao passar nada, ele adota o nome Anonimo
exibir_mensagem_3(nome="Adrian")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# return 

def calcular_total(numeros):
    return sum(numeros) # sum = somar

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

x = calcular_total([10, 20, 34]) # 64
y = retorna_antecessor_e_sucessor(10) # (9, 11)

print(x)
print(y)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados ...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}") 

salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # existem duas formas de serem feitas a passagem de parametros para função
salvar_carro(marca = "Fiat", modelo = "Palio", ano = 1999, placa = "ABC-1234") # segunda forma  

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# *Args e **Kwargs / args = tupla kwargs = dicionário

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


exibir_poema(
    
    "Sexta-feira, 26 de agosto de 2022",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",
    autor="Tim Peters",
    ano=1999,
)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Parametros por posição

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): # após a barra tem de ser escrito o paramêtro de comparação
    print(modelo, ano, placa, marca, motor, combustivel)           # antes da barra deverá ser escrito por posição


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido pois está sendo passado  
                                                                                                             # parametro antes da barra

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Parametros nomeados 

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")

#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500
