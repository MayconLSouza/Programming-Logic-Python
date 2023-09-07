#27.Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.
NumeroVoltas = int(input("Digite o número de voltas: "))
Distancia = float(input("Digite a distância percorrida em metros: "))
Tempo = float(input("Digite o tempo em minutos: "))
VelocidadeMedia = ((3*NumeroVoltas*Distancia)/(50*Tempo))
print("A velocidade média foi: ",VelocidadeMedia,"km/h")