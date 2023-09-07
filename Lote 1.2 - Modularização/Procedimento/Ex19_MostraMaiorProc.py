#19.Receba 2 valores reais. Calcule e mostre o maior deles. Modularizar através de procedimento.
def  Maior():
      if(Numero1 == Numero2):
        print("Números iguais")
      elif(Numero1 < Numero2):
        print("O maior número é ",Numero2)
      else:
        print("O maior número é ",Numero1)

Numero1 = int(input("Digite o 1°número: "))
Numero2 = int(input("Digite o 2°número: "))
Maior()