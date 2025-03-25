import math
q = int(input())

for j in range(q):
    n = int(input())
    
    if n < 2:
        print("Not Prime")
    elif n == 2:
        print("Prime")
    else:
        ehPrimo = True
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                ehPrimo = False
                break
        if ehPrimo:
            print("Prime")
        else:
            print("Not Prime")