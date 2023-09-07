#33.Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.
Numero = int(input("Digite um número: "))
Serie = 0
for Contador in range(1,Numero+1):
  Serie = (Serie+(1/Contador))
print("Serie =",Serie)