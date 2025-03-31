def media_valores_0(*args):
    soma = 0
    elementos = 0

    for value in args:
        soma += value
        elementos += 1

    return soma / elementos


def media_valores_1(*args):
    tamanho = len(args)
    total = 0

    for value in args:
        total += value / tamanho

    return total


def media_valores_2(*args):
    return sum(args) / len(args)


if __name__ == "__main__":
    from random import randint

    for i in range(100):
        tamanho = randint(1, 20)
        sinal = [randint(0, 100) for _ in range(tamanho)]

        a = round(media_valores_0(*sinal), 4)
        b = round(media_valores_1(*sinal), 4)
        c = round(media_valores_2(*sinal), 4)

        print(a, b, c)
        assert a == b == c
