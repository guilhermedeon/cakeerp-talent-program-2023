'''
4 - Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

minha_lista = list()

i = 0

while i < 3:
    try:
        value = float(input("Digite o número - posicao: " + str(i+1) + "\n"))
        minha_lista.append(value)
        i = i + 1
    except:
        print("Valor invalido")

soma = 0

for item in minha_lista:
    soma = soma + item

soma = round(soma,2)

print("Soma final = " + str(soma))
