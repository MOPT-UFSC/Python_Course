valor = int(input())
print(valor)

notas_cem = valor // 100
valor = valor % 100

notas_cinquenta = valor // 50
valor = valor % 50

notas_vinte = valor // 20
valor = valor % 20

notas_dez = valor // 10
valor = valor % 10

notas_cinco = valor // 5
valor = valor % 5

notas_dois = valor // 2
valor = valor % 2

notas_um = valor

print(f"{notas_cem} nota(s) de R$ 100,00")
print(f"{notas_cinquenta} nota(s) de R$ 50,00")
print(f"{notas_vinte} nota(s) de R$ 20,00")
print(f"{notas_dez} nota(s) de R$ 10,00")
print(f"{notas_cinco} nota(s) de R$ 5,00")
print(f"{notas_dois} nota(s) de R$ 2,00")
print(f"{notas_um} nota(s) de R$ 1,00")