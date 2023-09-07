"""
9. Criar e carregar uma matriz [4][4] com valores aleatórios, sendo que a diagonal principal terá seus dados carregados no programa segundo:
| 1 |   |    |    |
|   | 4 |    |    |
|   |   | 16 |    |
|   |   |    | 64 |
"""
import random

# Criar matriz 4x4
matriz = [[0 for _ in range(4)] for _ in range(4)]

for linha in range(0,4):
  for coluna in range(0,4):
    if(linha == coluna):
      if((linha % 2) == 0):
        matriz[linha][coluna] = (4**(linha))
      else:
        matriz[linha][coluna] = (4**(linha))
      print(matriz[linha][coluna], end=" ")
    else:
      matriz[linha][coluna] = random.randint(1, 100)
      print(matriz[linha][coluna], end=" ")
  print()  # Pular para a próxima linha