opcao = -1

while opcao != 0:
    print("\nMenu:")
    print("[1] Dizer Olá")
    print("[2] Dizer Adeus")
    print("[0] Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print("Olá!")
    elif opcao == 2:
        print("Adeus!")
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente.")