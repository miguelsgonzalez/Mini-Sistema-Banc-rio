extrato = 0
executando = True
qtdSaque = 0

usuarios = []

contas = []

numero_conta = 1


def depositar(valor):
    global extrato
    extrato = extrato + valor


def sacar(valor):
    global extrato
    extrato = extrato - valor


def mostrar_extrato():
    return print(f"Seu extrato é de {extrato}")


def cadastrar_usuario():
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento: ")
    cpf = input("Digite o CPF: ")

    cpf = ''.join(c for c in cpf if c.isdigit())

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Esse CPF já está cadastrado!")
            return

    endereco = input("Digite o endereço: ")

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")


def criar_conta():
    global numero_conta

    cpf = input("Digite o CPF do usuário: ")

    cpf = ''.join(c for c in cpf if c.isdigit())

    for usuario in usuarios:

        if usuario["cpf"] == cpf:

            conta = {
                "agencia": "0001",
                "numero": numero_conta,
                "usuario": usuario
            }

            contas.append(conta)

            print("Conta criada com sucesso!")
            print(f"Agência: {conta['agencia']}")
            print(f"Número da conta: {conta['numero']}")

            numero_conta = numero_conta + 1

            return

    print("Usuário não encontrado!")


while executando:
    print("""
    --------------------MENU--------------------

    1 - Depósito
    2 - Saque
    3 - Extrato
    4 - Cadastrar novo usuário
    5 - Criar conta corrente
    6 - Sair

    --------------------------------------------
    """)

    i = 0
    acao = int(input())

    if acao == 1:
        
        deposito = float(input("Qual valor deseja depositar?"))
        if deposito<=0:
            print("Esse valor não é possível!")
                
        else:
            depositar(deposito)
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
            sacar(saque)
            print("O valor foi sacado!")
            qtdSaque = qtdSaque + 1
               


    elif acao == 3:
        mostrar_extrato()


    elif acao == 4:
        cadastrar_usuario()


    elif acao == 5:
        criar_conta()


    elif acao == 6:
        executando = False

    else:
        print("Essa não é uma ação executável!")