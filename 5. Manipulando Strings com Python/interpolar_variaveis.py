#Old style %
nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
print("Olá, me chamo %. Eu tenho %d anos de idade, trabalho como %5 e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))
#>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
print ("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.". format (nome, idade, profissao,linguagem))
print ("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} estou matriculado no curso de {o}.". format (linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho fidade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem} ." .format (nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Olá, me chamo {nome}. Eu tenho (idade} anos de idade, trabalho como {profissao] e estou matriculado no curso de {linguagem}." .format (**profissao))
#›> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.

#f-string
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
print (f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
#>>> Olá, me chamo Guilherme. Eu tenho 28 anos de idade, trabalho como Progamador e utilizo e estou matriculado no curso de Python.

#Formatar strings com f-string
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")
#››› "Valor de PI: 3.14"
print (f"Valor de PI: {PI: 10.2f}")
#››› "Valor de PI: 3.14"

nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem - "Python"
dados = {"nome": "Guilherme", "idade": 28}
print("Nome: %s Idade: %d" + (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}". format(idade, nome))
print ("Nome: {nome} Idade: {idade}".format(none=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}". format (**dados) )
print ("Nome: {nome} Idade: {idade}")

nome = "Guilherme Arthur de Carvalho"
nome [0]
nome[:99]
#>>>"Gultherme"
nome [10:]
#"Arthur de Carvalho*
nome [10:16]
#"Arthur*
nome [10:16:2]
#"Atu"
nome [:]
#"Guilherme Arthur de Carvalho"
nome [::-1]
#"ohlavrac ed ruhtrA emrehliuG*

nome = "Guilherme Arthur de Carvalho"
print (nome[0])
print (nome[-1])
print (nome [:9])
print (nome [10:1])
print (nome [10:161])
print(nome [10:16:2])
print (nome[:])
print(nome[::-1])