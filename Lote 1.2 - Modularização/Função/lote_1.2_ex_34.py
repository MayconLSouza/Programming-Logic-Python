# 34. Receba um número. Calcule e mostre os resultados da tabuada desse número. Modularizar através de função.
def  FuncaoTabuada(Contador,Numero):
      Tabuada = (Numero*Contador)
      return Tabuada

Numero = int(input("Digite um número: "))
Contador = 1
while Contador <= 10:
  print(Numero,"*",Contador,"=",FuncaoTabuada(Contador,Numero))
  Contador = (Contador+1)