#16.Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes. Calcule o salário que serão as horas trabalhadas x o valor por hora. Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exiba o salário a receber. Modularizar através de procedimento.
def SalarioFinal():
    SalarioBruto = (HoraTrabalhada*ValorHora)
    Desconto = (SalarioBruto*(PercentualDesconto/100))
    SalarioLiquido = (SalarioBruto-Desconto)
    SalarioFinal = (SalarioLiquido+(100*NumeroDependente))
    print("O salário a receber é: ",SalarioFinal," reais.")

HoraTrabalhada = float(input("Digite a quantidade de horas trabalhadas: "))
ValorHora = float(input("Digite o valor por hora: "))
PercentualDesconto = float(input("Digite o percentual de desconto: ",))
NumeroDependente = float(input("Digite o número de dependentes: "))
SalarioFinal()