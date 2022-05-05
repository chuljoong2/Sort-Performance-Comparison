def selection_sort(A):
    n = len(A)
    for i in range(0, n - 1):
        min = i
        for j in range(i + 1, n):
            if A[j] < A[min]:
                min = j
        A[i], A[min] = A[min], A[i]


A = [5, 8, 3, 1, 2, 7, 6, 4]
selection_sort(A)
print(A)
