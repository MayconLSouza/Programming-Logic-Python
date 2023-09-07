#37.Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.
Numero = int(input("Digite um número: "))
if(Numero < 1):
  print("Número inválido")
else:
  if(Numero == 1):
    print("1 ° termo = 1")
  else:
    print("1 ° termo = 1")
    Fibonacci_Anterior = 0
    Fibonacci_Atual = 1
    Contador = 2
    while Contador <= Numero:
      Fibonacci = (Fibonacci_Anterior+Fibonacci_Atual)
      Fibonacci_Anterior = Fibonacci_Atual
      Fibonacci_Atual = Fibonacci
      Contador += 1
      print((Contador-1),"° termo =",Fibonacci)