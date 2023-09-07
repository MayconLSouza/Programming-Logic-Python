"""
2. Criar e coletar um vetor [100] inteiro e exibir:
a. O maior e o menor valor;
b. A média dos valores
vetor dinâmico
"""
vetor = []
for Contador in range (0,100):
  Numero = Contador 
  vetor.append(Numero)
  if (Contador == 0):
    Media = vetor[Contador]
    Maior = vetor[Contador]
    Menor = vetor[Contador]
  else:
    if(vetor[Contador] > Maior):
      Maior = vetor[Contador]
    elif(vetor[Contador] < Menor):
      Menor = vetor[Contador]
    Media = (Media+vetor[Contador])
Media = (Media/100)
print("O maior número da série é: ", Maior)
print("O menor número da série é: ", Menor)
print("A média da série: ", Media)