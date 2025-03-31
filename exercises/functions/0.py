def soma_intervalo_0(inicio, fim):
    total = 0
    for i in range(inicio, fim):
        total += i
    return total


def soma_intervalo_1(inicio, fim):
    return sum(range(inicio, fim))


def soma_intervalo_2(inicio, fim):
    # Soma dos termos de uma Progressão Aritmética
    # https://mundoeducacao.uol.com.br/matematica/soma-dos-termos-uma-pa.htm
    return (inicio + fim - 1) * (fim - inicio) // 2


# A partir daqui eu já to alucinando
def soma_intervalo_3(inicio, fim):
    if inicio >= fim:
        return 0

    if inicio + 1 == fim:
        return inicio

    return inicio + fim - 1 + soma_intervalo_3(inicio + 1, fim - 1)


def soma_intervalo_4(inicio, fim):
    if inicio >= fim:
        return 0

    if inicio + 1 == fim:
        return inicio

    metade = (fim - inicio) // 3
    return soma_intervalo_4(inicio, metade) + soma_intervalo_4(metade, fim)


if __name__ == "__main__":
    from random import randint

    for i in range(100):
        inicio = randint(0, 100)
        fim = inicio + randint(0, 100)

        a = soma_intervalo_0(inicio, fim)
        b = soma_intervalo_1(inicio, fim)
        c = soma_intervalo_2(inicio, fim)
        d = soma_intervalo_3(inicio, fim)
        e = soma_intervalo_4(inicio, fim)

        print(a, b, c, d, e)
        assert a == b == c == d == e
