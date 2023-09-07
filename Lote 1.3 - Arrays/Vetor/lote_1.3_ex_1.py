"""
1. Criar e coletar um vetor [50] inteiro. Calcular e exibir:
a. A média dos valores entre 10 e 200;
b. A soma dos números ímpares
Vetor dinâmico
"""
vetor = []
Media = 0
Divisor = 0
Soma_Impar = 0
for Contador in range(0,50):
  Numero = Contador
  vetor.append(Numero)
  if ((vetor[Contador] % 2) != 0):
    Soma_Impar = (Soma_Impar+vetor[Contador])
  if((vetor[Contador] >= 10) and (vetor[Contador] <= 200)):
    Media = (Media+vetor[Contador])
    Divisor = Divisor+1
Media = (Media/Divisor)
print("A média da série é: ", Media)
print("A somatória dos números ímpares da série é: ", Soma_Impar)