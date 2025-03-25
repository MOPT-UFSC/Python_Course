x, y = map(float, input().split())

if x > 0:
    if y > 0:
        print("Q1")
    elif y < 0:
        print("Q4")
    else:
        print("Eixo X")
elif x < 0:
    if y > 0:
        print("Q2")
    elif y < 0:
        print("Q3")
    else:
        print("Eixo X")
else:
    if y != 0:
        print("Eixo Y")
    else:
        print("Origem")










# x, y = input().split()
# x, y = float(x), float(y)

# if x > 0 and y > 0:
#     print("Q1")
# elif x < 0 and y > 0:
#     print("Q2")
# elif x < 0 and y < 0:
#     print("Q3")
# elif x > 0 and y < 0:
#     print("Q4")
# elif x == 0 and y != 0:
#     print("Eixo Y")
# elif x != 0 and y == 0:
#     print("Eixo X")
# else:
#     print("Origem")