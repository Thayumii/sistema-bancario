saldo = 200
limite_saque = 500
transacoes = []
saques_diarios = 0
limite_saques_diarios = 3

# OPERAÇÃO DE DEPÓSITO:
def depositar():
    global saldo
    valor = float(input("Informe o valor do depósito: R$"))
    if valor > 0:
        saldo += valor
        transacoes.append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")

# OPERAÇÃO DE SAQUE:
def sacar():
    global saldo, saques_diarios
    if saques_diarios >= limite_saques_diarios:
        print("Limite de saques diários atingido.")
    else:
        valor = float(input("Informe o valor do saque: R$"))
        if valor > limite_saque:
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
def extrato():
    if not transacoes:
        print("Não foram realizadas movimentações.")
    else:
        print("\nExtrato:")
        for transacao in transacoes:
            print(transacao)
        print(f"\nSaldo atual: R${saldo:.2f}")

while True:
    print("\n===== MENU =====")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        depositar()

    elif opcao == "2":
        sacar()

    elif opcao == "3":
        extrato()
    
    elif opcao == "4":
        print("Saindo do sistema bancário.")
        break

    else:
        print("Opção inválida. Tente novamente.")