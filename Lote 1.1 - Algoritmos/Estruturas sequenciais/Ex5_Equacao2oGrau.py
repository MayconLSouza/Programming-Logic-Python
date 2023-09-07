#5.Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue2 raízes).
import math
A = int(input("Digite o valor de a: "))
B = int(input("Digite o valor de b: "))
C = int(input("Digite o valor de c: "))
Delta = (pow(B,2)-1*(4*A*C))
X1 = (((-1*B)+math.sqrt(Delta))/(2*A))
X2 = (((-1*B)-math.sqrt(Delta))/(2*A))
print("As raízes da equação são:",X1," e ",X2)