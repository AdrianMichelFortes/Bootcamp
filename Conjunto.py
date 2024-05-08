# "set" "{}" é utilizado para remover repetições de uma lista

#lista ([])
#string ()
#tupla (())
#set    {} ou set

lista = set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}  Ele remove em ordem aleatoria os numeros que estiverem (dentro da lista repetidos) dependendo do pc pode dar varios
                                 #resultados diferentes no terminal, porém o resultado final sempre será o mesmo

string = set("abacaxi") # {"b", "a", "c", "x", "i"} # o resultado no terminal será esse porém pode estar em ordem trocada ñ influencia com o resultado final

tupla = set(("palio", "gol", "celta", "palio",)) # {"gol", "celta", "palio"} # o resultado no terminal pode ser igual a esse ou em ordem trocada

set = {"python", "java", "python"} # pode ser utilizado "{}" em vez de precisar escrever "set" será o mesmo resultado

print (lista)
print (string)  
print (tupla)
print (set)

#Exemplo de transformação de um set {} para lista ([])

numeros = {1, 2, 3, 2} # set {}

numeros = list(numeros) # transformando o "set {}" para uma lista "list"

numeros[0] # aqui será formada a lista dos numeros que sobrarem de set (os numeros que não forem repetidos)

print(numeros) # aqui fará com que apareça no terminal a lista

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# "for" utilizando ele em conjunto set


carros = {"gol", "celta", "palio", "gol"}

for carro in carros:
    print(carro)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.union utilizado para juntar duas coisas em set 

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_c = conjunto_a.union(conjunto_b) # {1, 2,} + {3, 4}

print(conjunto_c) # {1, 2, 3, 4} juntou os dois e printou

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.intersection utilizado para juntar os iguais o que não for igual cai fora

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_c = conjunto_a.intersection(conjunto_b) # {1, 2, 3} = {2, 3, 4}

print(conjunto_c) # {2, 3} uniu os iguais oque foi diferente não "printou"

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.difference utilizado para verificar a diferença entre os ambos set porém você faz um a um sendo um codigo mais extenso 

conjunto_a = {1, 2, 3} # {1} no conjunto_a diferente do conjunto_b tem o numero 1
conjunto_b = {2, 3, 4} # {4} no conjunto_b diferente do conjunto_a tem o numero 4 

x = conjunto_a.difference(conjunto_b) # {1} os numeros ou palavras que aparecem no terminal são os que são diferentes dos contidos em ambas as listas
y = conjunto_b.difference(conjunto_a) # {4} ou seja juntando ambas as listas ele vê o que tem de diferente e coloca no terminal 

print(x) # {1}
print(y) # {4}

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.symmetric_difference utilizado para verificar as diferenças entre ambos os set porém ele simplifica fazendo com que seja mais curto o codigo

conjunto_a = {1, 2, 3} # {1} 
conjunto_b = {2, 3, 4} # {4}
 
x = conjunto_a.symmetric_difference(conjunto_b) # {1, 4} Simplificou o codigo a cima fazendo apenas uma linha em vez de duas

print(x) # {1, 4} 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .issubset utilizado para verificar se os mesmos elementos estão em ambos os set dando true ou false leitura da esquerda para a direita

conjunto_a = {1, 2, 3,}
conjunto_b = {4, 1, 2, 5, 6, 3}

x = conjunto_a.issubset(conjunto_b) # True todos os elementos em a estão em b ou seja {1, 2, 3} 
y = conjunto_b.issubset(conjunto_a) # False aqui faltam elementos para b possa estar em a {1, 2, 3} elementos que faltam para dar #true ---> {4, 5, 6}

print(x) # conjunto a {-  1, 2, -  -  3} True  todos os elementos de a estão em b
print(y) # conjunto b {4, 1, 2, 5, 6, 3} False faltam alguns elementos em a para que b possa dar true 4 5 6

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.issuperset utilizado para verificar se os mesmos elementos estão em ambos os set dando true ou false leitura da direita para a esquerda no codigo

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

x = conjunto_a.issuperset(conjunto_b) # Nem todos os elementos de b estão em a
y = conjunto_b.issuperset(conjunto_a) # todos os elementos de a estão em b

print(x) # False
print(y) # True

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.isdisjoint Utilizado para fazer comparações de conjunto Se não possuirem itens iguais o resultado será True
#               se possuirem 1 item que seja igual em ambos os set dará false 



conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

x = conjunto_a.isdisjoint(conjunto_b) #True O conjunto A é diferente do conjunto B pois não possui nenhum numero repetido em ambos
y = conjunto_a.isdisjoint(conjunto_c) #False O conjunto A não é diferente do conjunto C pois possui o {1} no seu set 

print(x) # True
print(y) # False

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .add adiciona um numero ao set

sorteio = {1, 23} 

sorteio.add(25) # {1, 23, 25} adicionou 25

print(sorteio)

sorteio.add(42) # {1, 23, 25, 42} adicionou 42

print(sorteio)

sorteio.add(25) # {1, 23, 25, 42} Não adicionou 25 pois está sendo utilizado um set {} e set não possui repetições (não permite)

print(sorteio) # {1, 23, 25, 42} resultado final

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.clear limpa o set retira tudo oque tem dentro

sorteio = {1, 23}

sorteio # {1, 23}
sorteio.clear()
sorteio # {}

print(sorteio) # set() <------- vazio

sorteio.add(15) # adicionado 15 ao set que estava vazio 

print(sorteio) # {15} recebeu os 15 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#   

# {}.copy Utilizado para copiar e usar o codigo em outro momento que desejar ou reutilizar o mesmo

sorteio = {1, 23}

sorteio # {1, 23}
sorteio.copy() # copiou o sorteio 
sorteio # {1, 23}

print(sorteio) # {1, 23}

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.discard Elimina itens do set 

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0} # Eliminou os repetidos função do proprio set {}

numeros.discard(1) # Eliminou o numero 1 

numeros.discard(45)# Não eliminou o numero pois não estava no set

numeros # {0, 2, 3, 4, 5, 6, 7, 8, 9} numeros restantes

print(numeros) # {0, 2, 3, 4, 5, 6, 7, 8, 9}

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.pop remove sempre o primeiro item contido no set {}

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros) # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} inicial

print(numeros.pop()) # 0 removido
print(numeros.pop()) # 1 removido
print(numeros.pop()) # 2 removido
print(numeros.pop()) # 3 removido
print(numeros.pop()) # 4 removido
print(numeros.pop()) # 5 removido

print(numeros) # {6, 7, 8, 9} final apos ter removido o primeiro item da lista com os pop

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {}.remove diferente do discard ele da erro quando algum numero que não existe no set tenta ser removido

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} inicial

numeros.remove(0)   # 0 foi removido
numeros.remove(5)   # 5 foi removido
#numeros.remove(45) # 45 não foi removido o codigo dará erro é necessário colocar um numero existente no set acima para que o codigo volte a funcionar

numeros # {1, 2, 3, 4, 6, 7, 8, 9} após as remoções, final

print(numeros) # {1, 2, 3, 4, 6, 7, 8, 9} resultado

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {} len faz a contagem dos itens que estão dentro do set

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} inicial

len(numeros) # (len) contou o tamanho do set contendo 10 numeros 

print(len(numeros)) # Dessa forma irá printar o contador de numeros (len)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# {} in verifica se o numero está dentro do set 

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

x = 1 in numeros # True 1 está dentro do set numeros
y = 10 in numeros # False 10 não está dentro do set numeros

print(x) # True
print(y) # False

