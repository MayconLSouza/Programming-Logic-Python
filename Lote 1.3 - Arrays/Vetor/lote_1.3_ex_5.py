"""
5. Criar e coletar em um vetor [20] inteiro. Calcule e exiba, segundo: 
10 
 ∑ (A[1] – A[21–1]) 
i=1
vetor estático
"""
import random
Vetor = [0]*20
Soma = 0
for Contador in range(0,20):
  Vetor[Contador] = random.randint(0, 100)  # Intervalo entre 0 e 100, somente números inteiros
for Contador in range(0,10):
  Soma = Soma+(Vetor[Contador]-Vetor[19-Contador])
print("A somatória da série é: ", Soma)