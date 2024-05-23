#Strings:

#nome = "GuIlHeRme"

#print(nome.upper()) #Todas as letras maiusculas .upper
#print(nome.lower()) #Todas as letras minusculas .lower
#print(nome.title()) #TITULO "primeira letra maiuscula resto minuscula" .title

#texto = "   Olá mundo!    "

#print(texto)
#print(texto.strip()) #Retira o espaçamento da string .strip
#print(texto.rstrip()) #Retira o espaçamento da string do lado Direito .rstrip
#print(texto.lstrip()) #Retira o espaçamento da string do lado ESQUERDO .lstrip

#Menu = "Python"

#print ("####" + Menu + "####")
#print (Menu.center(14))
#print (Menu.center(14, "#"))
#print ("-".join(Menu)) #Coloca oq tiver em aspas duplas no meio das letras "".join

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Strings 2: "f-string"

#Nome = "Guilherme"
#idade =  28
#profissão = "Progamador"
#Linguagem = "Python"

#X= input("Digite o nome do jogador: ") 
#print(f"Nome:{X} Idade:{idade} Profissão:{profissão} Linguagem:{Linguagem}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Fatiamento de strings:

#nome = "Guilherme Arthur de Carvalho"

#print(nome[0])
#print(nome[-1])
#print(nome[:9])
#print(nome[10:])
#print(nome[10:16])
#print(nome[10:16:2])
#print(nome[:])
#print(nome[::-1])

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#String multiplas linhas:

nome = "Guilherme"

mensagem = f"""
    Olá meu nome é {nome}
Eu estou aprendendo Python
       Essa mensagem tem diferentes recuos.
""" #Utilização do f""" faz com que a frase apareça com os recuos deixados nos espaços em "branco"

print(mensagem)

print(
    """
      
    ====================Menu====================

    1 - Depositar
    2 - Sacar
    0 - Sair
      
    ============================================

         Obrigado por usar o nosso sistema!! 
    
    """)
