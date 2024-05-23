# ESSAS CHAVES A BAIXO ESTÃO DENTRO DE UM DICIONÁRIO {}
#
#
# contatos = { ⬅ INICIO DO DICIONÁRIO PRINCIPAL 
#           
#      [⬇CHAVES⬇]             [⬇DICIONÁRIOS DENTRO DE CADA CHAVE⬇]
#          🔑 
# "guilherme@gmail.com":  {"nome": "Guilherme", "telefone": "3333-2221"},
# "giovanna@gmail.com":   {"nome": "Giovanna", "telefone": "3443-2121"},
# "chappie@gmail.com":    {"nome": "Chappie", "telefone": "3344-9871"},
# "melaine@gmail.com":    {"nome": "Melaine", "telefone": "3333-7766"},
#          🔑 
#      [⬆CHAVES⬆]              [⬆DICIONÁRIOS DENTRO DE CADA CHAVE⬆]
#
# FIM DO DICIONÁRIO PRINCIPAL ➡ }

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# dict ou {} dicionário 
# para se utilizar dicionário se tem de usar tupla ou um valor imutável 

pessoa =  {"nome": "Guilherme", "idade": 28} # poder ser utilizado {} "objeto" em seguida fora das aspas : 2 pontos

pessoa = dict(nome="Guilherme", idade=28) # pode ser utilizado dict para ter acesso a ferramenta dicionário

pessoa["Telefone"] = "3333-1234" # aqui está sendo adicionado telefone ao dicionário "pessoa" utilizando []

print(pessoa) # {"nome": "Guilherme", "idade": 28, "telefone" : 3333-1234} 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

dados = {"nome": "Guilherme", "idade": 28, "telefone" : 3333-1234} 

dados["nome"] # Guilherme
dados["idade"] # 28
dados["telefone"] # 3333-1234 

# Os valores a cima foram substituidos por esses a baixo

dados["nome"] = "maria" 
dados["idade"] = 18 
dados["telefone"] = "9988-1781" 

print(dados) # {'nome': 'maria', 'idade': 18, 'telefone': '9988-1781'}

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# dicionário aninhados 

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"] # primeiro escolhe a linha usando o @ da casa e depois oque quer acessar dentro dela seja o nome ou telefone

print(telefone) # Dessa forma será printado apenas o telefone da "Giovanna"

print(contatos["giovanna@gmail.com"]) # Dessa maneira será printado tudo oque houver dentro do email de "Giovanna"

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# for dicionário

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

 #---------------------------------------------------------------------------------------------------------------------------------------------------------------#
 
# {}.clear
# limpa todas as listas deixando vazias
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.clear() # limpa todas as listas deixando vazias
print(contatos)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.copy usado para copiar o dicionário 

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"} # não altera os dados do dicionário original porém a copia pode ser modificada do jeito
}                                                                     # que for preferida pelo usuário

copia = contatos.copy() # está sendo copiada
copia["guilherme@gmail.com"] = {"nome": "gui"} # está sendo alterado o dicionário (copia) alterando o item contido dentro dele

contatos["guilherme@gmail.com"] # {"nome": "Guilherme", "telefone": "3333-2221"}  (contatos)

copia["guilherme@gmail.com"] # {"nome": "gui"}  (copia dos contatos modificada)

print(contatos) # contatos original
print(copia) # contatos copia

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.fromkeys utilizado para colocar chaves ao seu dicionário
# se o seu dicionário possuir nome coloque ele no lugar de dict

dict.fromkeys(["nome", "telefone"]) # {"nome": none, "telefone": none} 

dict.fromkeys(["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone": "vazio"}

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.get Ele procura a chave do dicionário

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"} 
} 

# contatos["chave"] #keyError aqui foi pedido pra que ele buscasse pela chave deu erro pois n foi utilizado .get

contatos.get("chave") # None nenhuma chave foi encontrada 
contatos.get("chave", {}) # {} se ele não encontrar uma chave ele retornará com o dicionário {vazio} logo apos a "," do codigo
contatos.get("guilherme@gmail.com", {}) # {guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}  essa é a mesma coisa da de cima a diferença 
                                        # é que existe essa chave então por esse motivo não retornou {vazio}

print(contatos.get("chave")) # none
print(contatos.get("chave", {})) # {} dicionário vazio
print(contatos.get("guilherme@gmail.com", {})) # {guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"} 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.items ele retorna uma lista de tuplas para a utilização do possivel comando for

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}  

contatos.items() 
print(contatos.items()) # ([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})]) <-------- lista de tuplas

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.keys utilizado para saber todas as chaves do dicionário quantas tem e quais são

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}  

resultado = contatos.keys() # dict_keys(['guilherme@gmail.com']) chave retornada
print(resultado)

novo_dicionario =  {"a": 100, 1: "teste", "b": "python"} # dict_keys(['a', 1, 'b']) chaves retornadas 
print(novo_dicionario.keys())

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.pop ele vai remover a chave do dicionário 

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}   

resultado = contatos.pop("guilherme@gmail.com") # {"nome": "Guilherme", "telefone": "3333-2221"} aqui foi removido o "email" "@"

print(resultado)

resultado = contatos.pop("guilherme@gmail.com", "Não encontrou a chave") # após a virgula do codigo pode ser colocado {} ou outra palavra 
                                                    # para caso não exista um valor para ser removido esse valor irá ser retornado 
print(resultado) # {}    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.popitem na falta de chaves da erro em vez de mostrar q n existe mais

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}  

#contatos.popitem()# ('guilherme@gmail.com', {"nome": "Guilherme", "telefone": "3333-2221"})
#print(contatos) 

#contatos.popitem()# KeyError quando não possuir mais chaves ele dará erro
#print(contatos) 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.setdefault faz alteração no dicionário caso falte algo
# se já possuir um nome ou idade, seja o item que for, o valor que você deu irá retornar e não fará com que tenha alterações no terminal

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna") # se não possuir o nome será trocada por "nome": "giovanna"
print(contato) # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28) # se não possuir idade será trocada por "idade": 28
print(contato) # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.uptade atualiza o dicionário

contatos ={
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}}) # aqui possui 1 dicionário guilherme@gmail.com
print(contatos) # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}}) 
print(contatos) # {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}  2 chaves  @giovanna@gmail.com
                #                                                                                                                          @guilherme@gmail.com

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.values mostra todos os dicionários e chaves

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.values()
print(contatos)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# "in" verificar se chave existe ou não em um dicionário

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos # true
print(resultado)

resultado = "megui@gmail.com" in contatos # false
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"] # false
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"] # true
print(resultado)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# "del" deletar algo do dicionário 

contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"] # removeu apenas o telefone dessa chave
del contatos["chappie@gmail.com"] # removeu a chave inteira 
print(contatos)