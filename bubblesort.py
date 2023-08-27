### Bubble sorting ###

def bubblesort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0, (length-i-1)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  ##swaping method for elements

arr = [2,9,5,3,7,4]
bubblesort(arr)
print(arr)

### time complexity = O(n^2)
