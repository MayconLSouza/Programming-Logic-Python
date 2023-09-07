#23.Receba 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
print("Os valores do 1°,2° e 3° números tem que estar em ordem crescente.")
Numero1 = int(input("Digite o valor do 1° número: "))
Numero2 = int(input("Digite o valor do 2° número: "))
Numero3 = int(input("Digite o valor do 3° número: "))
Numero4 = int(input("Digite o valor do 4° número: "))
if(Numero4 < Numero1):
  print("Os valores em ordem crescente são: ",Numero4,",", Numero1,",", Numero2,",", Numero3)
elif(Numero4 > Numero3):
  print("Os valores em ordem crescente são: ",Numero1,",", Numero2,",", Numero3,",", Numero4)
elif(Numero4 > Numero2):
  print("Os valores em ordem crescente são: ",Numero1,",", Numero2,",", Numero4,",", Numero3)
else:
  print("Os valores em ordem crescente são: ",Numero1,",", Numero4,",", Numero2,",", Numero3)