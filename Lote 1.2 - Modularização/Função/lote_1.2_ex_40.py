#40.	Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles. Modularizar através de função.
Numero1 = int(input("Digite o 1°número: "))
Numero2 = int(input("Digite o 2°número: "))
if(Numero1 == Numero2):
  print("Números iguais")
elif ((Numero1 < 0) and (Numero2 < 0)):
    print("Números inválido")
else:
  if(Numero1 > Numero2):  
    Maior = Numero1
    Menor = Numero2
  else:
    Maior = Numero2
    Menor = Numero1
  NumeroPrimo = (Menor+1)
  while NumeroPrimo < Maior:
    Divisor = 2
    Contador = 1
    while Contador <= NumeroPrimo:
      if((NumeroPrimo % Contador) == 0):
        Divisor = (Divisor-1)
      Contador = Contador+1
    if(Divisor == 0):
      print("Número Primo =",NumeroPrimo)
    NumeroPrimo = NumeroPrimo+1