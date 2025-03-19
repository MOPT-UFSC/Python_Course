cv, ce, cs, fv, fe, fs = map(int, input().split())

c_pontos = cv * 3 + ce
f_pontos = fv * 3 + fe

if c_pontos > f_pontos:
    print("C")
elif f_pontos > c_pontos:
    print("F")
else:
    if cs > fs:
        print("C")
    elif fs > cs:
        print("F")
    else:
        print("=")