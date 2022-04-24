import random

def bubbleSort_1(a):
    for x in range (0, len(a)):
        for y in range (0, len(a)):
            if a[x] < a[y]:
                number = a[x]
                a[x] = a[y]
                a[y] = number
                
def bubbleSort_2(a):
    for x in range (0, len(a)):
        for y in range (0, len(a)):
            if a[x] > a[y]:
                number = a[x]
                a[x] = a[y]
                a[y] = number                
            

a = random.sample(range(-100, 100), 10)
print("Arranjo não ordenado: ", a)

bubbleSort_1(a)
print("Arranjo ordenado: ", a)

bubbleSort_2(a)
print("Arranjo reordenado: ", a)

