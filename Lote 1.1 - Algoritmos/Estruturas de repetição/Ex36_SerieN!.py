#36.Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!
Numero = int(input("Digite um número: "))
Fatorial = 1
Contador = 1
Serie = 0
while Contador <= Numero:
  Fatorial = (Fatorial*Contador)
  Serie = (Serie+(1/Fatorial))
  Contador += 1
print("Serie =",Serie)