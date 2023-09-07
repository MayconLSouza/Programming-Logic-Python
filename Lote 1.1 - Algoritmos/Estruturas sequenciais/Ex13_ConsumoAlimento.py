#13.Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
Kilo = float(input("Digite o peso do alimento em kg: "))
Grama = (Kilo*1000)
Dia = (Grama/50)
print("O alimento durará ",Dia," dias.")