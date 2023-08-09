'''
5 - Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
'''

#takes percentage as number without "%", or example 50% = 50
def somaImposto(taxaImposto, custo):
    return custo + (custo * (taxaImposto/100))

valor = 10
print(valor)

#taxaimposto = 5%, valor = 10
valor = somaImposto(5,valor)
print(valor)
