def quick_sort(A, left=0, right=None):
    if right is None:
        right = len(A) - 1
    if left < right:
        p = partition(A, left, right)
        quick_sort(A, left, p)
        quick_sort(A, p + 1, right)


def partition(A, left, right):
    pivot = A[(left + right) // 2]
    low = left - 1
    high = right + 1
    while True:
        low += 1
        while A[low] < pivot:
            low += 1
        high -= 1
        while A[high] > pivot:
            high -= 1

        if low >= high:
            return high

        A[low], A[high] = A[high], A[low]


A = [5, 8, 3, 1, 2, 7, 6, 4]
quick_sort(A)
print(A)
