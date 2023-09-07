# 38. Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Modularizar através de função. Obs.: somente valores positivos.
def  FuncaoMaiorMenor(Numero_Inicial):
      Maior = Numero_Inicial
      Menor = Numero_Inicial
      Contador = 1
      while Contador < 100:
        Numero_Novo = Contador
        if (Numero_Novo < 0):
          Maior = Maior
          Menor = Menor
        else:
          if(Numero_Novo > Maior):
            Maior = Numero_Novo
          else:
            if(Numero_Novo < Menor):
              Menor = Numero_Novo
        Contador = Contador+1
      return Maior, Menor
      

Numero_Inicial = int(input("Digite um número: "))
if (Numero_Inicial < 0):
  print("Número inválido")
else:
  print(FuncaoMaiorMenor(Numero_Inicial))