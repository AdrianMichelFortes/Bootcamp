#Tupla: "irma" da lista
#Uma tupla tem um valor inical e segue com esse valor até o final sem alteração
#Em vez usar colchetes[lista] se usa parêntenses para(Tupla)

#Exemplos de tuplas de como podem ser criadas 

frutas = ("laranja", "pera", "uva",)   # O  aparecimento de uma virgula no final da tupla fará com que seja mais facil de ser reconhecida 

letras = tuple("python") # Pode ser utilizado também a palavra "tuple" para ser criar uma tupla

numeros = tuple([1, 2, 3, 4]) # Se for colocado uma lista dentro de uma tupla o  valor ou o item que existir dentro da mesma não haverá modificações até
                              # o final do codigo
                               
pais = ("Brasil",) # Novamente uma virgula no final para deixar mais claro que é uma tupla

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#          [0]       [1]      [2]     [3]
frutas = ("maçã", "laranja", "uva", "pera",) 

frutas[0]

frutas[2]

print(frutas[0]) #maçã

print(frutas[2]) #uva

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#          [0]       [1]      [2]     [3]
frutas = ("maçã", "laranja", "uva", "pera",) 

frutas[-1]  #laranja

frutas[-3]  #pera

print(frutas[-1]) #pera

print(frutas[-3]) #laranja

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Tuplas aninhadas: não sofrem alteração até o final do codigo 
#Se usa tupla quando você quer ter a garantia de que o valor contido dentro dela não seja alterado

Matriz = (

        (1,"a",2),
        ("b",3,4),
        (6,5,"c"),

)

Matriz[0]
Matriz[0][0]
Matriz[0][-1]
Matriz[-1][-1]

print(Matriz [0])       # (1, 'a' ,2)
print(Matriz [0][0])    # 1
print(Matriz [0][-1])   # 2
print(Matriz [-1][-1])  # c

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Fatiamento:

tupla = ("p", "y", "t", "h", "o", "n")

tupla[2:]    # 2 ponto inicial, O  segundo valor n foi declarado fazendo com que irá até o final da lista
tupla[:2]    # sem inicio, ponto de parada 2
tupla[1:3]   # ponto inicial 1, ponto de parada 3
tupla[0:3:2] # 0 ponto inicial, 3 ponto de parada, 2 pulando os itens de 2 a 2 (lembrando que sempre pegara a primeira letra)
tupla[::]    # Quando não tive especificações pegará do inicio ao fim
tupla[::-1]  # Do inicio ao fim porém da direita para a esquerda

print(tupla[2:])      #('t', 'h', 'o', 'n')
print(tupla[:2])      #('p', 'y')
print(tupla[1:3])     #('y', 't')
print(tupla[0:3:2])   #('p', 't')
print(tupla[::])      #('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1])    #('n', 'o', 'h', 't', 'y', 'p')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Iterar tupla:

carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .count utilizado para contagem de vezes que uma palavra aparece em uma tupla ou lista

cores = ("vermelho", "azul", "verde", "azul",)

cores.count("vermelho") #1
cores.count("azul")     #2
cores.count("verde")    #1

print(cores.count("vermelho")) 
print(cores.count("azul"))
print(cores.count("verde"))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# .index Ele passa a posição do item que você procura na tupla (apenas o primeiro que ele encontrar) se tiver dois repetidos ele  não irá contar o proximo
              # [0]     [1]    [2]   [3]      [4]
linguagens = ("python", "js", "c", "java", "csharp",)

linguagens.index("java")   #3
linguagens.index("python") #0

print(linguagens.index("java"))
print(linguagens.index("python"))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#

# len usado para saber o tamanho da tupla ou lista.

linguagens = ("python", "js", "c", "java", "csharp",)  
len (linguagens) #5 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------#