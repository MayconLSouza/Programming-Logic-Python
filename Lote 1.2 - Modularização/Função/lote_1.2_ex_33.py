# 33. Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N. Modularizar através de função.
def  FuncaoSerie(Numero):
      Contador = 1
      Serie = 0
      while Contador <= Numero:
        Serie = (Serie+(1/Contador))
        Contador = (Contador+1)
      return Serie

Numero = int(input("Digite um número: "))
print("Serie =",FuncaoSerie(Numero))