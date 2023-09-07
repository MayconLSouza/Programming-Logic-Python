# 44. Receba o número da base e do expoente. Calcule e mostre o valor da potência. Modularizar através de função.
def  FuncaoPotencia(Base,Expoente):
        Potencia = (Base**Expoente)
        return Potencia

Base = int(input("Digite a base: "))
Expoente = int(input("Digite o expoente: "))
print(Base,"^",Expoente,"=",FuncaoPotencia(Base,Expoente))