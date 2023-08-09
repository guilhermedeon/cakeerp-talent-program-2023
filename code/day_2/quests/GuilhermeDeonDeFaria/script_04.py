'''
4 - Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

def somar(n1,n2,n3):
    return round(n1+n2+n3,2)

minha_lista = list()
i = 0

while i < 3:
    try:
        value = float(input("Digite o número - posicao: " + str(i+1) + "\n"))
        minha_lista.append(value)
        i = i + 1
    except:
        print("Valor invalido")


soma = somar(
    minha_lista[0],
    minha_lista[1],
    minha_lista[2]
    )

print("Soma final = " + str(soma))

