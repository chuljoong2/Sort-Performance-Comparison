def quick_sort(A, left, right):
    if left >= right:
        # left == right: 원소가 1개인 경우
        # left > right: 원소가 0개인 경우
        return

    pivot = left
    low = left + 1
    high = right

    while low <= high:
        while low <= right and A[pivot] >= A[low]:
            # 피봇보다 큰 숫자를 찾을 때 까지 왼쪽에서 이동
            low += 1
        while high > left and A[pivot] <= A[high]:
            # 피봇보다 작 숫자를 찾을 때 까지 오른쪽에서 이동
            high -= 1

        if low > high:
            # 엇갈렸다면 작은 숫자(현재 high)와 피봇을 swap
            A[high], A[pivot] = A[pivot], A[high]
        else:
            # 엇갈리지 않았다면 작은 숫자와 큰 숫자를 swap
            A[low], A[high] = A[high], A[low]

    quick_sort(A, left, high - 1)  # 현재 high에는 swap했기 때문에 피봇이 위치
    quick_sort(A, high + 1, right)

    return A


A = [5, 3, 8, 4, 9, 1, 6, 2, 7]
quick_sort(A, 0, len(A) - 1)
print(A)
