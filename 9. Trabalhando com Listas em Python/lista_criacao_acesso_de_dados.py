"""
Listas em Python podem armazenar de maneira sequencial
qualquer tipo de objeto. Podemos criar listas utilizando o
construtor list, a função range ou colocando valores separados
por vírgula dentro de colchetes. Listas são objetos mutáveis,
portanto podemos alterar seus valores após a criação.
"""

frutas = ["laranja", "maca", "uva"]
frutas = []
letras = list ("python")
numeros = list (range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

frutas = ["maçã", "laranja", "uva", "pera"]
frutas [-1] # pera
frutas [ - 3] # laranja

"""
Listas aninhadas
Listas podem armazenar todos os tipos de objetos Python,
portanto podemos ter listas que armazenam outras listas. Com
isso podemos criar estruturas bidimensionais (tabelas), e
acessar informando os índices de linha e coluna.
"""

matriz = [
[1, "a", 2],
["b", 3, 4],
[6, 5, "c"]
]

matriz[0] # [1, "a", 2] linha especifica
matriz[0][0] # 1 linha e coluna especifica
matriz[0][-1] # 2
matriz[-1][-1] # c

lista = ["p", "y", "t", "h", "o", "n"]
lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"] inicial final e step
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n","o,"h',"t","y", "p"]

#Filtro versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]

#Modificando valores versão
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append (numero ** 2)
    print(quadrado)