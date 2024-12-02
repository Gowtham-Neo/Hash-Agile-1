def secondLargest(arr):
    if len(arr) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')  

    for i in arr:
        if i > largest:
            second_largest = largest
            largest = i
        elif i > second_largest and i < largest:
            second_largest = i

    return second_largest if second_largest != float('-inf') else None


arr=[1,2,3,4,5]
print("The Second largest Number for the given arr is ",secondLargest(arr))