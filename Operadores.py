#operadores aritmeticos:

#produto_1 = 10
#produto_2 = 20

#print(produto_1 + produto_2) #adição
#print(produto_1 - produto_2) #subtração
#print(produto_1 / produto_2) #divisor float 
#print(produto_1 // produto_2) #divisor int
#print(produto_1 * produto_2) #multiplicador 
#print(produto_1 % produto_2) #resto_de_divisão
#print(produto_1 ** produto_2) #potenciação

#X = 11
#if X%2==0:
#    print("é um numero par")
#else:
#    print("nao é par") 

#x= 10 + (5*4)   
#print(x)   

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#operadores de comparação:

#saldo = 200
#saque = 200

#print(saldo==saque) # comparando duas variaveis   (verdadeiro ou falso!)
#print(saldo!=saque) # saldo difererente de saque 
#print(saldo>saque)  # saldo maior que saque
#print(saldo>=saque) # saldo maior ou igual ao valor do saque
#print(saldo<saque)  # saldo menor que saque  
#print(saldo<=saque) # saldo menor ou igual ao valor do saque

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Operadores De Atribuição:

#saldo = 500

#print(saldo)

#saldo = 200

#print(saldo)

#saldo += 200

#print(saldo)

#saldo -= 200

#print(saldo)

#saldo /= 200

#print(saldo)

#saldo //= 200

#print(saldo)

#saldo *= 200

#print(saldo)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Operadores Lógicos:

#saldo = 1000
#saque = 250
#limite = 200
#conta_especial = True

#print(True and True)
#print(True and False)
#print(False and False) #"and" ambos tem ser de ser verdadeiro se não dará a resposta falsa "False"
#print(True or True)     
#print(True or False)
#print(False or False) # "or" algum de ambos sendo verdadeiro a resposta dará verdadeira "True"




#expressão = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
#print (expressão)

#expressão_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#print (expressão_2)

#conta_normal_com_saldo_suficiente = saque and saque <= limite
#conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

#expressão_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
#print(expressão_3)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Operadores De Identidade:

#saldo = 1000
#limite = saldo

#print(saldo is limite)
#print(saldo is not limite)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Operadores De Associação:

#Frutas =["limão", "uva", "banana"]
#Curso = "Curso de python"

#print  ("laranja" in Frutas)
#print  ("banana" not in Frutas) #É utilizado "not in" para saber se o item não está na lista
#print  ("python" in Curso)
#print  ("limão" in Frutas) #É utilizado "in" para saber se um item está na lista 

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#