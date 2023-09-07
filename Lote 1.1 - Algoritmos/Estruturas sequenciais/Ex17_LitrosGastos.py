#17.Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média.
VelocidadeMedia = float(input("Digite a velocidade média do veículo em km/h: "))
Tempo = float(input("Digite o tempo de percurso em horas: "))
Distancia = (VelocidadeMedia*Tempo)
LitrosGastos = (Distancia/12)
print("A quantidade de litros gastos foi: ",LitrosGastos)