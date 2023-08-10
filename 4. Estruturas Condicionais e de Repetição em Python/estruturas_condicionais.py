#Exemplo
saldo = 2000.0
saque = float (input( "Informe o valor do saque: "))
if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")


MAIOR_IDADE  = 18
IDADE_ESPECIAL = 12
idade = int(input("Informe sua idade:"))
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")
if idade >= MAIOR_IDADE:
    print("Malor de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CNH.")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade <= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
    print("Ainda não pode tirar a CNH.")