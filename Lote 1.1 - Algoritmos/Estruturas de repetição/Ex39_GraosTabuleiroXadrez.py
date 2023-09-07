"""
39.	Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
Casa: 	1	2	3	4	...	64
Qdte:	1	2	4	8	...	N
"""
Contador = 0
Soma = 0
while Contador < 64:
  Graos = (2**Contador)
  Soma = (Soma+Graos)
  Contador = Contador+1
print("Soma =",Soma)