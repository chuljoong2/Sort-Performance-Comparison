# 버블 정렬 (Bubble Sort)

**`버블 정렬`은 이웃하는 숫자를 비교하여 작은 수를 앞쪽으로 이동시키는 과정을 반복하여 정렬하는 알고리즘**이다.

작은 수는 배열의 앞부분으로 이동하는데 배열을 좌우가 아니라 상하로 그려보면 정렬하는 과정에서 작은 수가 마치 거품처럼 위로 올라가는 것을 연상케 한다.

## **버블 정렬** 알고리즘

```
def bubble_sort(A):
	# 입력: 배열 A
	# 출력: 정렬된 배열 A
	n = len(A)
	for pass = 1 to n - 1:
		for i = 1 to n - pass:
			if A[i-1] > A[i]:
				A[i-1]와 A[i]의 자리를 바꿈
	return A
```

아래와 같은 배열이 있다.

A = [40, 10, 50, 90, 20, 80, 30, 60]

위 수도코드를 이 배열에 대해 버블 정렬이 수행되는 과정은 다음과 같다.

**[pass 1]**

![https://user-images.githubusercontent.com/63987872/166850739-a8b37989-2b98-4e69-ac46-3d751ae1da52.png](https://user-images.githubusercontent.com/63987872/166850739-a8b37989-2b98-4e69-ac46-3d751ae1da52.png)

최종적으로 pass 1에서 즉, 첫 번째 시도에서 첫 번째로 큰 수가 맨 마지막에 가는 것을 확인할 수 있다.

**[pass 2]**

![https://user-images.githubusercontent.com/63987872/166850743-4ce0e05c-328d-471e-b7b1-cae0027a9d91.png](https://user-images.githubusercontent.com/63987872/166850743-4ce0e05c-328d-471e-b7b1-cae0027a9d91.png)

**[pass 3]**

![https://user-images.githubusercontent.com/63987872/166850744-ca4a70d6-74d4-410f-b972-5876ed3f77ea.png](https://user-images.githubusercontent.com/63987872/166850744-ca4a70d6-74d4-410f-b972-5876ed3f77ea.png)

**[pass 4]**

![https://user-images.githubusercontent.com/63987872/166850745-6e5b7e7b-ee51-40c1-817f-7b6f30413f81.png](https://user-images.githubusercontent.com/63987872/166850745-6e5b7e7b-ee51-40c1-817f-7b6f30413f81.png)

**[pass 5]** ~ **[pass 7]**

pass 4의 결과와 동일하다.

pass가 진행함에 따라 가장 큰 수가 뒤로 가면서 정렬되는 것을 알 수 있다. 또한 pass는 len(A)-1번 진행된다.

## 구현

```python
def bubble_sort(A, n):
  for p in range(1, n):
    for i in range(1, n - p + 1):
      if A[i - 1] > A[i]:
        A[i - 1], A[i] = A[i], A[i - 1]

  return A

A = [40, 10, 50, 90, 20, 80, 30, 60]

bubble_sort(A, len(A))

print(A)
```
