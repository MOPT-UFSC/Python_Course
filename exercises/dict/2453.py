n = input()
nova = str()

i = 1
while i < len(n):
    nova += (n[i])
    if i < len(n) - 1 and n[i+1] == ' ':
        nova += (' ')
        i += 1
    i += 2
print(nova)
