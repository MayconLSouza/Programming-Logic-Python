#32.Receba um número inteiro. Calcule e mostre o seu fatorial.
Numero = int(input("Digite um número: "))
Fatorial = 1
Contador = 1
while Contador <= Numero:
  Fatorial = (Fatorial*Contador)
  Contador = Contador+1
print("Fatorial de",Numero,"=",Fatorial)