# Sistema Bancário - Versão 2

Este projeto foi desenvolvido como parte de um desafio proposto pela **DIO (Digital Innovation One), ele implementa um sistema bancário simples utilizando Python**. A versão 2 traz melhorias e novas funcionalidades, como a criação de usuários, contas correntes e a modularização das operações bancárias.

## Funcionalidades
1. **Criar Usuário (Cliente do Banco)**:
   - O sistema permite criar um usuário informando `nome`, `CPF`, `data de nascimento` e `endereço`.
   - O CPF é único para cada usuário e a validação impede cadastros duplicados.
   - Os usuários são armazenados em uma lista.

2. **Criar Conta Corrente**:
   - O sistema permite vincular uma conta corrente a um usuário existente.
   - Cada conta é composta por `agência`, `número da conta` e `usuário`.
   - Um usuário pode ter mais de uma conta, e o número da conta é gerado automaticamente.
  
3. **Operações Bancárias**:
   - **Depósito**: Permite realizar depósitos na conta bancária, atualizando o saldo e registrando a transação.
   - **Saque**: Realiza saques respeitando o limite diário de saques e o valor máximo permitido por saque.
   - **Extrato**: Exibe o histórico de transações (depósitos e saques) e o saldo atual da conta.
  
## Melhorias na Modularização:

- As operações de saque, depósito e exibição de extrato foram separadas em funções específicas para melhor organização e manutenção do código.
- Foram criadas funções para **criar usuário** e **criar conta corrente**, tornando o código mais modular.

## Regras do Desafio
1. O sistema deve permitir apenas depósitos de valores positivos.
2. O saque tem um limite diário de três transações e de R$500,00 por saque.
3. As operações de saque e depósito devem ser registradas e exibidas no extrato.
4. O saldo deve ser atualizado corretamente a cada operação.
