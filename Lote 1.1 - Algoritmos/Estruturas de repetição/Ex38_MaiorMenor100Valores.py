"""
38.Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.
Numero = int(input("Digite um número: "))
if (Numero < 0):
  print("Número inválido")
else:
  Maior = Numero
  Menor = Numero
  Contador = 1
  while Contador < 100:
    Numero = int(input("Digite um número: "))
    if (Numero < 0):
      print("Número inválido")
    else:
      if(Numero > Maior):
        Maior = Numero
      else:
        if(Numero < Menor):
          Menor = Numero
    Contador = Contador+1
  print("O menor número é ",Menor,"e o maior número é ",Maior)
"""