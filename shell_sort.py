def shell_sort(A, gap):
    n = len(A)
    for h in gap:
        for i in range(h, n):
            CurrentElement = A[i]
            j = i
            while j >= h and A[j - h] > CurrentElement:
                A[j] = A[j - h]
                j -= h
            A[j] = CurrentElement
    return A


A = [30, 60, 90, 10, 40, 80, 40, 20, 10, 60, 50, 30, 40, 90, 80]
n = len(A) // 3 + 1
gap = []

while True:
    gap.append(n)
    if n == 1:
        break
    n = n // 3 + 1

shell_sort(A, gap)
print(A)
