palavra1 = input()
palavra2 = input()
palavra3 = input()

if palavra1.lower() == "vertebrado":
    if palavra2.lower() == "ave":
        if palavra3.lower() == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if palavra3.lower() == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if palavra2.lower() == "inseto":
        if palavra3.lower() == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if palavra3.lower() == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
