
def quick_sort(arr):  # sourcery skip: remove-unnecessary-else
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
    # middle = [x for x in arr if x == pivot]
        right = [x for x in arr[1:] if x > pivot]
    
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example array to be sorted
arr = [12, 4, 5, 6, 7, 3, 1, 15]

# Call the quick_sort function to sort the array
sorted_array = quick_sort(arr)
print("Sorted array:", sorted_array)



### another method ###

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for num in arr[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quicksort(left) + [pivot] + quicksort(right)


# Example usage
input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = quicksort(input_array)
print(sorted_array)
