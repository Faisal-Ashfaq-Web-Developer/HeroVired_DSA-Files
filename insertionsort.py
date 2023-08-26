## insertion sorting ##

def insertionSort(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i-1
        while j>=0 and k<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k

arr = [23,5,34,6,8,12,32,3]

insertionSort(arr)
print("Sorted Array: ", arr)

### time complexity = O(n^2)