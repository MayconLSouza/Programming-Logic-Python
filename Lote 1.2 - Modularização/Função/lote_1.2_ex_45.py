# 45. Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 + ... + 15/225. Modularizar através de função.
def  FuncaoSerie(Dividendo):
      Serie = 0
      while Dividendo <= 15:
        if((Dividendo % 2) == 0):
          Serie = (Serie+((-1*Dividendo)/(Dividendo**2)))
        else:
          Serie = (Serie+(Dividendo/(Dividendo**2)))
        Dividendo = Dividendo+1
      return Serie
    
Dividendo = 1
print("Serie =",FuncaoSerie(Dividendo))