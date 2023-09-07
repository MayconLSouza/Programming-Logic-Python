"""
4. Criar e coletar em um vetor [30] real e calcular e exibir:
a. A média do grupo;
b. A quantidade de notas acima do grupo;
c. As posições dos valores abaixo da média do grupo.
vetor dinâmico
"""
import random
Vetor = []
Media = 0
Notas_Acima = 0
for Contador in range(0,30):
  # Intervalo entre 0 e 10
  Notas = round(random.uniform(0, 11), 2) # Arredonda para duas casas decimais 
  Vetor.append(Notas)
  Media = (Media+Vetor[Contador])
Media = (Media/30) 
Media = round(Media, 2) # Arredonda para duas casas decimais 
print("A média da série é: ", Media)
for Contador in range(0,30):
  if(Vetor[Contador] > Media):
    Notas_Acima = (Notas_Acima+1)
  elif(Vetor[Contador] < Media):
    print("A posição da nota ",Vetor[Contador]," que é menor que a média ",Media," é: ", Contador)
print("A quantidade de notas acima da média é: ", Notas_Acima)