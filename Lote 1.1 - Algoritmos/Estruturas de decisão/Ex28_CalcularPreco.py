"""
28.	Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
Venda Mensal	    Preço Atual	    Preço Novo
    <500	            <30	            +10%
>=500 e <1000	     >=30 e <80	        +15%
  >=1000	            >=80	          -5%
Obs.: para outras condições, preço novo será igual ao preço atual.
"""
VendaMensal = int(input("Digite o número de vendas mensais: "))
PrecoAtual = float(input("Digite o preço atual do produto: "))
if((VendaMensal < 500) and (PrecoAtual < 30)):
  PrecoNovo = (PrecoAtual*1.1)
elif(((VendaMensal >= 500) and (VendaMensal < 1000)) and ((PrecoAtual >= 30) and (PrecoAtual < 80))):
  PrecoNovo = (PrecoAtual*1.15)
elif((VendaMensal >= 1000) and (PrecoAtual >= 80)):
  PrecoNovo = (PrecoAtual*0.95)
else:
  PrecoNovo = PrecoAtual
print("O preço será: ",PrecoNovo," reais.")