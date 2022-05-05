import heapq


def heap_sort(A):
    heap = []
    H = []

    for item in A:
        heapq.heappush(heap, item)
    while len(heap):
        H.append(heapq.heappop(heap))

    return H


A = [5, 8, 3, 1, 2, 7, 6, 4]
H = heap_sort(A)
print(H)
