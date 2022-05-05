def insertion_sort(A, n):
    for i in range(1, n):
        # i = 1 to n - 1
        current_element = A[i]
        j = i - 1
        while j >= 0 and A[j] > current_element:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = current_element
    return A


A = [40, 10, 50, 90, 20, 80, 30, 60]
insertion_sort(A, len(A))
print(A)
