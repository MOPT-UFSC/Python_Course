nome_funcionario = input()
salario_fixo = float(input())
total_vendas = float(input())

salario_total = salario_fixo + 0.15 * total_vendas
print(f"TOTAL = R$ {salario_total:.2f}")