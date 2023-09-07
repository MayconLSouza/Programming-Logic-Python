# 35. Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores. Modularizar através de função.
def FuncaoSoma(NumeroA,NumeroB):
      if(NumeroA == NumeroB):
        Soma = 0
        return Soma
      else:
        if(NumeroA < NumeroB):
          if((NumeroA % 2) == 0):
            Contador = NumeroA+1
            Soma = 0
            while Contador < NumeroB:
              Soma = (Soma+Contador)
              Contador = Contador+2
            return Soma
          else:
            Contador = NumeroA+2
            Soma = 0
            while Contador < NumeroB:
              Soma = (Soma+Contador)
              Contador = Contador+2
            return Soma
        else:
          if((NumeroB % 2) == 0):
            Contador = NumeroB+1
            Soma = 0
            while Contador < NumeroA:
              Soma = (Soma+Contador)
              Contador = Contador+2
            return Soma
          else:
            Contador = NumeroB+2
            Soma = 0
            while Contador < NumeroA:
              Soma = (Soma+Contador)
              Contador = Contador+2
            return Soma


NumeroA = int(input("Digite o 1°número: "))
NumeroB = int(input("Digite o 2°número: "))
print("Soma = ",FuncaoSoma(NumeroA,NumeroB))