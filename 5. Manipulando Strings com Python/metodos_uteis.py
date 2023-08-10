curso = "pYtHon"
print(curso.upper( ))
#>>> PYTHON
print(curso.lower )
#>>> python
print(curso.title())
#>>> Python

curso = "    Python"
print (curso.strip())
#>>> "Python"
print (curso.lstrip())
#>>> "Python"
print(curso.rstrip())
#>>> "   Python"

curso = "Python"
print (curso.center(10, "#"))
#>›> "##Python##
print(".".join(curso))
#>>> "P.y.t.h.o.n"

nome = "gUIlherME"
print(nome. upper())
print (nome. lower())
print (nome. title())
texto = "olá mundo!"
print (texto + ".")
print(texto. strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")
menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))
