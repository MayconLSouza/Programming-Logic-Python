#24.Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3. Modularizar através de procedimento.
def  Divisivel():
      if((Numero % 2) == 0):
        if((Numero % 3) == 0):
          print("Divisível por 2 e 3")
        else:
          print("Não divisível")
      else:
        print("Não divisível")

Numero = int(input("Digite um número: "))
Divisivel()