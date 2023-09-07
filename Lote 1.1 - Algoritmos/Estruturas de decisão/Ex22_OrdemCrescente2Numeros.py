#22.Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.
Numero1 = int(input("Digite o valor do 1° número: "))
Numero2 = int(input("Digite o valor do 2° número: "))
if(Numero1 < Numero2):
  print("Os valores em ordem crescente são: ",Numero1,",",Numero2)
else:
  print("Os valores em ordem crescente são: ",Numero2,",",Numero1)