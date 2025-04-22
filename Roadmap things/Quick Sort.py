import random
arrayLength = 10

arr = []

for i in range(0, arrayLength):
    arr.append(random.randint(1,100))

def quicksort(array):

    i = 0
    length = len(array)

    if length < 2:
        return array
    
    pivot = array[length // 2]

    left, middle, right = [], [], []

    for i in range(0, length):
        if array[i] < pivot:
            left.append(array[i])
        elif array[i] == pivot:
            middle.append(array[i])
        elif array[i] > pivot:
            right.append(array[i])
    
    array = quicksort(left)
    array.append(middle)
    array.append(quicksort(right))
    print(array)
    return array

print(arr)
arr = quicksort(arr)
print(arr)