while True:
    n = int(input())
    if n == 0:
        break

    valores = list(map(int, input().split()))

    copia = valores.copy()
    copia.sort(reverse=True)
    segundo_maior = copia[1]

    for i in range(len(valores)):
        if valores[i] == segundo_maior:
            print(i + 1)
            break
    
















# while True:
#     n = int(input())
#     if n == 0:
#         break

#     valores = list(map(int, input().split()))

#     index_maior = 0 if valores[0] > valores[1] else 1
#     index_seg_maior = 1 if valores[0] > valores[1] else 0
#     for i in range(2, n):
#         if valores[i] > valores[index_maior]:
#             index_seg_maior = index_maior
#             index_maior = i
#         elif valores[i] > valores[index_seg_maior]:
#             index_seg_maior = i
#     print(index_seg_maior + 1)








# while True:
#     n = int(input())
#     if n == 0:
#         break

#     valores = list(map(int, input().split()))

#     indice_maior = max(range(n), key=valores.__getitem__)
#     valores[indice_maior] = -1
#     indice_maior = max(range(n), key=valores.__getitem__)

#     print(indice_maior + 1)