#35.Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
Numero1 = int(input("Digite o 1°número: "))
Numero2 = int(input("Digite o 2° número: "))
if(Numero1 == Numero2):
  print("Soma = 0")
else:
  if(Numero1 < Numero2):
    if((Numero1 % 2) == 0):
      Contador = Numero1+1
      Soma = 0
      while Contador < Numero2:
        Soma = (Soma+Contador)
        Contador = Contador+2
      print("Soma = ",Soma)
    else:
      Contador = Numero1+2
      Soma = 0
      while Contador < Numero2:
        Soma = (Soma+Contador)
        Contador = Contador+2
      print("Soma = ",Soma)
  else:
    if((Numero2 % 2) == 0):
      Contador = Numero2+1
      Soma = 0
      while Contador < Numero1:
        Soma = (Soma+i)
        Contador = Contador+2
      print("Soma = ",Soma)
    else:
      Contador = Numero2+2
      Soma = 0
      while Contador < Numero1:
        Soma = (Soma+Contador)
        Contador = Contador+2
      print("Soma = ",Soma)