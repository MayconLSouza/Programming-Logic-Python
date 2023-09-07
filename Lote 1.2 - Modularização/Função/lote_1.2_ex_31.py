# 31. Calcule e mostre o quadrado dos números entre 10 e 150. Modularizar através de função.
def  FuncaoQuadrado(Contador):
      Quadrado = (Contador*Contador)
      return Quadrado

Contador = 10
while Contador <= 150:
  print(Contador,"*",Contador,"=",FuncaoQuadrado(Contador))
  Contador = (Contador+1)