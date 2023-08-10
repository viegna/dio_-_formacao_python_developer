menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=>"""

saldo = 0
limite = 500
extrato = "";
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if(opcao) == "d":
        print("Depósito")
        valor = float(input("Digite o valor de depósito"))

        if valor >= 0:
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"
        else:
            print("Operação falhou: Valor inválido.")
    elif(opcao) == "s":
        print("Sacar")
        valor = float(input("Digite o valor de saque"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou: Saldo excedido")
        elif excedeu_limite:
            print("Operação falhou: valor de saque excede limite")
        elif excedeu_saque: 
            print("Operação falhou: excedeu o numero de saques")

        elif valor >0:
            saldo -= valor;
            extrato += f"Saque de: R$ {valor:.2df}\n"
            numero_saques += 1

        else:
            print("Operação falhou: o valor informado é invalido")


    elif(opcao) == "e":
        print("Extrato")
        print("-----------------------------------------------------")
        print("Não houveram transações" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("-----------------------------------------------------")

    elif(opcao) == "q":
        print("Sair")
        break
        
    else:
        print("Operação Inválida")