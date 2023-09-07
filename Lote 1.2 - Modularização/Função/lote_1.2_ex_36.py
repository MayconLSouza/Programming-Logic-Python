# 36. Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N! Modularizar através de função.
def  FuncaoSerie(Numero):
      Fatorial = 1
      Contador = 1
      Serie = 0
      while Contador <= Numero:
        Fatorial=(Fatorial*Contador)
        Serie = (Serie+(1/Fatorial))
        Contador = Contador+1
      return Serie

Numero = int(input("Digite um número: "))
print(FuncaoSerie(Numero))