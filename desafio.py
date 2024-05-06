menu = """
Insira uma operação:

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Insira o valor de depósito: "))

        if valor > 0:
        
            saldo += valor
            extrato += f"Depósito: R$ {saldo:.2f}\n"
            if valor > 0:
                print("\nDepósito realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "1":
        valor = float(input("Insira o valor de saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite.")

        elif excedeu_saque:
            print("Operação falhou! O limite de saques diários foi excedido.")
        

        elif valor > 0:
            print("\nSaque Realizado com sucesso!")
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
       
         
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "2":
        print("\n=========EXTRATO=========")
        print("Não foram realizadas operações!" if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("\n=========================")
    
    elif opcao == "3":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")