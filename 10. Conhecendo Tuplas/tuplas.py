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

#Exemplo
matriz = (
(1, "a", 2),
("b", 3, 4),
(6, 5, "c"),
)
matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz [-1][-1]# "c
#Tuplas anin

Exemplo
tupla = ("p", "y", "+", "h", "o", "n",)
tupla[2:] # ("t""h", "", "n")
tupla[:2]# ("p", "y")
tupla[1:3] # ("y"t")
tupla[0:3:2] # ("p","t")
tupla[::] # ("p", "y", "t""h". "o". "n")
tupla[::-1] # ("n", "o","h","+" "y", "p")