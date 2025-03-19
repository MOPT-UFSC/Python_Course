codigo, quantidade = map(int, input().split())

if codigo == 1:
    valor_produto = 4
elif codigo == 2:
    valor_produto = 4.5
elif codigo == 3:
    valor_produto = 5
elif codigo == 4:
    valor_produto = 2
else:
    valor_produto = 1.5

total = quantidade * valor_produto
print(f"Total: R$ {total:.2f}")