import random

array = random.sample(range(15),15)

print (array)

def swap (i,j,array):
    array[i], array[i-1] = array[i-1], array[i]
    return array


def bubbleSort(array):
    while True:
        change = False
        for i in range (1,len(array)):
            if array[i] < array[i-1]:
                swap(i,i-1,array)
                change = True
        if change == False:
            break 
    return array

print (bubbleSort(array))