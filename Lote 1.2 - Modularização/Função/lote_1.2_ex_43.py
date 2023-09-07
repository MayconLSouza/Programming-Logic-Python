"""
43. Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano. Modularizar através de função.
"""
def  FuncaoAno(Altura_Ana,Altura_Maria):
      Ano = 0
      while Altura_Ana < Altura_Maria:
        Altura_Ana = (Altura_Ana+0.03)
        Altura_Maria = (Altura_Maria+0.02)
        Ano = Ano+1
      return Ano

Altura_Ana = 1.1
Altura_Maria = 1.5
print(FuncaoAno(Altura_Ana,Altura_Maria),"anos.")