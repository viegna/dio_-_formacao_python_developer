#Exemplo
set ([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
set ("abacaxi")
# {"b", "a", "c""x"', "i"}
set(("palio", "gol", "celta", "palio"))
# {"gol", "celta", "palio"}

{}.union #unir ambos
conjunto_a = {1, 2}
conjunto_b = {3, 4}
conjunto_a. union (conjunto_b) # {1, 2, 3, 4}

{}.intersection # os iguais
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_a.intersection (conjunto_b) # {2, 3}

{}.difference # os diferentes entre 1 ou outro
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_a.difference (conjunto_b)
conjunto_b.difference (conjunto_a)
# {1}
# {4}

{}.symmetric_diff #os diferentes entre ambos
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_a.symmetric_difference(conjunto_b)

{}.issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
conjunto_a.issubset (conjunto_b) #se todos elementos em a estão em b
conjunto_b.issubset (conjunto_a)
# True
# False

{}.issuperset 
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
conjunto_a.issuperset (conjunto_b) # False # se b esta dentro de a
conjunto_b.issuperset (conjunto_a) # True

{}.isdisjoint # se os conjuntos não se tocam, todos os elementos de um conjunto não estão presentes no outro
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
conjunto_a.isdisjoint (conjunto_b) # True
conjunto_a.isdisjoint (conjunto_c)
# False

{}.add
sorteio = {1, 23}
sorteio.add (25) # {1, 23, 25}
sorteio.add (42) # {1, 23, 25, 42}
sorteio. add (25)
# {1, 23, 25, 42).

sorteio = {1, 23}
sorteio # {1, 23}
sorteio.copy()
sorteio # {1, 23}

sorteio = {1, 23}
sorteio # {1, 23}
sorteio.clear()
sorteio # 

{}. discard
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard (1)
numeros.discard (45)
numeros
# {2, 3, 4, 5, 6, 7, 8, 9, 0}

{}.рор #tira todos os valores iguais ao primeiro da lista
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros. pop ()
# 0
numeros. pop ( )
# 1
numeros
# {2. 3. 3. 4. 5. 6. 7. 8. 91

{}.remove #remove o valor imposto
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
numeros
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros. remove (0) # 0
numeros
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

#len
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
len (numeros) # 10

#in
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
1 in numeros # True
10 in numeros
# False