# 41. Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7. Modularizar através de função.
def  FuncaoDado(Dado1,Dado2):
      Soma = (Dado1+Dado2)
      return Soma

Dado1 = 0
while Dado1 <= 6:
  Dado1 = Dado1+1
  Dado2 = 1
  while Dado2 <= 6:
    Soma = FuncaoDado(Dado1,Dado2)
    if(Soma == 7):
      print(Dado1,"+",Dado2,"= 7")
    Dado2 = Dado2+1