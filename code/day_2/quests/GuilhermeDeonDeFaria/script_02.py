'''
2 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem
lida.
'''

minha_lista = list()

i = 0

while i < 5:
    try:
        print("\nPessoa n: " + str(i+1))
        idade = int(input("Digite a idade\n"))
        altura = int(input("Digite a altura em cm\n"))
        minha_lista.append([idade,altura])
        print("Ok")
        i = i+1
    except:
        print("Erro no input")

print("\n\nPessoas:")
for i in range(len(minha_lista)-1,-1,-1):
    pessoa = minha_lista[i]
    print("\nPessoa n: " + str(i+1))
    print("Idade = " + str(pessoa[0]))
    print("Altura = " + str(pessoa[1]) + "cm")

