def mergesort(arr):
    if len(arr) <=1:
        return arr
    middle = (len(arr)//2)
    left = arr[:middle]
    right = arr[middle:]

    left = mergesort(left)
    right = mergesort(right)
    return combine(left, right)

def combine(left, right):
    result = []
    l,r = 0,0

    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    result.extend(left[l:])
    result.extend(right[r:])
    return result

arr = [23,54,34,12,114,14,25]
result = mergesort(arr)
print(result)

