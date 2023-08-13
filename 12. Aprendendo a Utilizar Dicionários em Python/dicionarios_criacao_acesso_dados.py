#Exemplo
pessoa = {"nome": "Guilherme", "idade": 28}
pessoa = dict (nome= "Guilherme", idade=28)
pessoa["telefone"] = "3333-1234"
#"telefone"; "3333-1234"}
# {"nome": "Guilherme", "idade": 28,

#Exemplo
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
dados ["nome"] # "Guilherme"
dados ["idade"]
# 28
dados ["telefone"]
# "3333-1234"
dados["nome"] = "Maria"
dados ["idade"] = 18
dados ["telefone"] = "9988-1781"
dados
# {"nome": "Maria" "idade": 18, "telefone": "9988-1781"}

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna","telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie","telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine","telefone": "3333-7766"},
}

contatos ["giovanna@gmail.com"]["telefone"]
# "3443-2121"

contatos = {
    "guilhermedgmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine","telefone": "3333-7766"},
}

for chave in contatos:
    print (chave, contatos [chave])

{}.clear
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna","telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie","telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine","telefone": "3333-7766"},
}
contatos.clear ()
contatos
# {}

{}.copy
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}
copia = contatos. copy ()
copia[ "guilherme@gmail.com"] = {"nome": "Gui"}
contatos["guilherme@gmail.com"] # {"nome"; # {"nome": "Guilherme") "telefone""3333-2221"}
copia["guilherme@gmail.com"] # {"nome": "Gui"}

{}.fromkeys
dict. fromkeys (["nome", "telefone"]) # {"nome": None,"telefone": None}
dict. fromkeys (["nome", "telefone"], "vazio") # {"nome": "vazio", "telefone"vazio"}

{}.get
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}
contatos ["chave" ]
# KeyError
contatos.get ("chave")
# None
contatos. get ("chave", {}) # {}
contatos.get("guilherme@gmail.com",{})#{"guilherme@gmail.com":{"nome""Guilherme""telefone"; "3333-2221"}

{}.рор
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}
contatos.pop("guilherme@gmail.com") # {'nome': 'Guilherme','telefone''3333-2221'}
contatos.pop("guilherme@gmail.com", {}) # {}

resultado = contatos.pop("guilhermedgmail.com", "nao encontrou") #
print(resultado)

{}.setdefault
contato = {'nome': 'Guilherme','telefone': '3333-2221'}
contato.setdefault ("nome", "Giovanna") # "Guilherme"
contato# { 'nome':'Guilherme','telefone': '3333-2221'}
contato.setdefault ("idade", 28)
contato# {'nome';'Guilherme'# 28'telefone':'3333-2221','idade': 28}

contato = {"nome":"Guilherme","telefone":"3333-2221"}
contato.setdefault("nome", "Giovanna") # "Guilherme"
print (contato) # ('nome': 'Guilherme', 'telefone': '3333-2221')
contato.setdefault ("idade", 28) #-28
print(contato) #{'nome'; 'Guitherme' 'telefone': '3333-2221', 'idade': 28}

{}.update
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
}
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
contatos
# {'guilherme@gmail.com': {'nome': 'Gui'}}
contatos.update ({"giovanna@gmail.com": {"nome": "Giovanna", "telefone":"3322-8181"}})
contatos # {'guilherme@gmail.com': {'nome': 'Gui'), giovanna@gmail.com'{'nome': 'Giovanna''telefone': '3322-8181'}}

{}.values
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie","telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine","telefone":"3333-7766"},
}
contatos.values ()
# dict_values ([{'nome': 'Guilherme', 'telefone':'3333-2221 }, {'nome': 'Giovanna''telefone': '3443-2121'}, {'nome': 'Chappir'telefone': '3344-9871'), {'nome''Melaine''telefone'; '3333-7766'71)

#del
contatos = {
"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
"chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
"melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos ["guilherme@gmail.com"]["telefone"]
del contatos ["chappie@gmail.com"]
contatos # {'guilherme@gmail.com': ('nome': 'Guilherme '), giovanna@gmail.com' { 'nome':'Giovanna' 'telefone': '3443-2121'), 'melaine@gmail.com': {'nome { 'nome' 'Melaine' 'telefone'; '3333-7766'}}

