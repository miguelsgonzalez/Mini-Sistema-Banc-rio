extrato = 0
executando = True
qtdSaque = 0
while executando == True:
    print("""
    --------------------MENU--------------------

    1 - Depósito
    2 - Saque
    3 - Extrato
    4 - Sair

    --------------------------------------------
    """)

    i = 0
    acao = int(input())

    if acao == 1:
        
        deposito = float(input("Qual valor deseja depositar?"))
        if deposito<=0:
            print("Esse valor não é possível!")
                
        else:
            extrato = extrato + deposito
            print("O valor foi depositado!")
               

    elif acao == 2:
        
        saque = float(input("Qual valor deseja sacar?"))
        if qtdSaque == 3:
                print("Você não pode mais realizar saques! O limite diário é de 3!")
              
        elif saque<=0:
            print("Esse valor não é possível!")
                
        elif saque > 500:
            print("O limite do saque é de 500 reais!")
               
        elif saque>extrato:
            print("Você não tem saldo suficiente!")
                
        else:
            extrato = extrato - saque
            print("O valor foi sacado!")
            qtdSaque = qtdSaque + 1
               


    elif acao == 3:
        print(f"Seu extrato é de:R${extrato}")

    elif acao == 4:
        executando = False

    else:
        print("Essa não é uma ação executável!")