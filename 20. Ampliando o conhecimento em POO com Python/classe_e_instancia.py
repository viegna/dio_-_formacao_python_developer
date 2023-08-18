class Estudante:
    escola = "DIO"
def _init_(self, nome, numero) :
    self. nome = nome
    self. numero = numero
def str (self):
    return f"{self .nome} (self.numerol) - (self.escola?"
gui = Estudante("Guilherme", 56451)
gi = Estudante ("Giovanna", 17323)

"""
Métodos de classe estão ligados à classe e não ao objeto. Eles
têm acesso ao estado da classe, pois recebem um parâmetro
que aponta para a classe e não para a instância do objeto.
"""

"""
Um método estático não recebe um primeiro argumente
explícito. Ele também é um método vinculado à classe e não ac
objeto da classe. Este método não pode acessar ou modificar (
estado da classe. Ele está presente em uma classe porque fai
sentido que o método esteja presente na classe.
"""