"""
Criando tuplas
Tuplas são estruturas de dados muito parecidas com as listas, a
principal diferença é que tuplas são imutáveis enquanto listas
são mutáveis. Podemos criar tuplas através da classe tuple, ou
colocando valores separados por vírgula de parenteses.
"""

#Exemplo
frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil")

#Exemplo
frutas = ("maçã", "laranja", "uva", "pera")
frutas [0] # maçã
frutas [2] # uva

"""
Tuplas aninhadas
Tuplas podem armazenar todos os tipos de objetos Python,
portanto podemos ter tuplas que armazenam outras tuplas.
Com isso podemos criar estruturas bidimensionais (tabelas), e
acessar informando os índices de linha e coluna.
"""