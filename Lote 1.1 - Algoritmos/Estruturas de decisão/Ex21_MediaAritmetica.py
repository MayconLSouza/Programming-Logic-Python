"""
21.Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média:
a.Se a média for >= 6,0 exibir “APROVADO”;
b.Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
c.Se a média for < 3,0 exibir “RETIDO”.
"""
Nota1 = float(input("Digite o valor da nota do 1° bimestre: "))
Nota2 = float(input("Digite o valor da nota do 2° bimestre: "))
Nota3 = float(input("Digite o valor da nota do 3° bimestre: "))
Nota4 = float(input("Digite o valor da nota do 4° bimestre: "))
NotaFinal = ((Nota1+Nota2+Nota3+Nota4)/4)
print("A nota final é: ",NotaFinal)
if(NotaFinal > 3):
  if(NotaFinal < 6):
    print("Exame")
  else:
    print("Aprovado")
else:
  print("Retido")