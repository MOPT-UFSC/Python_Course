def lista_dobro_0(n):
    lista = []
    for i in range(n):
        lista.append(2 * i)
    return lista


def lista_dobro_1(n):
    """
    It is not really a list like I asked in the exercise,
    cut it can be easily converted, and in some cases this
    way this approach is even better.
    """
    for i in range(n):
        yield 2 * i


def lista_dobro_2(n):
    return [2 * i for i in range(n)]


if __name__ == "__main__":
    a = lista_dobro_0(5)
    b = list(lista_dobro_1(5))
    c = lista_dobro_2(5)
    assert [0, 2, 4, 6, 8] == a == b == c