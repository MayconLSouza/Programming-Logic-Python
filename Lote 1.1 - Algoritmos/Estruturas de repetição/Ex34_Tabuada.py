#34.Receba um número. Calcule e mostre os resultados da tabuada desse número.
Numero = int(input("Digite um número: "))
Contador = 1
while Contador <= 10:
  Tabuada = (Numero*Contador)
  print(Numero,"*",Contador,"=",Tabuada)
  Contador+=1