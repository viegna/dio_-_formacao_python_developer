"""
O que são funções?
Função é um bloco de código identificado por um nome e pode
receber uma lista de parâmetros, esses parâmetros podem ou
não ter valores padrões. Usar funções torna o código mais
legível e possibilita o reaproveitamento de código. Programar
baseado em funções, é o mesmo que dizer que estamos
programando de maneira estruturada.
"""

#Exemplo
def exibir_mensagem() :
    print("Olá mundo!")
def exibir_mensagem_2(nome) :
    print (f"Seja bem vindo {nome}!")
def exibir_mensagem_3 (nome= "Anônimo"):
    print (f"Seja bem vindo {nome}!")
exibir_mensagem ()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3 (nome="Chappie")