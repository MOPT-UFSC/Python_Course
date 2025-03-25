from math import sqrt
from math import pi
while True:
    try:
        a, b, c = map(int, input().split())

        semiPerimetro = (a + b + c) / 2
        areaTriangulo = sqrt(semiPerimetro * (semiPerimetro - a) * (semiPerimetro - b) * (semiPerimetro - c))
        areaCirculo = pi * (areaTriangulo / semiPerimetro) ** 2

        areaCirculoMaior = pi * ( (a * b * c) / (4 * areaTriangulo)) ** 2

        print("%.4f %.4f %.4f" % (areaCirculoMaior - areaTriangulo, areaTriangulo - areaCirculo, areaCirculo))
    except EOFError:
        break