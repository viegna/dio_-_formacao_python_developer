"""O que são?
São operadores utilizados em conjunto com os operadores de
comparação, para montar uma expressão lógica. Quando um
operador de comparação é utilizado, o resultado retornado é
um booleano, dessa forma podemos combinar operadores de
comparação com os operadores lógicos, exemplo:
op_comparacao + op_logico + op_comparacao... N...
"""

#Exemplo
saldo = 1000
saque = 200
limite = 100
saldo >= saque
#>>> True
saque <= limite
#››> False

#Parênteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True
saldo >= saque and saque <= limite or conta_especial and saldo >= saque
#››> True
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#››› True

print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)
saldo = 1000
saque = 250
limite = 200
conta_especial * True
exp = saldo >= saque and saque <=  limite or conta_especial and saldo >= saque
print(exp)
exp_2 = (saldo >= saque and saque <= limite)
print (exp_2)
