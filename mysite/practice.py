import random
from typing import Counter

array = random.sample(range(15),15)

print (array)

def swap (i,j,array):
    array[i], array[i-1] = array[i-1], array[i]
    return array

def selSort(array):
    sI = 0
    while sI < len(array) - 1:
        cI = sI
        for i in range(sI+1, len(array)):
            if array[cI] > array[i]:
                cI = i
        swap(cI, sI, array)
        sI += 1
        
    return array

print(array)