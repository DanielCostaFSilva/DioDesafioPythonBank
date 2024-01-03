menu= """"

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3


while True: 
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depisito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"

        else: 
            print("Operação falhou! o valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Voce não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação inválida! o Valor do saque exedeu o limite.")
        
        elif excedeu_saque: 
            print("Operação inválida! Número máximo de saque exedido.")

        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! o valor informado é inválido.")

    elif opcao == "e":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada")
