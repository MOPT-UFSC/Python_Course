from math import gcd


def add_fraction(n1, d1, n2, d2):
    nr = n1 * d2 + n2 * d1
    dr = d1 * d2
    return nr, dr


def sub_fraction(n1, d1, n2, d2):
    nr = n1 * d2 - n2 * d1
    dr = d1 * d2
    return nr, dr


def mul_fraction(n1, d1, n2, d2):
    nr = n1 * n2
    dr = d1 * d2
    return nr, dr


def div_fraction(n1, d1, n2, d2):
    nr = n1 * d2
    dr = n2 * d1
    return nr, dr


def simplify_fraction(n, d):
    gcd_fraction = gcd(n, d)
    nr = n // gcd_fraction
    dr = d // gcd_fraction
    return nr, dr


n = int(input())

for _ in range(n):
    line = input().split()
    n1 = int(line[0])
    d1 = int(line[2])
    op = line[3]
    n2 = int(line[4])
    d2 = int(line[6])

    nr = 1
    dr = 1

    if op == "+":
        nr, dr = add_fraction(n1, d1, n2, d2)

    elif op == "-":
        nr, dr = sub_fraction(n1, d1, n2, d2)
    
    elif op == "*":
        nr, dr = mul_fraction(n1, d1, n2, d2)

    elif op == "/":
        nr, dr = div_fraction(n1, d1, n2, d2)
    
    else:
        print("deu merda")
    
    ns, ds = simplify_fraction(nr, dr)

    print(f"{nr}/{dr} = {ns}/{ds}")
