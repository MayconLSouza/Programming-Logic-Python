#43.Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.
AlturaAna = 1.1
AlturaMaria = 1.5
Ano = 0
while AlturaAna < AlturaMaria:
  AlturaAna = (AlturaAna+0.03)
  AlturaMaria = (AlturaMaria+0.02)
  Ano = Ano+1
print(Ano,"anos.")