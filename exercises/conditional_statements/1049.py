tipo = input()
classificacao = input()
tipo_alimentacao = input()

if tipo == "vertebrado":
    if classificacao == "ave":
        if tipo_alimentacao == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if tipo_alimentacao == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if classificacao == "inseto":
        if tipo_alimentacao == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if tipo_alimentacao == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")