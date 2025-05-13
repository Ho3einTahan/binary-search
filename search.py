def binarySearch(list, target):
    left, right = 0, len(list) - 1

    while left <= right:

        middle = left + right

        if target > list[middle]:
            left = middle + 1
        elif target < list[middle]:
            right = middle - 1
        else:
            return middle
    return -1


print(binarySearch([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 60))
