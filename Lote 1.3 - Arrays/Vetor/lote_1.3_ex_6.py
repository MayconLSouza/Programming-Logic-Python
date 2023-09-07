"""
6. Criar e coletar em um vetor [20] com números aleatórios. Classificar este vetor em ordem crescente e mostre os dados.
vetor estático
"""
import random

vetor = [0] * 20

for contador in range(0, 20):
    vetor[contador] = random.randint(0, 100)  # Intervalo entre 0 e 100, somente números inteiros

tamanho_vetor = 20
swapped = 1

while swapped != 0:
    swapped = 0
    for contador in range(0, (tamanho_vetor - 1)):
        if vetor[contador] > vetor[contador + 1]:
            temp = vetor[contador + 1]
            vetor[contador + 1] = vetor[contador]
            vetor[contador] = temp
            swapped = 1
    tamanho_vetor = tamanho_vetor - 1

for contador in range(0, 20):
    print("O valor da posição", contador, "é", vetor[contador])