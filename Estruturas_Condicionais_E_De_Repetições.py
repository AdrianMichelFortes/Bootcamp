#Identação e blocos:

#Simulação simples De Deposito e Saque De Um Caixa

#def Sacar(valor):
#    print("Seja bem vindo")
#    saldo = 500 
#    print("Saldo Atual:",saldo)
#    if saldo >= valor:
#        print("valor Sacado:", valor)
#        print("Saldo Restante:", saldo-valor)
#    else:
#        print("Saldo insuficiente")
#        print("Tentativa de saque:", valor)

#def Depositar(valor):
#    print("Seja bem vindo")
#    saldo = 500
#    print("Saldo Atual:", saldo)
#    saldo+= valor
#    print("Novo saldo:", saldo)
#    print("O deposito foi um sucesso!")
    

#Sacar(0)
#Depositar(250)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Estruturas Condicionais:

#Maior_Idade = 18
#Idade_Especial = 17 

#Idade = int(input("Informe a sua idade:"))

#if Idade >= Maior_Idade:
#    print("Maior de idade, Pode tirar CNH.")

#if Idade < Maior_Idade:
#    print("Ainda não pode tirar a CNH.") 
    
#if Idade >= Maior_Idade:
#    print("Maior de idade, Pode tirar CNH.")
#else:
#    print("Ainda não pode tirar a CNH.") 


#if Idade >= Maior_Idade:
#    print("Maior de idade, Pode tirar CNH.")
#elif Idade == Idade_Especial:
#    print("Pode fazer aulas teoricas, mas não pode fazer aulas práticas")
#else:
#    print("ainda não pode tirar a CNH")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Estrutura Condicional Aninhada:

#Conta_normal = True
#Conta_universitaria = False

#saldo = 2000
#saque = 2500
#Cheque_Especial = 450

#if Conta_normal:
#    if saldo >= saque:
#        print("Saque realizado com sucesso!")
#    elif saque <= (saldo + Cheque_Especial):
#        print("Saque realizado com cheque especial!")
#    else:
#        print("Não foi possivel realizar o saque, saldo insuficiente!")
#elif Conta_universitaria:
#    if saldo >= saque:
#        print("Saque realizado com sucesso!")
#    else:
#        print("Saldo insuficiente!")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Estrutura Condicional Ternaria:

#saldo = 2000
#saque = 2500

#status = "Sucesso" if saldo >= saque else "Falha"

#print(f"{status} ao realizar o saque!")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Estrutura Repetição "for":

#texto = input("informe o seu texto: ")
#texto = "" #Quando ñ possuir nenhum caracter dentro de aspas ele pulara da função "for" para "else"
#Vogais = "AEIOU"

#Exemplo utilizando um iterável

#for letra in texto:
#    if letra.upper() in Vogais:
#        print() # print Sem nada dentro pula linha! (Terminal)
#        print(letra, end="")
#else:
#    print()
#    print("Deu tudo errado")

#Exemplo utilizando a função built-in range

#for numero in range(0, 51, 5): #Função range: 0 a 51 pulando de 5 em 5: lembrar que se fosse de 1 a 1  pararia um numero antes (50)
#    print(numero, end=" ")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Estrutura Repetição "while":

#opcao = -1 #Variavel utilizada somente para entrar dentro do menu, sem ela n funciona
#A diferença entre usar "while" ou "if" é que "while" irá ficar repetindo até a opção for a determinada pelo usuário " while opcao != 0 " if ñ repetira 
#while opcao != 0: #Enquanto a opção for diferente de 0 ele irá continuar dentro do menu
#    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n"))

#    if opcao == 1:
#       print("Sacando...")
#    elif opcao == 2:
#        print("Exibindo o extrato...")
#    elif opcao == 0:
#        print("Obrigado por usar nosso sistema bancário")
#    elif opcao >= 3 or opcao < 0: # Correção na sintaxe do else e remoção da condição opcao < 0
#        print("Número errado, tente novamente:")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Estrutura Repetição "break":


    
#while True:
#    numero = int(input("Informe um número: "))

#    if numero == 10:
#        break #Se o valor comentado for 10 para a operação

#    if numero % 2 == 0:
#        continue # pula o 10

#    print(numero)


#for numero in range(100):
#    if numero % 2 == 0:
#        continue

#    print(numero, end=" ")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------#