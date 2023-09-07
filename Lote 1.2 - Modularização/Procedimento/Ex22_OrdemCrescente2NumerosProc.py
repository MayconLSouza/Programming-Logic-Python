#22.Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente. Modularizar através de procedimento.
def  Crescente():
      if(Numero1 < Numero2):
        print("Os valores em ordem crescente são ",Numero1,",",Numero2)
      else:
        print("Os valores em ordem crescente são ",Numero2,",",Numero1)

Numero1 = int(input("Digite o 1°número: "))
Numero2 = int(input("Digite o 2°número: "))
Crescente()