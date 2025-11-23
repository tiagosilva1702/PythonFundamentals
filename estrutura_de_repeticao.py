# identacao e blocos de código
"""for i in range(5):
    print(f"Iteração {i}")
    if i % 2 == 0:
        print(f"{i} é um número par")
    else:
        print(f"{i} é um número ímpar")
"""
saldo = 1000

'''def sacar(valor):
    
    if valor <= saldo:
        saldo -= valor
        print(f"Saque de {valor} realizado com sucesso. Saldo restante: {saldo}")
    else:
        print("Saldo insuficiente para saque.")
'''
# If else python
opcao = int(input("Escolha uma opção: [1] Sacar [2] Depositar [3] Extrato [4] Sair "))
if opcao == 1:
    valor = float(input("Informe a quantia para saque: "))
    saldo -= valor;
    print(f"Saque de {valor} realizado com sucesso. Saldo restante: {saldo}")
elif opcao == 2:
    valor = float(input("Informe a quantia para depósito: "))
    saldo += valor;
    print(f"Depósito de {valor} realizado com sucesso.")
    print(f"Seu saldo atual é de {saldo}.")
elif opcao == 3:
    print(f"Seu saldo é de {saldo}.")
elif opcao == 4:
    print("Saindo do sistema.") 