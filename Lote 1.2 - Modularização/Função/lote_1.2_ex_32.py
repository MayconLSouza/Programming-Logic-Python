# 32. Receba um número inteiro. Calcule e mostre o seu fatorial. Modularizar através de função.
def  FuncaoFatorial(Numero):
      Fatorial = 1
      Contador = 1
      while Contador <= Numero:
        Fatorial = (Fatorial*Contador)
        Contador = (Contador+1)
      return Fatorial

Numero = int(input("Digite um número: "))
print("Fatorial de",Numero,"=",FuncaoFatorial(Numero))