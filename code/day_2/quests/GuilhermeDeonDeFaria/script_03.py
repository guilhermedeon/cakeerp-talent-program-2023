'''
3 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A. "Telefonou para a vítima?"
B. "Esteve no local do crime?"
C. "Mora perto da vítima?"
D. "Devia para a vítima?"
E. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''

respostas = list()
perguntas = (
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?")

i = 0
while i < 5:
    try:
        print("\nResponda SIM ou NAO - Questao: " + str(i+1))
        resposta = input(perguntas[i]+"\n")
        resposta = resposta.lower()
        if resposta  == "nao" or resposta == "sim":
            i = i + 1
            respostas.append(resposta)
        else:
            raise Exception()
    except:
        print("Resposta invalida")


print("\nRespostas:")
contagemSim = 0
for i in range(0,len(respostas)):
    print(perguntas[i])
    print(respostas[i])
    if respostas[i] == "sim":
        contagemSim = contagemSim + 1

print("\nVeredito:")
if contagemSim < 2:
    print("Inocente!")
if contagemSim == 2:
    print("Suspeito!")
if contagemSim == 3 or contagemSim == 4:
    print("Cumplice!")
if contagemSim == 5:
    print("Assassino!")
