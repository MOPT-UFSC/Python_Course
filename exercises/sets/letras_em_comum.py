palavra1 = input().replace(" ", "")
palavra2 = input().replace(" ", "")

letras_em_comum = set(palavra1).intersection(palavra2)

print(list(letras_em_comum))