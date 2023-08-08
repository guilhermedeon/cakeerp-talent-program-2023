'''
10 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que
calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
atual:
A. salários até R$ 280,00 (incluindo) : aumento de 20%
B. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
C. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
D. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
E. o salário antes do reajuste;
F. o percentual de aumento aplicado;
G. o valor do aumento;
H. o novo salário, após o aumento.
'''

def calcular_percentual_reajuste(salario):
    reajuste = 0
    if salario <= 280:
        reajuste = 20
    elif salario <= 700:
        reajuste = 15
    elif salario <= 1500:
        reajuste = 10
    else:
        reajuste = 5
    return reajuste/100

def calcular_salario_mais_reajuste(salario,reajuste):
    return salario + (salario * reajuste)


i = 0
salarioInicial = 0

while i < 1:
    try:
        salarioInicial = round(float(input("\nSalario atual do colaborador: \n")),2)
        i = i + 1
    except:
        print("Valor invalido")

percentualReajuste = calcular_percentual_reajuste(salarioInicial)
salarioReajustado = round(
    calcular_salario_mais_reajuste(
        salarioInicial,
        percentualReajuste
        ),
    2)
valorAumento = round(salarioReajustado - salarioInicial,2)

print("\nSalario inicial = " + str(salarioInicial))
print("Percentual de aumento aplicado = " + str(percentualReajuste*100) + "%")
print("Valor do aumento = " + str(valorAumento))
print("Novo salario = " + str(salarioReajustado) + "\n")


