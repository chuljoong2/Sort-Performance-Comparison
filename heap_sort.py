def insert(h, item):
    h.append(item)
    i = len(h) - 1
    while i > 1:
        if h[i] > h[i // 2]:
            h[i], h[i // 2] = h[i // 2], h[i]
        i //= 2


def downheap(i, H, size):
    left = i * 2
    right = i * 2 + 1
    smallest = i

    if left <= size and H[left] > H[smallest]:
        smallest = left
    if right <= size and H[right] > H[smallest]:
        smallest = right
    if smallest != i:
        H[smallest], H[i] = H[i], H[smallest]
        downheap(smallest, H, size)


def heap_sort(A):
    H = [None]
    for item in A:
        insert(H, item)
    n = len(A)
    heapsize = n
    for _ in range(n):
        H[1], H[heapsize] = H[heapsize], H[1]
        heapsize -= 1
        downheap(1, H, heapsize)

    return H


A = [10, 30, 50, 80, 60, 70, 40, 90, 20]
print(heap_sort(A))
