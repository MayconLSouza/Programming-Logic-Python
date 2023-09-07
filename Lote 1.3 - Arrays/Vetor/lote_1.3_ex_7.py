"""
7. A partir do exercício 6 (vetor classificado) solicitar um valor qualquer e verificar a sua existência no vetor (utilizar pesquisa binária).
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

numero_procurado = int(input("Digite o número que procura: "))
menor = 0
maior = 19
encontrado = False

while menor <= maior:
    meio = (menor + maior) // 2
    if (vetor[meio] == numero_procurado):
        print("O número foi encontrado na posição", meio)
        encontrado = True
        break
    elif (vetor[meio] < numero_procurado):
        menor = meio + 1
    else:
        maior = meio - 1

if not encontrado:
    print("Valor não existente")