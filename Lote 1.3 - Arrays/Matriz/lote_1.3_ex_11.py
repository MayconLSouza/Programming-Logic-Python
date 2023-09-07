"""
11. Criar uma matriz [8][8] inteiro e o programa irá carregar segundo:
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 |
| 1 | 2 | 3 | 3 | 3 | 3 | 2 | 1 |
| 1 | 2 | 3 | 4 | 4 | 3 | 2 | 1 |
| 1 | 2 | 3 | 4 | 4 | 3 | 2 | 1 |
| 1 | 2 | 3 | 3 | 3 | 3 | 2 | 1 |
| 1 | 2 | 2 | 2 | 2 | 2 | 2 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
"""
# Criar matriz 8x8
matriz = [[0 for _ in range(8)] for _ in range(8)]

# Preencher matriz
for linha in range(0,8):
  for coluna in range(0,8):
    if(linha == 0 or coluna == 0 or linha == 7 or coluna == 7):
      matriz[linha][coluna] = 1
    elif(linha == 1 or coluna == 1 or linha == 6 or coluna == 6):
      matriz[linha][coluna] = 2
    elif(linha == 2 or coluna == 2 or linha == 5 or coluna == 5):
      matriz[linha][coluna] = 3
    else:
      matriz[linha][coluna] = 4

# Exibir a matriz
for linha in range(8):
    for coluna in range(8):
        print("{:<2}".format(matriz[linha][coluna]), end=" ")
    print()