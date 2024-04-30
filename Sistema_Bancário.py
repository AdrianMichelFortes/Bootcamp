Menu="""
=============================================

    Bem vindo ao nosso sistema bancário:

            [1]Depositar
            [2]Sacar
            [3]Extrato
            [4]Sair
=============================================
    """

print(Menu)

saldo = 0
numero_saques= 0
extrato=""

while True:

    x=int(input("Digite um numero:"))

    if x==1:
        print("Você possui um saldo de: ",saldo)
        valor=int(input("informe o valor do deposito:"))

        if valor >0:
            saldo+=valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Numero invalido")
    elif x==2:
        print("Você possui um saldo de: ",saldo)
        y=int(input("Digite o valor que deseja sacar: "))

        if y>saldo:
            print("Você não tem saldo suficiente")
        elif y>=500:
            print("Você não pode sacar esse valor, seu limite é R$500 por saque")
        elif numero_saques>=3:
            print("Você já excedeu numero de saques hoje")
        elif y>0:
            saldo -= y
            extrato += f"Saque: R${y:.2f}\n"
            numero_saques = numero_saques + 1
        else:
            print("Operação invalida")

    elif x==3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif x==4:
        break
    else:
        print("Numero incorreto tente novamente: ")
