'''
1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

minha_lista = list()

i = 0

while i < 3:
    try:
        value = int(input("\nDigite um número inteiro\n"))
        minha_lista.append(value)
        i = i + 1
        print("Ok")
    except:
        print("Nao e um numero inteiro")

print("\nItens:")
for item in minha_lista:
    print(item)
