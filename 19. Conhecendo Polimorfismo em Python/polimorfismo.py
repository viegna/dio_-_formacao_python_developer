len ("python" )
len ([10, 20, 30])

"""
Na herança, a classe filha herda os métodos da classe pai. No
entanto, é possível modificar um método em uma classe filha
herdada da classe pai. Isso é particularmente útil nos casos em
que o método herdado da classe pai não se encaixa
perfeitamente na classe filha.
"""

class Passaro:
    def voar (self): pass
class Pardal(Passaro):
    def voar (self):
        print("Pardal voa")
class Avestruz (Passaro):
    def voar (self):
        print ("Avestruz não voa")
def plano_de_voo (passaro):
    passaro.voar()
plano_de_voo(Pardal ())
plano_de_voo (Avestruz ())