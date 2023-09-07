#12.Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.
Nascimento = int(input("Digite o ano de nascimento: "))
Atual = int(input("Digite o ano atual: "))
Idade = (Atual-Nascimento)
Idade17 = (Idade+17)
print("A idade é: ",Idade," anos")
print("A idade daqui 17 anos será: ",Idade17," anos")