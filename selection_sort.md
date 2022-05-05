# 선택 **정렬 (Selection Sort)**

**`선택 정렬`은 입력 배열 전체에서 최솟값을 선택하여 배열의 0번째 원소와 자리를 바꾸고, 다음에는 0번째 원소를 제외한 나머지 원소에서 최솟값을 선택하여 배열의 1번째 원소와 자리를 바꾼다. 이러한 방식으로 마지막에 2개의 원소 중에서 작은 값을 선택하여 자리를 바꿈으로써 정렬하는 알고리즘**이다.

## 선택 **정렬** 알고리즘

```
def selection_sort(A):
	# 입력: 배열 A
	# 출력: 정렬된 배열 A
	n = len(A)
	for i = 0 to n - 2:
		min = i
		for j = i + 1 to n - 1:
			if A[j] < A[min]:
				min = j
		A[i]와 A[min]의 자리를 바꿈
	return A
```

아래와 같은 배열이 있다.

A = [40, 10, 50, 90, 20, 80, 30, 60]

위 수도코드를 이 배열에 대해 선택 정렬이 수행되는 과정은 다음과 같다.

**[i = 0]**

![https://user-images.githubusercontent.com/63987872/166850757-8d0580b4-cbdf-4d1b-a3c1-e1a0f9d899b9.png](https://user-images.githubusercontent.com/63987872/166850757-8d0580b4-cbdf-4d1b-a3c1-e1a0f9d899b9.png)

i = 0 일 때 A[0]~A[7] 중 최솟값은 10으로 최솟값의 인덱스인 min은 1이 된다. i와 min의 위치를 스왑하여 인덱스가 0과 1의 위치를 스왑한다.

**[i = 1]**

![https://user-images.githubusercontent.com/63987872/166850758-0bb42b6b-cf3c-409e-aaa3-58019f2abd07.png](https://user-images.githubusercontent.com/63987872/166850758-0bb42b6b-cf3c-409e-aaa3-58019f2abd07.png)

i = 1 일 때 A[1]~A[7] 중 최솟값은 20으로 최솟값의 인덱스인 min은 4이 된다. i와 min의 위치를 스왑하여 인덱스가 1과 4의 위치를 스왑한다.

**[i = 2]**

![https://user-images.githubusercontent.com/63987872/166850759-17f8bf62-6fb8-4350-baaf-5be9a951e0c4.png](https://user-images.githubusercontent.com/63987872/166850759-17f8bf62-6fb8-4350-baaf-5be9a951e0c4.png)

i = 2 일 때 A[2]~A[7] 중 최솟값은 30으로 최솟값의 인덱스인 min은 6이 된다. i와 min의 위치를 스왑하여 인덱스가 2과 6의 위치를 스왑한다.

...

**[i = 6]**

![https://user-images.githubusercontent.com/63987872/166850761-99f7db0a-73ca-4849-a1bc-6d17daeb6b1c.png](https://user-images.githubusercontent.com/63987872/166850761-99f7db0a-73ca-4849-a1bc-6d17daeb6b1c.png)

최종적으로 작은 숫자들이 모두 앞쪽으로 배치되어 정렬되는 것을 확인할 수 있다.

## 구현

```python
def selection_sort(A, n):
  for i in range(0, n - 1):
    min = i

    for j in range(i + 1, n):
      if A[j] < A[min]:
        min = j

    A[i], A[min] = A[min], A[i]

  return A

A = [40, 10, 50, 90, 20, 80, 30, 60]

selection_sort(A, len(A))

print(A)
```
