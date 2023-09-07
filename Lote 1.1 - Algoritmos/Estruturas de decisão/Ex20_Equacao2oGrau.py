#20.Receba 3 coeficientes A, B, e C de uma equação do 2º grau da fórmula Ax²+Bx+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.
import math
A = int(input("Digite o valor de a: "))
B = int(input("Digite o valor de b: "))
C = int(input("Digite o valor de c: "))
Delta = (pow(B,2)-1*(4*A*C))
if(Delta >= 0):
  X1=(((-1*B)+math.sqrt(Delta))/(2*A))
  X2=(((-1*B)-math.sqrt(Delta))/(2*A))
  print("As raízes são: ",X1,X2)
else:
  print("Não existe raiz real")