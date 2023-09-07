#15.Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.
import math
Cateto1 = float(input("Digite o valor do 1° cateto: "))
Cateto2 = float(input("Digite o valor do 2° cateto: "))
Hipotenusa = (math.sqrt(pow(Cateto1,2)+pow(Cateto2,2)))
print("O valorda hipotenusa é: ",Hipotenusa)