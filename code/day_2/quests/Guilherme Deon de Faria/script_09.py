'''
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
#sorts array/list using bubble sort algorithm
def bubble_sort(array):
    for i in range(len(array)-1,0,-1):
        for j in range(0,i):
            if array[j] > array[j+1]:
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux
    return array

#reverses array
def reverse(array):
    result = list()
    for i in range(len(array)-1,-1,-1):
        result.append(array[i])
    return result


myarray = list()
i = 0

while i < 3:
    try:
        value = float(input("\nDigite um numero para a posicao: " + str(i+1) + "\n"))
        myarray.append(value)
        i = i + 1
    except:
        print("Ocorreu um erro")


print("\nEm ordem decrescente:")
for item in reverse(bubble_sort(myarray)):
    print(item)
