#for
texto = input ("Informe um texto: ")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
print( ) # adiciona uma quebra de linha

#Utilizando range com for
for numero in range(0, 11):
    print (numero, end=" ")
#››› 0 12 3 4567 89 10

# exibindo a tabuada do 5
#for numero in range(start, end, step):
for numero in range(0, 51, 5):
    print (numero, end=" ")
#››› 0 5 10 15 20 25 30 35 40 45 50


while True:
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        continue
    
    if numero == 10:
        break


    print (numero)
