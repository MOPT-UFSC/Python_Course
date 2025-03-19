l, a, p, r = map(int, input().split())

diagonal_caixa = (l ** 2 + p ** 2 + a ** 2) ** 0.5
diametro_esfera = 2 * r

if diagonal_caixa > diametro_esfera:
    print("N")
else:
    print("S")