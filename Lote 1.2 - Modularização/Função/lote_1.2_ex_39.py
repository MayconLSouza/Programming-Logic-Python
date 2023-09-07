"""
39. Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde: 
Casa: 1 2 3 4 ... 64 
Qdte: 1 2 4 8 ... N
Modularizar através de função.
"""
def  FuncaoGraos(Contador):
      Soma = 0
      while Contador < 64:
        Soma = (Soma+(2**Contador))
        Contador = Contador+1
      return Soma

Contador = 0
print(FuncaoGraos(Contador))