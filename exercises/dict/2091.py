while True:
    n = int(input())
    if n == 0:
        break
    entrada = list(map(int, input().split()))
    x = entrada[0]
    for i in range(1, n):
        x ^= entrada[i]
    print(x)