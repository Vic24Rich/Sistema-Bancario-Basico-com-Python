# Sistema Bancário com Python

# Variáveis a serem usadas no código
saldo = 0
num_saques = 0
extrato = ""
LIMITE_SAQ_DIARIO = 500
LIMITE_SAQUES = 3

# Apresentação gráfica das opções do usuário
print("""
++++++++++++++++++++++++++++++++++++++++++++++++++
            BEM VINDO AO BANCO COD-DEV
++++++++++++++++++++++++++++++++++++++++++++++++++
    SELECIONE UMA DAS OPÇÕES:
        - D = DEPÓSITO
        - E = EXTRATO
        - S = SAQUE
        - Q = SAIR DO PROGRAMA
++++++++++++++++++++++++++++++++++++++++++++++++++
""")
# Escolha das opções de oprações a serem feitas no banco.
while True:
    opcao = input("Escreva uma das opçoes: ")

    # Operação de depósito.
    if opcao == "D":
        print("Bem vindo a aba de depósito!")
        deposito = float(input("Digite o valor a ser depositado: R$"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Valor depositado de R$ {deposito:.2f}\n"
            print("Depósito realizado.")
        else:
            print("Operação inválida")

    # Operação de apresentar o extrato
    elif opcao == "E":
        print(f"""
++++++++++++++++++++++++++++++++++++++++++++++++++
Essas operações feitas:
{extrato}
++++++++++++++++++++++++++++++++++++++++++++++++++""")

    # Operação de saques
    elif opcao == "S":
            print(f"Lembre-se que você tem um limite de {LIMITE_SAQUES} por dia,\nsendo um limite de R${LIMITE_SAQ_DIARIO}\nSeu saldo em conta é de R$ {saldo}")
            saque = float(input("Digite o valor a ser sacado: R$"))
            if saque > 0:
                num_saques += 1
                extrato += f"Você fez uma saque de R$ {saque}\n"
            elif num_saques >= LIMITE_SAQ_DIARIO:
                print("Não poderão ser feitos mais saques")
            elif saque < saldo:
                print("Saldo insuficiente.")
            elif saque <= saldo:
                print("Saque liberado!")
            else:
                print("Operação invalida!")

    # Sair do programa.
    elif opcao == "Q":
        break

    # Caso programe apresente algum erro ou valor digitado errado, essa será a mensagem mostrada.
    else:
        print("Operação inválida, selecione uma operação válida!")