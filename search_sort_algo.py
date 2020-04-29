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


# -----------------------------------------------------
# Driver Code
my_arr = [40, 20, 90, 70, 10, 30, 80, 50, 100, 60]

print(linear_search(my_arr, 70))
print(linear_search(my_arr, 45))


my_sorted_ist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(binary_search(my_sorted_ist, 80))
print(binary_search(my_sorted_ist, 33))
