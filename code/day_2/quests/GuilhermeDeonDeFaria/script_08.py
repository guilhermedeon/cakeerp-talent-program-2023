'''
8 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
B. A mensagem "Reprovado", se a média for menor do que sete;
C. A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''

#dict nao seria a melhor estrutura de dados, mas quis testar
notas_dict = {
    0 : 0,
    1 : float(0)
    }

i = 0
while i < 2:
    try:
        nota = float(input("\nDigite a nota " + str(i+1) + "\n"))
        notas_dict.update({i:nota})
        i = i + 1

    except:
        print("Ocorreu um erro...")

media = (notas_dict.get(0) + notas_dict.get(1)) / 2

print("\nMedia final = " + str(media))

if media == 10:
    print("Aprovado com distincao")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
