# Função para verificar se B corresponde aos últimos dígitos de A
def verifica_encaixe(A, B):
    if len(B) > len(A):
        return "nao encaixa"
    
    if A[-len(B):] == B:
        return "encaixa"
    else:
        return "nao encaixa"

# Leitura da quantidade de casos de teste
N = int(input())

# Loop para processar cada caso de teste
for _ in range(N):
    A, B = input().split()
    resultado = verifica_encaixe(A, B)
    print(resultado)