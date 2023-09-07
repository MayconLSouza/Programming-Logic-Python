#18.Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menos valor. Modularizar através de procedimento.
def  Diferenca():
      if(Numero1 > Numero2):
        Diferenca = (Numero1-Numero2)
      else:
        Diferenca = (Numero2-Numero1)
      print("A diferença do maior número para o menor é: ",Diferenca)

Numero1 = int(input("Digite o 1°número: "))
Numero2 = int(input("Digite o 2°número: "))
Diferenca()