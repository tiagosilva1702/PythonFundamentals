'''while True:
    comando = input("Digite 'sair' para encerrar o loop: ")
    if comando.lower() == 'sair':
        break
'''
# Exemplo com continue usando for divisão por 2 para exibir apenas números ímpares
# % 2 == 1 número par ou seja, resto da divisão por 2 é 1
for numero in range(10):
    if numero % 2 == 0:
        continue
    print(numero)