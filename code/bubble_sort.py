def bubble_sort(A):
    n = len(A)
    for p in range(1, n):
        for i in range(1, n - p + 1):
            if A[i - 1] > A[i]:
                A[i - 1], A[i] = A[i], A[i - 1]


A = [5, 8, 3, 1, 2, 7, 6, 4]
bubble_sort(A)
print(A)
