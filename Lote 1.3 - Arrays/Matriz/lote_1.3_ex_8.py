"""
8. Criar e carregar uma matriz [4][3] inteiro com quantidade de produtos vendidos em 4 semanas. Calcular e esemanaibir:
  a. A quantidade de cada produto vendido no mês;
  b. A quantidade de produtos vendidos por semana;
  c. O total de produtos vendidos no mês.
"""
import random

# Criar matriz 4x3 (4 semanas e 3 produtos)
matriz_vendas = [[0 for _ in range(3)] for _ in range(4)]

# Gerar dados aleatórios para a matriz de vendas
for semana in range(4):
    for produto in range(3):
        matriz_vendas[semana][produto] = random.randint(10, 100)

# Calcular e exibir a quantidade de cada produto vendido no mês
for produto in range(1, 4):
    quantidade_por_produto = 0
    for semana in range(1, 5):
        quantidade_por_produto += matriz_vendas[semana - 1][produto - 1]
    print("A quantidade do produto", produto, "vendido no mês foi", quantidade_por_produto)

# Calcular e exibir a quantidade de produtos vendidos por semana
for semana in range(1, 5):
    quantidade_por_semana = 0
    for produto in range(1, 4):
        quantidade_por_semana += matriz_vendas[semana - 1][produto - 1]
    print("A quantidade de produtos vendidos na semana", semana, "foi", quantidade_por_semana)

# Calcular e exibir o total de produtos vendidos no mês
total_vendido_mes = sum(sum(semana) for semana in matriz_vendas)
print("O total de produtos vendidos no mês foi", total_vendido_mes)