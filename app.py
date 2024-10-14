class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        # Inicializa um usuário com nome, cpf, data de nascimento e endereço.
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

    def __str__(self):
        # Retorna uma string representando o usuário.
        return f"Nome: {self.nome}, CPF: {self.cpf}"

class ContaCorrente:
    numero_conta_sequencial = 1  # Variável global.

    def __init__(self, usuario):
        # Cria uma conta corrente para um usuário.
        self.agencia = "0001"
        self.numero = ContaCorrente.numero_conta_sequencial
        self.usuario = usuario
        self.saldo = 0
        self.limite_saque = 500
        self.transacoes = []  # Lista para armazenar transações da conta.
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
        ContaCorrente.numero_conta_sequencial += 1

    def depositar(self, valor):
        # Realiza um depósito na conta, se o valor for válido.
        if valor > 0:
            self.saldo += valor
            self.transacoes.append(f"Depósito: R${valor:.2f}")  # Registra a transação.
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        # Realiza um saque da conta, respeitando limites de saque e saldo disponível.
        if self.saques_diarios >= self.limite_saques_diarios:
            print("Limite de saques diários atingido.")
        elif valor > self.limite_saque:
            print(f"O limite por saque é de R${self.limite_saque:.2f}")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > 0:
            self.saldo -= valor
            self.saques_diarios += 1
            self.transacoes.append(f"Saque: R${valor:.2f}")  # Registra a transação.
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do saque deve ser positivo.")

    def exibir_extrato(self):
        # Exibe o extrato da conta, mostrando transações e saldo atual.
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            print("\nExtrato:")
            for transacao in self.transacoes:
                print(transacao)
            print(f"\nSaldo atual: R${self.saldo:.2f}")

class Banco:
    def __init__(self):
        # Inicializa o banco com listas para armazenar usuários e contas.
        self.usuarios = []
        self.contas = []

    def criar_usuario(self, nome, cpf, data_nascimento, endereco):
        # Cria um novo usuário, se o CPF não estiver cadastrado.
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                print("Erro: CPF já cadastrado.")  # Verifica se o CPF já está registrado.
                return
        usuario = Usuario(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} cadastrado com sucesso.")

    def criar_conta_corrente(self, cpf):
        # Cria uma conta corrente para um usuário com CPF válido.
        usuario = next((user for user in self.usuarios if user.cpf == cpf), None)
        if not usuario:
            print("Erro: Usuário não encontrado.")
            return
        conta = ContaCorrente(usuario)
        self.contas.append(conta)
        print(f"Conta corrente número {conta.numero} criada para o usuário {usuario.nome}.")

    def buscar_conta(self, cpf):
        # Busca a conta associada a um CPF e retorna a conta ou None se não encontrada.
        for conta in self.contas:
            if conta.usuario.cpf == cpf:
                return conta
        return None

# Menu principal com as operações do sistema bancário.
def menu():
    banco = Banco()  # Instancia o banco.

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
            # Realiza um depósito, se a conta for encontrada.
            cpf = input("Informe o CPF do titular: ")
            conta = banco.buscar_conta(cpf)
            if conta:
                try:
                    valor = float(input("Informe o valor do depósito: R$"))
                    conta.depositar(valor)
                except ValueError:
                    print("Erro: valor inválido.")
            else:
                print("Conta não encontrada.")

        elif opcao == "2":
            # Realiza um saque, se a conta for encontrada.
            cpf = input("Informe o CPF do titular: ")
            conta = banco.buscar_conta(cpf)
            if conta:
                try:
                    valor = float(input("Informe o valor do saque: R$"))
                    conta.sacar(valor)
                except ValueError:
                    print("Erro: valor inválido.")
            else:
                print("Conta não encontrada.")

        elif opcao == "3":
            # Exibe o extrato da conta do usuário.
            cpf = input("Informe o CPF do titular: ")
            conta = banco.buscar_conta(cpf)
            if conta:
                conta.exibir_extrato()
            else:
                print("Conta não encontrada.")

        elif opcao == "4":
            # Cria um novo usuário.
            nome = input("Informe o nome do usuário: ")
            cpf = input("Informe o CPF (somente números): ")
            data_nascimento = input("Informe a data de nascimento (DD/MM/AAAA): ")
            endereco = input("Informe o endereço: ")
            banco.criar_usuario(nome, cpf, data_nascimento, endereco)

        elif opcao == "5":
            # Cria uma nova conta corrente para um usuário existente.
            cpf = input("Informe o CPF do usuário para vincular a conta: ")
            banco.criar_conta_corrente(cpf)

        elif opcao == "6":
            print("Saindo do sistema bancário.")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()