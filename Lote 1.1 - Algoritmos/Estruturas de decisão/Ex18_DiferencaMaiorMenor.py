#18.Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menos valor.
Numero1 = int(input("Digite o valor do 1° número: "))
Numero2 = int(input("Digite o valor do 2° número: "))
if(Numero1>Numero2):
  Diferenca = (Numero1-Numero2)
else:
  Diferenca = (Numero2-Numero1)
print("A diferença do maior número para o menor é: ",Diferenca)