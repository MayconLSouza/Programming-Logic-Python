"""
10. Criar uma matriz [8][8] onde o programa irá carregar segundo:
casa  |  1  |  2  |  3  |  4  |  ...   
valor |  1  |  2  |  4  |  8  |  ...  
Exibir a soma dos valores.
"""

# Criar matriz 8x8
matriz = [[0 for _ in range(8)] for _ in range(8)]

# Declaração de variáveis
soma_valores = 0
casa = 1

# Preencher a matriz com os valores conforme especificado
for linha in range(0,8):
  for coluna in range(0,8):
    matriz[linha][coluna] = (2**(casa-1))
    soma_valores += (2**(casa-1))
    casa += 1

# Exibir a soma dos valores
print("A soma dos valores é", soma_valores)