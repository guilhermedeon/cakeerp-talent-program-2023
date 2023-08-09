'''
7 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

option = str(input("Digite o sexo: F=Feminino, M = Masculino: \n"))
option = option.lower()

if option == 'f':
    print("\nFeminino")
elif option == 'm':
    print("\nMasculino")
else:
    print("Sexo invalido")
