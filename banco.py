# Variáveis globais.
saldo = 200
limite_saque = 500
transacoes = []
saques_diarios = 0
limite_saques_diarios = 3
usuarios = [] # Armazena os usuários(clientes).
contas = [] # Armazena as contas bancárias.
numero_conta_sequencial = 1

# OPERAÇÃO PARA CRIAR USUÁRIO.
def criar_usuario(nome, cpf, data_nascimento, endereco):
    for usuario in usuarios: # Verifica se o CPF já está cadastrado.
        if usuario['cpf'] == cpf:
            print("Erro: CPF já cadastrado.")
            return
        
# OPERAÇÃO PARA CADASTRAR O NOVO USUÁRIO.
    usuario = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    } 
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso.")   

# OPERAÇÃO PARA CRIAR CONTA CORRENTE.
def criar_conta_corrente(cpf):
    global numero_conta_sequencial
    # Verifica se o usuário com o CPF existe
    usuario = next((user for user in usuarios if user['cpf'] == cpf ), None)
    if not usuario:
        print("Erro: Usuário não encontrado.")
        return

    # Cria a conta para o usuário. 
    conta = {
        "agencia": "0001",
        "numero": numero_conta_sequencial,
        "usuario": usuario
    }   
    contas.append(conta)
    numero_conta_sequencial += 1
    print(f"Conta corrente número {conta['numero']} criada para o usuário {usuario['nome']}.")    

# OPERAÇÃO DE DEPÓSITO:
def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        transacoes.append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")

# OPERAÇÃO DE SAQUE:
def sacar(valor):
    global saldo, saques_diarios
    if saques_diarios >= limite_saques_diarios:
        print("Limite de saques diários atingido.")
    elif valor > limite_saque:
        print(f"O limite por saque é de R${limite_saque:.2f}")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        saques_diarios += 1
        transacoes.append(f"Saque: R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso.")
    else:
        print("O valor do saque deve ser positivo.")

# OPERAÇÃO DE EXTRATO:
def exibir_extrato():
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        print("\nExtrato:")
        for transacao in transacoes:
            print(transacao)
        print(f"\nSaldo atual: R${saldo:.2f}")

# Menu principal.
def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Criar Usuário")
        print("5. Criar Conta Corrente")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                valor = float(input("Informe o valor do depósito: R$"))
                depositar(valor)
            except ValueError:
                print("Erro: valor inválido. Tente novamente.")

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$"))
            sacar(valor)

        elif opcao == "3":
            exibir_extrato()

        elif opcao == "4":
            nome = input("Informe o nome do usuário: ")
            cpf = input("Informe o CPF (somente números): ")
            data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
            endereco = input("Informe o endereço: ")
            criar_usuario(nome, cpf, data_nascimento, endereco)

        elif opcao == "5":
            cpf = input("Informe o CPF do usuário para vincular a conta: ")
            criar_conta_corrente(cpf)

        elif opcao == "6":
            print("Saindo do sistema bancário.")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()