[].append
lista = [ ]
lista. append (1)
lista.append( "Python")
lista. append ([40, 30, 20])
print (lista) # [1, "Python", [40, 30, 20]]

[].clear
lista = [1, "Python", [40, 30, 20]]
print (lista)
# [1, "Python", [40, 30, 20]]
lista.clear()
print (lista)

[].сору
lista = [1, "Python", [40, 30, 20]]
lista.copy ()
print(lista) # [1, "Python", [40, 30, 20]]

lista - [1, "Python", [40, 30, 20]]
12 - lista.copy()
print(lista) # [1, "Python", [40, 30, 20]]
print(id(12), id(lista))

[].extend
linguagens = ["python", "js", "c"]
print (linguagens) # ["python", "js", "c"]
linguagens.extend (["java", "csharp"])
print (linguagens) # ["python", "js", , "c" , "java", "csharp"]

[].index
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens. index ("java") # 3
linguagens. index("python")# 0

[].pop
linguagens ="python", "js", "c", "java", "csharp"
linguagens. pop() # csharp
linguagens.pop() # java
linguagens. pop() #
linguagens.pop(0) # python

[].remove
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove ("c")
print (linguagens) # ["python", "js", "java", "csharp"]

[].reverse
linguagens = ["python", "js", "c", "java", "sharp" ]
linguagens.reverse()
print (linguagens) # ["sharp", "java","js", "python"]

[].sort
linguagens =["python","js", "C", "java", "csharp"]
linguagens. sort() # ["c", "csharp", "java", "js", "python"]
linguagens= ["python", "js","java", "csharp"]
linguagens. sort (reverse=True) # ["python", "js", "java", "sharp", "C" ]
linguagens =["python", "js","java", "csharp"]
linguagens. sort (key=lambda X: len(linguagens)) # ["c", "js", "java", "python", "csharp"
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens. sort (key=lambda X: len(linguagens), reverse=True) # ["python", "csharp","java", "js", "c"']

sorted
linguagens = ["python", "js", "java", "csharp"]
sorted (linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python", "sharp" ]
sorted (linguagens, key=lambda x: len(x), reverse=True) # ["python", "csharp", "java", "js",

linguagens = ["python", " js" "c", "java", "csharp"]
print(sorted(linguagens, key=lambda x: len(x))) # ["c*, "js", "java", "python", "esharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # ["python", "sharp", "java" "js", "c*]
print (sorted(linguagens))