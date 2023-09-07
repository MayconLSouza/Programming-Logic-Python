#17.Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l. Receber o tempo de percurso e a velocidade média. Modularizar através de procedimento.
def LitrosGastos():
    LitrosGastos = ((VelocidadeMedia*Tempo)/12)
    print("A quantidade de litros gastos na viagem foi: ",LitrosGastos," l")

VelocidadeMedia = float(input("Digite a velocidade média do veículo em km/h: "))
Tempo = float(input("Digite o tempo de percurso em horas: "))
LitrosGastos()