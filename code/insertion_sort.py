def insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        current_element = A[i]
        j = i - 1
        while j >= 0 and A[j] > current_element:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = current_element


A = [5, 8, 3, 1, 2, 7, 6, 4]
insertion_sort(A)
print(A)
