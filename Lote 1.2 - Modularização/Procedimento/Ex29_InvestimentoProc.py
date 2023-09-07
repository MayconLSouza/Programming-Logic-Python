#29.Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados. Modularizar através de procedimento.
def  Montante():
      if(TipoInvestimento == 1):
        Montante = (Capital*1.03)
        print("O valor do investimento na poupança corrigido após 30 dias será: ",Montante," reais.")
      else:
        if(TipoInvestimento == 2):
          Montante = (Capital*1.05)
          print("O valor do investimento em renda fixa corrigido após 30 dias será: ",Montante," reais.")
        else:
          print("Investimento inválido")

TipoInvestimento = int(input("Digite o tipo de investimento: "))
Capital = float(input("Digite o valor do investimento: "))
Montante()