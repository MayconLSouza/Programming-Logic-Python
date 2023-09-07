#19.Receba 2 valores reais. Calcule e mostre o maior deles.
Numero1 = int(input("Digite o valor do 1° número: "))
Numero2 = int(input("Digite o valor do 2° número: "))
if(Numero1 == Numero2):
  print("Números iguais")
elif(Numero1 < Numero2):
    print("O maior número é: ",Numero2)
else:
    print("O maior número é: ",Numero1)