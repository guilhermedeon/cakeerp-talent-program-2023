'''
6 - Faça um Programa que peça dois números e imprima o maior deles.
'''

try:
    value_1 = float(input("Primeiro valor:\n"))
    value_2 = float(input("Segundo valor:\n"))

    print("\n")
    if value_1 > value_2:
        print(value_1)
    if value_2 >= value_1:
        print(value_2)

except:
    print("Valor invalido")


