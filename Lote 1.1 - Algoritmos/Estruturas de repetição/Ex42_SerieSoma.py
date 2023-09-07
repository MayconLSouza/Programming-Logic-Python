#42.Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99.
Divisor = -1
Dividendo = 0
Serie = 0
while Dividendo <= 50:
  Dividendo = (Dividendo+1)
  Divisor = (Divisor+2)
  Serie = ((Dividendo/Divisor)+Serie)
print("Serie =",Serie)