# Sistema Bancário - Versão 1

Este projeto foi desenvolvido como parte de um desafio proposto pela **DIO (Digital Innovation One)**. O objetivo é implementar um sistema bancário simples em Python que permita realizar operações básicas, como depósito, saque e visualização de extrato.

## Funcionalidades
- **Depósito**: Permite ao usuário adicionar um valor positivo à conta bancária.
- **Saque**: Limite de três saques diários com o valor máximo de R$500,00 por saque. Caso o saldo seja insuficiente ou o limite de saques seja excedido, o sistema exibirá mensagens apropriadas.
- **Extrato**: Exibe todas as transações (saques e depósitos) realizadas, além do saldo atual. Se não houver movimentações, uma mensagem será exibida.

## Regras do Desafio
1. O sistema deve permitir apenas depósitos de valores positivos.
2. O saque tem um limite diário de três transações e de R$500,00 por saque.
3. As operações de saque e depósito devem ser registradas e exibidas no extrato.
4. O saldo deve ser atualizado corretamente a cada operação.
