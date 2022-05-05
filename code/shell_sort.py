def shell_sort(A):
    n = len(A)
    m = n // 3 + 1
    gap = []
    while True:
        gap.append(m)
        if m == 1:
            break
        m = m // 3 + 1

    for h in gap:
        for i in range(h, n):
            CurrentElement = A[i]
            j = i
            while j >= h and A[j - h] > CurrentElement:
                A[j] = A[j - h]
                j -= h
            A[j] = CurrentElement


A = [5, 8, 3, 1, 2, 7, 6, 4]
shell_sort(A)
print(A)
