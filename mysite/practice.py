import random
from typing import Counter

array = random.sample(range(15),15)

print (array)

def swap (i,j,array):
    array[i], array[i-1] = array[i-1], array[i]
    return array

def selectionSort(array):
    smallestIdx = 0
    while smallestIdx < len(array) :
        currentIdx = smallestIdx
        for i in range(currentIdx, len(array)-1):
            if array[i] < array[currentIdx]:
                currentIdx = i
        swap(currentIdx, smallestIdx, array)
        smallestIdx += 1
    return array


print(selectionSort(array))