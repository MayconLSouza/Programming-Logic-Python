"""
3. Criar e coletar valores inteiros nos vetores VT1[3] e VT2[3]. Concatenar esses valores em um 3º vetor (VT3[6]) e mostrar os seus dados. 
P. ex: VT1| 1| 2| 3|     |VT2| 4| 5| 6|     |VT3| 1| 2| 3| 4| 5| 6
vetor estático
"""
Vetor1 = [0]*3
Vetor2 = [0]*3
Vetor3 = [0]*6
for Contador in range (0,3):
  Vetor1[Contador] = int(input("Digite um número(vetor 1): "))
  Vetor2[Contador] = int(input("Digite um número(vetor 2): "))
  Vetor3[Contador] = Vetor1[Contador]
  Vetor3[Contador+3] = Vetor2[Contador]
for Contador in range (0, 6):
  print(Vetor3[Contador])