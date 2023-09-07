#26.Receba 2 números inteiros. Verifique e mostre se o maior número é múltiplo do menor. Modularizar através de procedimento.
def  Multiplo():
      if(Numero1 == Numero2):
        print("números iguais")
      else:
        if(Numero1 > Numero2):
          if((Numero1 % Numero2) == 0):
            print(Numero1," é múltiplo de ",Numero2)
          else:
            print(Numero1," não é múltiplo de ",Numero2)
        else:
          if((Numero2 % Numero1) == 0):
            print(Numero2," é múltiplo de ",Numero1)
          else:
            print(Numero2," não é múltiplo de ",Numero1)

Numero1 = int(input("Digite o 1°número: "))
Numero2 = int(input("Digite o 2°número: "))
Multiplo()