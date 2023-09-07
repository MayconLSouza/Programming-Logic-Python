#25.Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.
HoraInicial = int(input("Digite a hora de início do jogo: "))
MinutoInicial = int(input("Digite o minuto de início do jogo: "))
HoraFinal = int(input("Digite a hora do final do jogo: "))
MinutoFinal = int(input("Digite o minuto do final do jogo: "))
if(MinutoInicial <= MinutoFinal):
  if(HoraInicial <= HoraFinal):
    MinutoJogo = (MinutoFinal-MinutoInicial)
    HoraJogo = (HoraFinal-HoraInicial)
  else:
    MinutoJogo = (MinutoFinal-MinutoInicial)
    HoraJogo = ((HoraFinal+24)-HoraInicial)
else:
    if(HoraInicial < HoraFinal):
      MinutoJogo = ((MinutoFinal+60)-MinutoInicial)
      HoraJogo = ((HoraFinal-1)-HoraInicial)
    else:
      MinutoJogo = ((MinutoFinal+60)-MinutoInicial)
      HoraJogo = ((HoraFinal+23)-HoraInicial)
print("A duração do jogo foi: ",HoraJogo,"h ",MinutoJogo,"min")