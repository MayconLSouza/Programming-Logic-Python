#20.Receba 3 coeficientes A, B, e C de uma equação do 2º grau da fórmula AX²+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre. Modularizar através de procedimento.
import math
def  Equacao2():
      Delta = ((B**2)-(4*A*C))
      if(Delta > 0):
        X1 = (((-1*B)+math.sqrt(Delta))/(2*A))
        X2 = (((-1*B)-math.sqrt(Delta))/(2*A))
        print("Os valores das raízes são ",X1," e ",X2)
      elif(Delta == 0):
        X = ((-1*B)/(2*A))
        print("O valor da raiz é ",X)
      else:
        print("Não existe raiz real")

A = int(input("Digite o valor do a: "))
B = int(input("Digite o valor do b: "))
C = int(input("Digite o valor do c: "))
Equacao2()