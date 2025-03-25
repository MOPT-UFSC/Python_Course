alcool = 0
gasolina = 0
diesel = 0
while True:
    n = int(input())
    
    if n == 1:
        alcool += 1
    elif n == 2:
        gasolina += 1
    elif n == 3:
        diesel += 1
    elif n == 4:
        break
print("MUITO OBRIGADO")
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')