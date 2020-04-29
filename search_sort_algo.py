"""
Some search and Sort algorithms
Course: Algorithms and Programming for Intelligent Systems
Semester: SS 2020
"""


def linear_search(lst, key):
    pos = 0
    while pos < len(lst):
        if lst[pos] == key:
            return pos
        pos += 1

    return -1


# search a sorted list for a key using binary search
def binary_search(lst, key):
    first = 0
    last = len(lst) - 1
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == key:
            return mid
        else:
            if key < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return -1


# bubble sort a list
def bubble_sort(lst):
    n = len(lst)
    for i in range(0, n):
        for j in range(n - 1, i, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]  # swap


# merge two sorted lists
def merge_lists(list1, list2):
    size1 = len(list1)
    size2 = len(list2)
    result = []
    i, j = 0, 0

    while i < size1 and j < size2:
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result = result + list1[i:] + list2[j:]
    return result


# merge sort with returned list
def mergeSort(list):
    if len(list) <= 1:
        return list
    else:
        mid = len(list) // 2
        left_half = list[:mid]
        right_half = list[mid:]

        left_half = mergeSort(left_half)
        right_half = mergeSort(right_half)
        return merge_lists(left_half, right_half)
        # return merge_lists(mergeSort(left_half), mergeSort(right_half)) # this is equivalent


# -----------------------------------------------------
# Driver Code
my_arr = [40, 20, 90, 70, 10, 30, 80, 50, 100, 60]

print(linear_search(my_arr, 70))
print(linear_search(my_arr, 45))


my_sorted_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(binary_search(my_sorted_list, 80))
print(binary_search(my_sorted_list, 33))

# bubble_sort(my_arr)
# print(my_arr)


list_a = [1, 6, 8, 12, 15, 16, 19, 21, 45]
list_b = [3, 6, 9, 10, 15, 44]
list_c = merge_lists(list_a, list_b)
print(list_c)

my_arr2 = mergeSort(my_arr)
print(my_arr2)